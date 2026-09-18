"""Reproduce manuscript checks and figures without changing historical evidence.

From repository root:
    .venv/Scripts/python.exe -B manuscript/scripts/reproduce.py
Use --figures-only after a complete run to redraw saved numerical results.
Exact script assertions support specified identities, not universal exhaustion,
novelty or formal verification. The manuscript supplies conventional proofs.
"""
from __future__ import annotations

import argparse
import ast
from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import re
import runpy
import sys
import time
from unittest.mock import patch

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle
import mpmath as mp
import numpy as np
import scipy
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "manuscript/supplementary/computational-results.json"
FIGURES = ROOT / "manuscript/figures"
REPLAYS = [
    "check_small_networks.py", "check_four_state_classification.py",
    "check_observable_criterion.py", "check_state_splitting.py",
    "check_five_state_extensions.py", "check_theta_residue_construction.py",
    "check_theta_fast_spectral.py", "check_balanced_boundary_witness.py",
    "derive_balanced_path.py", "check_balanced_cone_bound.py",
    "check_balanced_cone_sufficiency.py", "check_balanced_fold.py",
    "check_finite_precision_instability.py", "check_three_state_precision.py",
    "check_publication_audit.py",
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scientific_payload(value):
    """Drop run provenance only; retain every scientific result and diagnostic."""
    omitted = {"environment", "python", "sympy", "mpmath", "numpy", "scipy", "platform",
               "command", "command_from_root", "source_sha256", "script_sha256", "created_utc"}
    if isinstance(value, dict):
        return {k: scientific_payload(v) for k, v in value.items()
                if k not in omitted and not k.startswith("executed_at")}
    if isinstance(value, list):
        return [scientific_payload(v) for v in value]
    return value


def changed_paths(a, b, prefix=""):
    if type(a) is not type(b):
        return [prefix]
    if isinstance(a, dict):
        out = []
        for k in sorted(a.keys() | b.keys()):
            if k not in a or k not in b:
                out.append(prefix + "/" + k)
            else:
                out += changed_paths(a[k], b[k], prefix + "/" + k)
        return out
    if isinstance(a, list):
        if len(a) != len(b):
            return [prefix + "/length"]
        return sum((changed_paths(x, y, prefix + "/" + str(i))
                    for i, (x, y) in enumerate(zip(a, b))), [])
    return [] if a == b else [prefix]


def replay(name):
    captured = {}
    transcript = io.StringIO()

    def capture_write(path, data, *args, **kwargs):
        target = Path(path).resolve()
        assert target.is_relative_to(ROOT), str(target)
        assert target.suffix == ".json", str(target)
        captured[target.relative_to(ROOT).as_posix()] = json.loads(data)
        return len(data)

    start = time.perf_counter()
    with patch.object(Path, "write_text", capture_write), redirect_stdout(transcript):
        runpy.run_path(str(ROOT / "analysis" / name), run_name="__main__")
    assert len(captured) == 1, (name, captured.keys())
    destination, result = next(iter(captured.items()))
    original = json.loads((ROOT / destination).read_text(encoding="utf-8"))
    differences = changed_paths(scientific_payload(original), scientific_payload(result))
    return {
        "script": "analysis/" + name, "script_sha256": sha(ROOT / "analysis" / name),
        "elapsed_seconds": round(time.perf_counter() - start, 3),
        "historical_output": destination, "historical_output_sha256": sha(ROOT / destination),
        "assertions_passed": True, "historical_scientific_payload_identical": not differences,
        "changed_scientific_paths": differences, "captured_result": result,
        "stdout": transcript.getvalue(),
    }


def embedded_cone_check():
    path = ROOT / "analysis/publication-endpoint-audit.md"
    blocks = re.findall(r"```python\s*\n(.*?)\n```", path.read_text(encoding="utf-8"), re.S)
    code = next(b for b in blocks if "assert q==expected" in b)
    transcript = io.StringIO()
    with redirect_stdout(transcript):
        exec(compile(code, "<independent-cone-to-path>", "exec"), {})
    return {"source": str(path.relative_to(ROOT)), "source_sha256": sha(path),
            "extracted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
            "assertions_passed": True, "stdout": transcript.getvalue(),
            "scope": "Exact independent cone reconstruction agrees coefficientwise with the path witness; shared source constants and SymPy arithmetic."}


def independent_three_state():
    e, k = sp.symbols("epsilon kappa")
    q = sp.Matrix([[-1-e, 1, e], [1, -2+k, 1-k], [k, 1-e, -1+e-k]])
    expected = [1-e+2*k-k*k, 1+k-e*e, 1-k+2*e-e*k]
    weights = [sp.expand((-q).minor_submatrix(i, i).det()) for i in range(3)]
    assert weights == expected
    z = sp.factor(sum(weights))
    pi = sp.Matrix([weights]) / z
    assert (pi*q).applyfunc(sp.cancel) == sp.zeros(1, 3)
    assert q*sp.ones(3, 1) == sp.zeros(3, 1) and sp.trace(q) == -4
    current = (e-k)*(1-e-k)/z
    cycle = [(0, 2), (2, 1), (1, 0)]
    for i, j in cycle:
        assert sp.cancel(pi[i]*q[i, j] - pi[j]*q[j, i] - current) == 0
    ratio = sp.prod(q[i, j]/q[j, i] for i, j in cycle)
    assert sp.cancel(ratio - e*(1-e)/(k*(1-k))) == 0
    t0 = q.subs({e: 0, k: 0})
    t0[0, 1] = t0[1, 0] = 0
    assert -t0.inv()*sp.ones(3, 1) == sp.Matrix([1, 2, 3])
    return {"assertions_passed": True, "method": "Independent symbolic directed-tree cofactors, stationarity, all three currents, cycle affinity and killed-generator mean times",
            "domain": "0 < kappa < epsilon < 1/2", "trace": "-4",
            "stationary_tree_weights": list(map(str, weights)), "normalizer": str(z),
            "generator_max_entry_error": "epsilon (exact on the stated domain)",
            "joint_row_TV_bound": "2*(epsilon+kappa); analytic coupling bound, not measured TV",
            "source_mean_next_mark_times": [1, 2, 3]}


def stationary(ctx, q):
    system = q.T.copy()
    for j in range(q.rows):
        system[q.rows-1, j] = 1
    return ctx.lu_solve(system, ctx.matrix([0]*(q.rows-1) + [1]))


def flux_entropy(ctx, q, pi):
    total = ctx.mpf(0)
    for i in range(q.rows):
        for j in range(i+1, q.rows):
            if q[i, j] == q[j, i] == 0:
                continue
            assert q[i, j] > 0 and q[j, i] > 0
            f, g = pi[i]*q[i, j], pi[j]*q[j, i]
            total += (f-g)*(ctx.log(f)-ctx.log(g))
    return total


def quantitative_data(endpoint):
    ctx = mp.mp.clone()
    ctx.dps = 100
    root = ctx.findroot(lambda z: 352*z**4-3168*z**3-4644*z*z-11340*z-7623,
                        ctx.mpf("10.557"))

    def decode(coefficients):
        v = ctx.mpf(0)
        for c in coefficients:
            p, _, q = c.partition("/")
            v = v*root + ctx.mpf(p)/ctx.mpf(q or "1")
        return v

    endpoint_models = {}
    for key, certificate in [("source", "entropy_source_certified"),
                             ("target", "entropy_target_certified")]:
        q = ctx.matrix([[decode(v) for v in row] for row in endpoint[key]])
        pi = stationary(ctx, q)
        sigma = flux_entropy(ctx, q, pi)
        bounds = endpoint[certificate]
        assert ctx.mpf(bounds["decimal_lower"]) < sigma < ctx.mpf(bounds["decimal_upper"])
        assert max(abs(sum(pi[i]*q[i, j] for i in range(5))) for j in range(5)) < ctx.mpf("1e-90")
        endpoint_models[key] = {"entropy_100dps": str(sigma), "stationary_100dps": list(map(str, pi)),
                                "certified_entropy_interval": bounds,
                                "support": [[i, j] for i in range(5) for j in range(i+1, 5) if q[i, j] != 0]}

    rows = []
    # Log-grid nodes are rounded decimal parameters only; every kappa remains
    # a positive mpmath number. No reverse rate is clipped or converted to float.
    for ev in np.geomspace(0.003, 0.3, 100):
        e = ctx.mpf(str(ev))
        k = ctx.exp(-1/e**2)
        q = ctx.matrix([[-1-e, 1, e], [1, -2+k, 1-k], [k, 1-e, -1+e-k]])
        pi = stationary(ctx, q)
        sigma = flux_entropy(ctx, q, pi)
        z = 3+e+2*k-e*e-e*k-k*k
        formula = (e-k)*(1-e-k)/z*(ctx.log(e)+ctx.log(1-e)-ctx.log(k)-ctx.log(1-k))
        residual = abs(sigma-formula)
        assert 0 < k < e < ctx.mpf("0.5")
        assert residual < ctx.mpf("1e-90")*max(1, abs(sigma))
        assert abs(sum(q[i, i] for i in range(3))+4) < ctx.mpf("1e-95")
        assert all(0 < q[i, j] <= 1 for i in range(3) for j in range(3) if i != j)
        rows.append({"epsilon": str(e), "log_kappa": str(ctx.log(k)),
                     "entropy": str(sigma), "asymptotic_entropy": str(1/(3*e)),
                     "generator_max_entry_error": str(e), "joint_row_TV_upper_bound": str(2*(e+k)),
                     "stationary_solve_vs_formula_residual": str(residual)})
    return {"precision_digits": 100, "seed": None, "root_100dps": str(root),
            "endpoint_models": endpoint_models, "three_state_points": rows,
            "numerical_tolerances": {"entropy_formula_relative": "1e-90", "stationary_residual": "1e-90"},
            "figure_scope": "Numerical curves illustrate analytic formulas and proved limits. The TV curve is a proved upper bound, not a numerical distance estimate."}


def inventory():
    scripts = []
    for path in sorted((ROOT / "analysis").rglob("*.py")):
        source = path.read_text(encoding="utf-8-sig")
        tree = ast.parse(source)
        scripts.append({"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path),
                        "syntax_valid": True, "description": ast.get_docstring(tree),
                        "freshly_replayed": path.name in REPLAYS})
    outputs = []
    for folder in (ROOT / "analysis", ROOT / "outputs"):
        for path in sorted(folder.glob("*.json")):
            value = json.loads(path.read_text(encoding="utf-8-sig"))
            outputs.append({"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path),
                            "top_level_keys": sorted(value) if isinstance(value, dict) else None,
                            "recorded_all_checks_passed": value.get("all_checks_passed") if isinstance(value, dict) else None})
    maps = []
    for path in sorted((ROOT / "knowledge").glob("source-*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        maps.append({"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path),
                     "nodes": len(data.get("nodes", [])), "edges": len(data.get("edges", []))})
    return {"analysis_scripts": scripts, "saved_scientific_outputs": outputs, "knowledge_shards": maps,
            "knowledge_merged_graph_present": (ROOT / "knowledge/graph.json").exists(),
            "knowledge_rendered_views_present": (ROOT / "knowledge/views").exists(),
            "formal_build_manifest_present": (ROOT / "formal/lake-manifest.json").exists(),
            "scope": "Inventory and syntax/JSON validation are coverage/provenance checks, not fresh independent proof verification. Discovery optimizations and infrastructure smoke examples are not manuscript evidence."}


def plot_network(ax, support, label, entropy):
    pos = {0: (-1.2, 1.05), 1: (1.2, 1.05), 2: (1.2, -0.6),
           3: (-1.2, -0.6), 4: (0, 0.02)}
    if [0, 2] in support:
        pos[2], pos[3] = pos[3], pos[2]
    names = [r"$x$", r"$y$", r"$h_1$", r"$h_2$", r"$h_3$"]
    for i, j in support:
        ax.add_patch(FancyArrowPatch(pos[i], pos[j], arrowstyle="<->", mutation_scale=9,
                                   shrinkA=12, shrinkB=12, lw=1.25,
                                   color="#B23A31" if (i, j) == (0, 1) else "#53616D"))
    for i in range(5):
        ax.add_patch(Circle(pos[i], 0.14, facecolor="white", edgecolor="#172A3A", lw=1.1, zorder=3))
        ax.text(*pos[i], names[i], ha="center", va="center", fontsize=10, zorder=4)
    ax.set(xlim=(-1.75, 1.75), ylim=(-1, 1.55), aspect="equal")
    ax.axis("off")
    ax.set_title(label, fontsize=10, loc="left", pad=5)
    ax.text(0, -0.96, r"$\sigma \simeq $" + entropy, ha="center", va="center", fontsize=10)


def figures(data):
    FIGURES.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.family": "DejaVu Serif", "font.size": 9,
                         "mathtext.fontset": "dejavuserif", "axes.spines.top": False,
                         "axes.spines.right": False, "pdf.fonttype": 42, "ps.fonttype": 42,
                         "svg.fonttype": "none", "savefig.facecolor": "white"})
    figure, ax = plt.subplots(1, 2, figsize=(7.1, 3.75))
    figure.subplots_adjust(left=0.045, right=0.975, top=0.9, bottom=0.30, wspace=0.16)
    endpoint = data["endpoint_models"]
    source_sigma = format(float(endpoint["source"]["entropy_100dps"]), ".13f")
    target_sigma = format(float(endpoint["target"]["entropy_100dps"]), ".13f")
    plot_network(ax[0], endpoint["source"]["support"], r"(a) $Q(z_*)$", source_sigma)
    plot_network(ax[1], endpoint["target"]["support"], r"(b) $Q_*$", target_sigma)
    strip = figure.add_axes([0.065, 0.055, 0.89, 0.175])
    strip.set(xlim=(0, 3), ylim=(0, 1))
    strip.axis("off")
    for i, (condition, value) in enumerate([
            (r"$0<z<z_*$", "Unbounded entropy"),
            (r"$z=z_*$", "Two entropy values"),
            (r"$z>z_*$", "Unique generator")]):
        strip.add_patch(Rectangle((i+0.015, 0.015), 0.97, 0.97, facecolor="#F1F4F5", edgecolor="#BEC8CF", lw=0.6))
        strip.text(i+0.5, 0.72, condition, ha="center", va="center", fontsize=10)
        strip.text(i+0.5, 0.30, value, ha="center", va="center", fontsize=10)
    for ext in ("pdf", "png", "svg"):
        figure.savefig(FIGURES / ("balanced-fiber." + ext), dpi=300, metadata={"Creator": "manuscript/scripts/reproduce.py"} if ext == "pdf" else None)
    plt.close(figure)

    rows = data["three_state_points"]
    ev = [float(x["epsilon"]) for x in rows]
    fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.85), layout="constrained")
    axes[0].loglog(ev, [float(x["entropy"]) for x in rows], color="#B23A31", lw=1.8,
                   label=r"$\sigma(Q_\varepsilon)$")
    axes[0].loglog(ev, [float(x["asymptotic_entropy"]) for x in rows], color="#172A3A", lw=1.1,
                   ls="--", label=r"$1/(3\varepsilon)$")
    axes[0].set(ylabel="Entropy-production rate", title="(a) Entropy diverges")
    axes[1].loglog(ev, [float(x["generator_max_entry_error"]) for x in rows], color="#172A3A", lw=1.8,
                   label=r"$\|Q_\varepsilon-Q_0\|_{\max}=\varepsilon$")
    axes[1].loglog(ev, [float(x["joint_row_TV_upper_bound"]) for x in rows], color="#26768B", lw=1.4,
                   ls="--", label=r"$d_{\rm TV}\leq 2(\varepsilon+\kappa)$")
    axes[1].set(ylabel="Generator error / row-TV upper bound", title="(b) Observable convergence")
    for ax in axes:
        ax.set_xlabel(r"$\varepsilon$  (fixed rate units)")
        ax.invert_xaxis()
        ax.legend(frameon=False, fontsize=8, loc="best")
        ax.grid(which="major", color="#DCE1E4", lw=0.5)
    for ext in ("pdf", "png", "svg"):
        fig.savefig(FIGURES / ("three-state-instability." + ext), dpi=300, metadata={"Creator": "manuscript/scripts/reproduce.py"} if ext == "pdf" else None)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--figures-only", action="store_true")
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError("Assertions must remain enabled; do not use Python -O")
    os.chdir(ROOT)
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(ROOT / "analysis"))
    if args.figures_only:
        saved = json.loads(OUT.read_text(encoding="utf-8"))
        figures(saved["figure_data"])
        print("Redrew two figures from saved checked numerical data.")
        return
    protected = sorted((ROOT / "analysis").glob("*.json")) + sorted((ROOT / "outputs").glob("*.json"))
    before = {p.relative_to(ROOT).as_posix(): sha(p) for p in protected}
    replays = []
    for name in REPLAYS:
        print("Replaying " + name, flush=True)
        replays.append(replay(name))
    print("Checking the independent cone-to-path reconstruction", flush=True)
    cone = embedded_cone_check()
    three = independent_three_state()
    endpoint = next(x["captured_result"] for x in replays if x["script"].endswith("check_balanced_fold.py"))
    figure_data = quantitative_data(endpoint)
    result = {"executed_at_utc": datetime.now(timezone.utc).isoformat(),
              "command_from_root": ".venv/Scripts/python.exe -B manuscript/scripts/reproduce.py",
              "environment": {"python": platform.python_version(), "platform": platform.platform(),
                              "sympy": sp.__version__, "mpmath": mp.__version__, "numpy": np.__version__,
                              "scipy": scipy.__version__, "matplotlib": matplotlib.__version__},
              "reproduction_script_sha256": sha(__file__), "random_seed": None,
              "method": "Deterministic historical-script replays with Path.write_text intercepted; exact independent cone/path and three-state checks; high-precision direct stationary solves for figure data",
              "replays": replays, "independent_cone_path_check": cone,
              "independent_three_state_check": three, "figure_data": figure_data,
              "coverage_inventory": inventory(), "historical_output_hashes": before,
              "mathematical_status": "Exact supporting calculations and numerical cross-checks; universal theorems rely on conventional proofs. No formal-verification or novelty certificate.",
              "all_checks_passed": True}
    after = {p.relative_to(ROOT).as_posix(): sha(p) for p in protected}
    assert before == after, "A historical output changed during reproduction"
    result["historical_outputs_unchanged"] = True
    figures(figure_data)
    result["figure_sha256"] = {p.relative_to(ROOT).as_posix(): sha(p) for p in sorted(FIGURES.glob("*")) if p.suffix in (".pdf", ".png", ".svg")}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(json.dumps({"all_checks_passed": True, "replayed_scripts": len(replays),
                      "historical_outputs_unchanged": True,
                      "changed_payloads": [x["script"] for x in replays if x["changed_scientific_paths"]],
                      "output": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
