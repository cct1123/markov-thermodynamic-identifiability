"""Full-six-rate conditioning and finite-record inference for one resolved pair.

Reproduce: .venv/Scripts/python.exe -B -m analysis.revision.inference --replicates 100
The numerical rate box is an explicit estimator constraint, not a theorem prior.
No accepted historical output is modified. See STATISTICS.md for assumptions.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import itertools
import json
from pathlib import Path
import platform
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.linalg import block_diag
from scipy.optimize import least_squares


RATE_NAMES = ("r", "s", "a", "c", "b", "d")
EDGES = ((0, 1), (1, 0), (0, 2), (1, 2), (2, 0), (2, 1))
RESET = np.array([[0., 1., 0.], [1., 0., 0.]])
DT = np.zeros((6, 3, 3))
DB = np.zeros((6, 3, 2))
for _j, (_src, _dst) in enumerate(EDGES):
    DT[_j, _src, _src] = -1
    if _j >= 2:
        DT[_j, _src, _dst] = 1
    else:
        DB[_j, _j, _j] = 1

DEFAULT_LAMBDAS = np.array([0.2, 1., 5.])
LOWER, UPPER = 1e-14, 20.
STARTS = np.array([[1., 1., 1., 1., 1., 1.],
                   [1., 1., .2, 1., .01, 1.],
                   [1., 1., 1., .2, 1., .01]])


def generator(rates):
    """Row generator; state order x,y,h and rate order r,s,a,c,b,d."""
    p = np.asarray(rates)
    q = np.zeros((3, 3), dtype=p.dtype)
    for value, (i, j) in zip(p, EDGES):
        q[i, j] = value
        q[i, i] -= value
    return q


def stationary(rates):
    q = generator(rates)
    system = q.T.copy()
    system[-1] = 1
    return np.linalg.solve(system, np.array([0., 0., 1.]))


def laplace(rates, lambdas, with_jacobian=False):
    """Returns Psi[incoming mark, lambda index, outgoing mark] and raw J.

    Marks +=x->y (index 0) and -=y->x (index 1); no conditional-next-label
    normalization. dPsi=R K(dT)K B + R K(dB), K=(lambda I-T)^(-1).
    """
    p, ls = np.asarray(rates), np.asarray(lambdas)
    t = generator(p)
    t[0, 1] = t[1, 0] = 0
    b = np.zeros((3, 2), dtype=p.dtype)
    b[0, 0], b[1, 1] = p[:2]
    k = np.linalg.inv(ls[:, None, None]*np.eye(3)-t)
    kb = k @ b
    rk = RESET @ k
    values = (RESET @ kb).transpose(1, 0, 2)
    if not with_jacobian:
        return values
    # Axes: lambda, incoming, outgoing, parameter -> incoming,lambda,out,param.
    j = np.einsum("lia,pab,lbj->lijp", rk, DT, kb)
    j += np.einsum("lia,paj->lijp", rk, DB)
    return values, j.transpose(1, 0, 2, 3).reshape(-1, 6)


def entropy(rates, with_gradient=False):
    """Cycle expression and raw gradient; strictly positive rates required."""
    r, s, a, c, b, d = np.asarray(rates)
    u = s*a*d-r*c*b
    z = s*b+s*d+c*b+r*b+r*d+a*d+a*c+a*s+r*c
    aff = np.log(s)+np.log(a)+np.log(d)-np.log(r)-np.log(c)-np.log(b)
    value = u*aff/z
    if not with_gradient:
        return value
    du = np.array([-c*b, a*d, s*d, -r*b, -r*c, s*a])
    dz = np.array([b+d+c, b+d+a, d+c+s, b+a+r, s+c+r, s+r+a])
    daff = np.array([-1/r, 1/s, 1/a, -1/c, -1/b, 1/d])
    return value, (du/z-u*dz/z**2)*aff+(u/z)*daff


def fixed_trace_rates(epsilon, reverse):
    return np.array([1., 1., epsilon, 1-reverse, reverse, 1-epsilon])


def simulate_marked_ctmc(rates, n_records, rng):
    """Actual Gillespie trajectory, initialized in stationarity.

    Discard the censored interval before the first mark. Retain n_records
    complete inter-mark intervals. Stop at an observed event (random horizon).
    Hidden-jump counts are diagnostics only and are never passed to inference.
    """
    p = np.asarray(rates, dtype=float)
    if not np.all(p > 0):
        raise ValueError("Simulation requires six positive, representable rates")
    q = generator(p)
    escapes = -np.diag(q)
    destinations = np.array([[1, 2], [0, 2], [0, 1]])
    probability_first = np.array([p[0], p[1], p[4]]) / escapes
    state = int(rng.choice(3, p=stationary(p)))
    incoming = np.empty(n_records, dtype=np.int8)
    outgoing = np.empty(n_records, dtype=np.int8)
    times = np.empty(n_records)
    jumps = np.zeros((3, 3), dtype=np.int64)
    previous_mark, elapsed, horizon, index = -1, 0., 0., 0
    while index < n_records:
        wait = rng.exponential(1/escapes[state])
        elapsed += wait
        horizon += wait
        next_state = int(destinations[state, int(rng.random() >= probability_first[state])])
        jumps[state, next_state] += 1
        mark = 0 if state == 0 and next_state == 1 else (
            1 if state == 1 and next_state == 0 else -1)
        if mark >= 0:
            if previous_mark >= 0:
                incoming[index], outgoing[index], times[index] = previous_mark, mark, elapsed
                index += 1
            previous_mark, elapsed = mark, 0.
        state = next_state
    return {"incoming": incoming, "outgoing": outgoing, "times": times,
            "horizon": horizon, "microscopic_counts": jumps}


def empirical_moments(record, lambdas):
    """Row means and consistent martingale covariance of the row estimators.

    The blocks do NOT assume iid successive marks. The centered row features
    are martingale differences conditional on the previous resolved mark.
    The ratio-estimator covariance is conditional feature covariance / n_I.
    """
    ls = np.asarray(lambdas)
    moments, covariances, counts = [], [], []
    for mark in range(2):
        selected = record["incoming"] == mark
        count = int(selected.sum())
        if count < 2:
            raise ValueError("Each incoming-mark row requires at least two records")
        features = (np.exp(-record["times"][selected, None, None]*ls[None, :, None])
                    * (record["outgoing"][selected, None, None] == np.arange(2)[None, None, :]))
        moments.append(features.mean(axis=0))
        covariances.append(np.cov(features.reshape(count, -1), rowvar=False, ddof=1)/count)
        counts.append(count)
    return np.array(moments), block_diag(*covariances), counts


def theoretical_moment_covariance(rates, lambdas):
    """Asymptotic covariance of sqrt(n) empirical row moments (n total)."""
    ls = np.asarray(lambdas)
    values = laplace(rates, ls)
    pi = stationary(rates)
    mark_fluxes = pi[:2]*np.asarray(rates)[:2]
    fractions = mark_fluxes/mark_fluxes.sum()
    sums = laplace(rates, (ls[:, None]+ls[None, :]).ravel()).reshape(2, len(ls), len(ls), 2)
    blocks = []
    for mark in range(2):
        f = values[mark].ravel()
        second = np.zeros((len(f), len(f)))
        for j in range(len(ls)):
            for k in range(len(ls)):
                for outgoing in range(2):
                    second[2*j+outgoing, 2*k+outgoing] = sums[mark, j, k, outgoing]
        blocks.append((second-np.outer(f, f))/fractions[mark])
    return block_diag(*blocks)


def fit_rates(moments, lambdas=DEFAULT_LAMBDAS, lower=LOWER, upper=UPPER):
    """Unweighted constrained nonlinear moments; three fixed starts, six rates.

    Fixed starts contain no true parameters. All candidates/statuses are retained
    in the count diagnostics; best objective is selected, even on optimizer failure.
    No zero-rate clipping or hidden reverse-edge epsilon is applied to data/models.
    """
    target = np.asarray(moments).ravel()
    def residual(z):
        return laplace(np.exp(z), lambdas).ravel()-target
    def jac(z):
        p = np.exp(z)
        return laplace(p, lambdas, True)[1]*p[None, :]
    candidates = [least_squares(residual, np.log(start), jac=jac,
                                bounds=(np.log(lower), np.log(upper)),
                                ftol=1e-10, xtol=1e-10, gtol=1e-10, max_nfev=350)
                  for start in STARTS]
    best = min(candidates, key=lambda fit: fit.cost)
    p = np.exp(best.x)
    return {"rates": p, "cost": float(best.cost), "success": bool(best.success),
            "nfev": sum(f.nfev for f in candidates),
            "boundary": bool(np.any(p < 10*lower) or np.any(p > .999*upper)),
            "failed_starts": sum(not f.success for f in candidates),
            "status": int(best.status), "optimality": float(best.optimality)}


def delta_interval(rates, covariance, lambdas=DEFAULT_LAMBDAS):
    """Pointwise asymptotic sandwich Wald interval, unavailable if rank unresolved.

    Covariance is for the empirical moment vector (not sqrt(n) moments).
    Boundary flags are handled by the caller; no nominal validity is asserted there.
    """
    _, j = laplace(rates, lambdas, True)
    jlog = j*np.asarray(rates)[None, :]
    u, s, vt = np.linalg.svd(jlog, full_matrices=False)
    value, gradient = entropy(rates, True)
    if s[-1] <= 1e-12*s[0]:
        return {"interval": None, "se": None, "log_condition": float(s[0]/s[-1]),
                "rate_log_se": None, "rank_unresolved": True}
    inverse = (vt.T/s)@u.T
    cov_log = inverse@covariance@inverse.T
    gradient_log = gradient*rates
    variance = float(gradient_log@cov_log@gradient_log)
    if variance < -1e-10*max(1., float(np.linalg.norm(cov_log))):
        raise ArithmeticError("Negative delta variance exceeds rounding tolerance")
    se = float(np.sqrt(max(0., variance)))
    return {"interval": [max(0., float(value)-1.959963984540054*se),
                         float(value)+1.959963984540054*se],
            "se": se, "log_condition": float(s[0]/s[-1]),
            "rate_log_se": np.sqrt(np.maximum(0., np.diag(cov_log))).tolist(),
            "rank_unresolved": False}


def conditioning_study(figure_dir):
    """Deterministic diagnostics, not proof certificates or universal design optima."""
    reference = np.array([1.2, .8, .9, .4, .3, 1.1])
    scales = np.logspace(-3, 3, 49)
    ratios = np.geomspace(1.001, 100, 45)
    condition = np.empty((len(ratios), len(scales)))
    minimum = np.empty_like(condition)
    for i, ratio in enumerate(ratios):
        for j, scale in enumerate(scales):
            _, jac = laplace(reference, scale*np.array([1/ratio, 1., ratio]), True)
            ss = np.linalg.svd(jac*reference, compute_uv=False)
            condition[i, j], minimum[i, j] = ss[0]/ss[-1], ss[-1]
    reverse_rates = np.logspace(-12, -1, 70)
    boundary = []
    for reverse in reverse_rates:
        p = fixed_trace_rates(.2, reverse)
        _, j = laplace(p, DEFAULT_LAMBDAS, True)
        raw = np.linalg.svd(j, compute_uv=False)
        _, logs, vt = np.linalg.svd(j*p, full_matrices=False)
        boundary.append({"reverse": float(reverse), "min_rate": float(p.min()),
                         "raw_singular_values": raw.tolist(), "log_singular_values": logs.tolist(),
                         "raw_condition": float(raw[0]/raw[-1]),
                         "log_condition": float(logs[0]/logs[-1]),
                         "weakest_log_direction": vt[-1].tolist()})
    tree_p = fixed_trace_rates(0., 0.)
    tree_sv = np.linalg.svd(laplace(tree_p, DEFAULT_LAMBDAS, True)[1], compute_uv=False)
    diagonal = []
    for e in np.linspace(.22, .49, 55):
        k = np.exp(-1/e**2)  # smallest is >1e-9, no float underflow.
        p = fixed_trace_rates(e, k)
        _, j = laplace(p, DEFAULT_LAMBDAS, True)
        sr, sl = np.linalg.svd(j, compute_uv=False), np.linalg.svd(j*p, compute_uv=False)
        diagonal.append({"epsilon": float(e), "reverse": float(k), "entropy": float(entropy(p)),
                         "raw_min_singular": float(sr[-1]), "log_min_singular": float(sl[-1])})
    designs = []
    candidate_points = [.025, .05, .1, .2, .5, 1., 2., 5., 10., 20., 40.]
    for points in itertools.combinations(candidate_points, 3):
        _, j = laplace(reference, points, True)
        ss = np.linalg.svd(j*reference, compute_uv=False)
        asymptotic = delta_interval(reference, theoretical_moment_covariance(reference, points), points)
        designs.append({"lambdas": list(points), "log_min_singular": float(ss[-1]),
                        "log_condition": float(ss[0]/ss[-1]),
                        "entropy_se_times_sqrt_n": asymptotic["se"]})
    largest_min = max(designs, key=lambda d: d["log_min_singular"])
    best_entropy = min(designs, key=lambda d: d["entropy_se_times_sqrt_n"])
    default_cov = theoretical_moment_covariance(reference, DEFAULT_LAMBDAS)
    default_asymptotic = delta_interval(reference, default_cov)

    result = {"reference_rates": reference.tolist(), "default_lambdas": DEFAULT_LAMBDAS.tolist(),
              "scales": scales.tolist(), "point_ratios": ratios.tolist(),
              "log_rate_condition_heatmap": condition.tolist(),
              "log_rate_min_singular_heatmap": minimum.tolist(),
              "fixed_e_boundary": boundary, "sparse_diagonal": diagonal,
              "tree_raw_singular_values": tree_sv.tolist(),
              "design_candidate_points": candidate_points, "design_count": len(designs),
              "design_largest_log_min_singular": largest_min,
              "design_smallest_entropy_asymptotic_se": best_entropy,
              "default_entropy_se_times_sqrt_n": default_asymptotic["se"],
              "designs": designs}
    plot_conditioning(result, figure_dir)
    return result


def publication_style():
    """At 6.3in manuscript width, 12pt labels become approximately 7.6pt."""
    plt.rcParams.update({"font.size": 12, "axes.labelsize": 12, "axes.titlesize": 12,
                         "xtick.labelsize": 12, "ytick.labelsize": 12,
                         "legend.fontsize": 11, "axes.spines.top": False,
                         "axes.spines.right": False, "pdf.fonttype": 42})


def save_publication_figure(fig, figure_dir, stem):
    fig.savefig(figure_dir/f"{stem}.pdf", metadata={"CreationDate": None, "ModDate": None})
    fig.savefig(figure_dir/f"{stem}.png", dpi=250)
    plt.close(fig)


def plot_conditioning(result, figure_dir):
    """Redraw only: every scientific value is taken from the saved payload."""
    publication_style()
    scales, ratios = result["scales"], result["point_ratios"]
    condition = np.asarray(result["log_rate_condition_heatmap"])
    boundary = result["fixed_e_boundary"]
    reverse_rates = [entry["reverse"] for entry in boundary]
    fig, axes = plt.subplots(1, 3, figsize=(10., 3.6), constrained_layout=True)
    mesh = axes[0].pcolormesh(scales, ratios, np.log10(condition), shading="auto", cmap="viridis")
    axes[0].set(xscale="log", yscale="log", xlabel=r"Laplace center $c$", ylabel=r"Point ratio $v$",
                title="(a) Laplace design")
    fig.colorbar(mesh, ax=axes[0], label=r"$\log_{10}\,\mathrm{cond}(J_{\log})$")
    axes[1].loglog(reverse_rates, [x["raw_singular_values"][-1] for x in boundary],
                   label="raw rates", color="#0072B2")
    axes[1].loglog(reverse_rates, [x["log_singular_values"][-1] for x in boundary],
                   label="log rates", color="#D55E00")
    axes[1].set(xlabel=r"Reverse rate $k$", ylabel="Smallest singular value",
                title="(b) Rate sensitivity")
    axes[1].legend(frameon=False)
    axes[2].semilogx(reverse_rates, [abs(x["weakest_log_direction"][4]) for x in boundary],
                     color="#009E73", label=r"$|v_{\min,b}|$")
    axes[2].set(xlabel=r"Reverse rate $b=k$", ylabel=r"Weakest $b$ component",
                ylim=(0, 1.04), title="(c) Weak direction")
    axes[2].legend(frameon=False)
    save_publication_figure(fig, figure_dir, "conditioning")


def wilson_interval(successes, count):
    if not count:
        return None
    z = 1.959963984540054
    p = successes/count
    den = 1+z*z/count
    center = (p+z*z/(2*count))/den
    half = z*np.sqrt(p*(1-p)/count+z*z/(4*count**2))/den
    return [float(center-half), float(center+half)]


def finite_data_study(replicates, sample_sizes, seed, figure_dir):
    models = {"interior": np.array([1.2, .8, .9, .4, .3, 1.1]),
              "moderately_sparse": fixed_trace_rates(.2, .01),
              "rare_reverse": fixed_trace_rates(.2, np.exp(-25.))}
    root_seed = np.random.SeedSequence(seed)
    children = root_seed.spawn(len(models)*len(sample_sizes)*replicates)
    cases, serial = [], 0
    for name, truth in models.items():
        truth_entropy = float(entropy(truth))
        for n in sample_sizes:
            runs = []
            for rep in range(replicates):
                child = children[serial]
                serial += 1
                trajectory = simulate_marked_ctmc(truth, n, np.random.default_rng(child))
                estimate, covariance, counts = empirical_moments(trajectory, DEFAULT_LAMBDAS)
                fit = fit_rates(estimate)
                rates = fit.pop("rates")
                uncertainty = delta_interval(rates, covariance)
                available = fit["success"] and not fit["boundary"] and not uncertainty["rank_unresolved"]
                interval = uncertainty["interval"]
                covered = bool(interval is not None and interval[0] <= truth_entropy <= interval[1])
                same_mark_counts = [int(np.sum((trajectory["incoming"] == mark)
                                               & (trajectory["outgoing"] == mark))) for mark in range(2)]
                # A transparent practical warning, NOT a coverage theorem. Zero
                # same-mark events make the corresponding empirical row-feature
                # covariance zero and can produce badly optimistic Wald errors.
                adequate_same_mark_counts = min(same_mark_counts) >= 20
                runs.append({"replicate": rep, "seed_spawn_key": list(child.spawn_key),
                             "row_counts": counts, "duration": float(trajectory["horizon"]),
                             "same_mark_counts": same_mark_counts,
                             "rare_mark_warning": not adequate_same_mark_counts,
                             "screened_delta_interval": interval if available and adequate_same_mark_counts else None,
                             "hidden_reverse_count": int(trajectory["microscopic_counts"][2, 0]),
                             "rates": rates.tolist(), "entropy": float(entropy(rates)),
                             "fit": fit, "uncertainty": uncertainty,
                             "interior_interval_available": available, "raw_wald_covered": covered,
                             "moment_residual_max": float(np.max(np.abs(laplace(rates, DEFAULT_LAMBDAS)-estimate)))})
            values = np.array([run["entropy"] for run in runs])
            rate_values = np.array([run["rates"] for run in runs])
            available_runs = [run for run in runs if run["interior_interval_available"]]
            n_available = len(available_runs)
            n_covered = sum(run["raw_wald_covered"] for run in available_runs)
            interior_widths = [run["uncertainty"]["interval"][1]-run["uncertainty"]["interval"][0]
                               for run in available_runs]
            summary = {"bias": float(values.mean()-truth_entropy),
                       "variance": float(values.var(ddof=1)) if replicates > 1 else None,
                       "rmse": float(np.sqrt(np.mean((values-truth_entropy)**2))),
                       "entropy_quantiles_05_50_95": np.quantile(values, [.05, .5, .95]).tolist(),
                       "rate_bias": (rate_values.mean(axis=0)-truth).tolist(),
                       "rate_variance": rate_values.var(axis=0, ddof=1).tolist() if replicates > 1 else None,
                       "optimizer_failure_count": sum(not run["fit"]["success"] for run in runs),
                       "boundary_fit_count": sum(run["fit"]["boundary"] for run in runs),
                       "rank_unresolved_count": sum(run["uncertainty"]["rank_unresolved"] for run in runs),
                       "interior_interval_count": n_available,
                       "rare_mark_warning_count": sum(run["rare_mark_warning"] for run in runs),
                       "screened_delta_interval_count": sum(run["screened_delta_interval"] is not None for run in runs),
                       "interior_covered_count": n_covered,
                       "conditional_interior_coverage": n_covered/n_available if n_available else None,
                       "conditional_coverage_wilson95": wilson_interval(n_covered, n_available),
                       "covered_and_interior_fraction": n_covered/replicates,
                       "raw_wald_coverage_ignoring_boundary_validity": sum(run["raw_wald_covered"] for run in runs)/replicates,
                       "median_interior_interval_width": float(np.median(interior_widths)) if interior_widths else None,
                       "median_duration": float(np.median([run["duration"] for run in runs])),
                       "no_hidden_reverse_count": sum(run["hidden_reverse_count"] == 0 for run in runs),
                       "median_moment_residual_max": float(np.median([run["moment_residual_max"] for run in runs]))}
            case = {"model": name, "truth_rates": truth.tolist(), "truth_entropy": truth_entropy,
                    "n_records": n, "replicates": replicates, "summary": summary, "runs": runs}
            cases.append(case)
            print(json.dumps({key: case[key] for key in ("model", "n_records", "truth_entropy", "summary")}), flush=True)
    plot_finite_data(cases, figure_dir)
    return {"seed": seed, "rng": "numpy.default_rng / PCG64; SeedSequence.spawn per run",
            "record_sampling": "n complete inter-mark intervals after first observed mark; stationary CTMC initialization",
            "sample_sizes": list(sample_sizes), "replicates_per_case": replicates,
            "lambdas": DEFAULT_LAMBDAS.tolist(), "rate_order": list(RATE_NAMES),
            "rate_box": [LOWER, UPPER], "fixed_starts": STARTS.tolist(),
            "optimizer": {"method": "scipy.optimize.least_squares / trf", "residual": "unweighted joint-Laplace moment residual",
                          "coordinates": "natural logarithms of all six rates", "ftol": 1e-10,
                          "xtol": 1e-10, "gtol": 1e-10, "max_nfev_per_start": 350},
            "interval": "pointwise asymptotic martingale-sandwich delta Wald, intersected with [0,infinity)",
            "interior_screen": "successful optimum; all rates in [10*lower,0.999*upper]; smin(Jlog)>1e-12*smax(Jlog)",
            "rare_mark_screen": "suppress suggested delta interval when either observed same-mark count is below 20; heuristic only, not a finite-sample coverage guarantee",
            "cases": cases}


def plot_finite_data(cases, figure_dir):
    """Redraw the saved Monte Carlo summaries without resampling or refitting."""
    publication_style()
    fig, axes = plt.subplots(1, 3, figsize=(10., 3.6), constrained_layout=True)
    colors = {"interior": "#0072B2", "moderately_sparse": "#D55E00", "rare_reverse": "#009E73"}
    labels = {"interior": "Interior", "moderately_sparse": r"Sparse: $b=10^{-2}$",
              "rare_reverse": r"Rare: $b=e^{-25}$"}
    for name in colors:
        selected = [case for case in cases if case["model"] == name]
        x = [case["n_records"] for case in selected]
        axes[0].loglog(x, [case["summary"]["rmse"] for case in selected], "o-", color=colors[name], label=labels[name])
        axes[1].semilogx(x, [case["summary"]["interior_interval_count"]/case["replicates"] for case in selected],
                         "o-", color=colors[name])
        y = [case["summary"]["conditional_interior_coverage"] if case["summary"]["conditional_interior_coverage"] is not None else np.nan
             for case in selected]
        axes[2].semilogx(x, y, "o-", color=colors[name])
    axes[0].set(xlabel="Observed records", ylabel="Entropy RMSE", title="(a) Point estimates")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncol=3, frameon=False)
    axes[1].set(xlabel="Observed records", ylabel="Interior interval fraction",
                ylim=(-.02, 1.05), title="(b) Interior fits")
    axes[2].set(xlabel="Observed records", ylabel="Coverage among interior fits",
                ylim=(-.02, 1.05), title="(c) Delta coverage")
    axes[2].axhline(.95, color=".45", ls="--", lw=1)
    save_publication_figure(fig, figure_dir, "finite-data")


def redraw_saved_figures(input_path, figure_dir, output_dir):
    """Keep original simulation payload bytes untouched; save a redraw manifest."""
    original = input_path.read_bytes()
    saved = json.loads(original)
    plot_conditioning(saved["conditioning"], figure_dir)
    stems = ["conditioning"]
    if "finite_data" in saved:
        plot_finite_data(saved["finite_data"]["cases"], figure_dir)
        stems.append("finite-data")
    assert input_path.read_bytes() == original
    result = {"kind": "publication figure styling from saved scientific payload; no Monte Carlo rerun",
              "executed_at_utc": datetime.now(timezone.utc).isoformat(),
              "command": ".venv/Scripts/python.exe -B -m analysis.revision.inference " + " ".join(sys.argv[1:]),
              "input": str(input_path), "input_sha256": hashlib.sha256(original).hexdigest(),
              "original_payload_bytes_unchanged": True,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "environment": {"python": platform.python_version(), "numpy": np.__version__,
                              "scipy": scipy.__version__, "matplotlib": matplotlib.__version__},
              "style": {"figure_inches": [10., 3.6], "font_points": 12,
                        "legend_points": 11, "png_dpi": 250,
                        "pdf_creation_and_modification_dates": None},
              "artifact_sha256": {str(path): hashlib.sha256(path.read_bytes()).hexdigest()
                                  for stem in stems for path in
                                  [figure_dir/f"{stem}.pdf", figure_dir/f"{stem}.png"]}}
    output = output_dir/"statistics-figures.json"
    output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "original_payload_bytes_unchanged": True}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replicates", type=int, default=100)
    parser.add_argument("--sample-sizes", type=int, nargs="+", default=[500, 5000, 20000])
    parser.add_argument("--seed", type=int, default=20260914)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/revision"))
    parser.add_argument("--figure-dir", type=Path, default=Path("manuscript/figures"))
    parser.add_argument("--conditioning-only", action="store_true")
    parser.add_argument("--figures-only", action="store_true",
                        help="Redraw saved conditioning/Monte Carlo data without changing the input JSON")
    parser.add_argument("--input", type=Path, default=Path("outputs/revision/statistics.json"),
                        help="Existing statistics payload used only with --figures-only")
    args = parser.parse_args()
    if args.replicates < 2 or min(args.sample_sizes) < 20:
        parser.error("Require at least 2 replicates and 20 complete records")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figure_dir.mkdir(parents=True, exist_ok=True)
    if args.figures_only:
        redraw_saved_figures(args.input, args.figure_dir, args.output_dir)
        return
    payload = {"kind": "illustrative numerical conditioning and finite-data simulation; not proof certificates",
               "executed_at_utc": datetime.now(timezone.utc).isoformat(),
               "command": ".venv/Scripts/python.exe -B -m analysis.revision.inference " + " ".join(sys.argv[1:]),
               "environment": {"python": platform.python_version(), "numpy": np.__version__,
                               "scipy": scipy.__version__, "matplotlib": matplotlib.__version__,
                               "platform": platform.platform()},
               "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "precision": "IEEE float64; tiny rates remain positive, boundary study stops at 1e-12",
               "conditioning": conditioning_study(args.figure_dir)}
    if not args.conditioning_only:
        payload["finite_data"] = finite_data_study(args.replicates, args.sample_sizes, args.seed, args.figure_dir)
    payload["artifact_sha256"] = {str(path): hashlib.sha256(path.read_bytes()).hexdigest()
                                  for stem in (("conditioning",) if args.conditioning_only else ("conditioning", "finite-data"))
                                  for path in [args.figure_dir/f"{stem}.pdf", args.figure_dir/f"{stem}.png"]}
    output = args.output_dir/("statistics-conditioning.json" if args.conditioning_only else "statistics.json")
    output.write_text(json.dumps(payload, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(output), "conditioning_designs": payload["conditioning"]["design_count"]}), flush=True)


if __name__ == "__main__":
    main()
