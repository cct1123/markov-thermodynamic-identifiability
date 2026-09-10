"""Layered capability checks only; never a scientific discovery or evidence ID.

Run from repository root: python -m analysis.capabilities.smoke [--require-z3]
"""

import argparse
import importlib.util
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm
import sympy as sp

from analysis.capabilities.counterexample_demo import run as counterexample
from analysis.research_tools.ctmc import entropy_production, stationary, stationary_exact, stationary_mp
from analysis.research_tools.graphs import connected_supports, observation_subsets
from analysis.research_tools.provenance import write_manifest


def check_smt(output, required):
    if importlib.util.find_spec("z3") is None:
        if required:
            raise RuntimeError("install analysis/requirements-smt.txt for --require-z3")
        return {"status": "skipped: optional z3-solver not installed"}, []
    import z3
    x, y = z3.Reals("x y")
    solver = z3.SolverFor("QF_NRA")
    solver.set(timeout=5000, random_seed=20260910)
    solver.add(x > 0, y > 0, x+y == 1, x*y > z3.RealVal("1/8"))
    smt_path = output / "existence.smt2"
    smt_path.write_text(solver.to_smt2(), encoding="utf-8")
    sat = solver.check()
    if sat != z3.sat:
        raise AssertionError(f"toy existence expected sat, got {sat}")
    witness = {str(v): str(solver.model().eval(v)) for v in (x, y)}
    # Independent rational substitution for this rational model.
    rx, ry = [sp.Rational(str(solver.model().eval(v))) for v in (x, y)]
    assert rx > 0 and ry > 0 and rx+ry == 1 and rx*ry > sp.Rational(1, 8)
    solver.reset()
    solver.add(x*x < 0)
    unsat_path = output / "impossible.smt2"
    unsat_path.write_text(solver.to_smt2(), encoding="utf-8")
    unsat = solver.check()
    assert unsat == z3.unsat
    # Exercise the unknown path deterministically with a resource bound.
    limited = z3.SolverFor("QF_NRA")
    limited.set(rlimit=1)
    limited.add(x*x == 2, x > 0)
    unknown = limited.check()
    assert unknown == z3.unknown
    qe = z3.Tactic("qe")(z3.Exists(x, x > y))
    assert z3.is_true(z3.simplify(qe.as_expr()))
    return {"status": "solver-checked (trusted Z3, no formal proof)",
            "sat": str(sat), "rational_model": witness, "unsat": str(unsat),
            "unknown": str(unknown), "reason_unknown": limited.reason_unknown(),
            "linear_qe": str(qe), "timeout_ms": 5000, "seed": 20260910,
            "unknown_rlimit": 1}, [smt_path, unsat_path]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="analysis/capabilities/results")
    parser.add_argument("--require-z3", action="store_true")
    args = parser.parse_args()
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    # A generic toy asymmetric two-state chain, with exact hand solution 3/5,2/5.
    q = sp.Matrix([[-2, 2], [3, -3]])
    pi, diagnostics = stationary(q)
    exact = stationary_exact(q)
    assert exact == sp.Matrix([sp.Rational(3, 5), sp.Rational(2, 5)])
    np.testing.assert_allclose(pi, [0.6, 0.4], rtol=0, atol=1e-14)
    precisions = []
    for dps in (50, 100):
        ctx, high, info = stationary_mp(q, dps=dps)
        assert abs(high[0] - ctx.mpf(3)/5) < ctx.power(10, -dps+5)
        info["pi"] = [str(v) for v in high]
        precisions.append(info)
    assert abs(entropy_production(q)) < 1e-25
    a, b, s, t = sp.symbols("a b s t", positive=True)
    symbolic = stationary_exact(sp.Matrix([[-a, a], [b, -b]]))
    assert symbolic == sp.Matrix([b/(a+b), a/(a+b)])
    eigenvalues = np.linalg.eigvals(np.array(q, dtype=float))
    np.testing.assert_allclose(sorted(eigenvalues), [-5, 0], atol=1e-14)
    # charpoly may replace an assumed symbol with a fresh polynomial generator.
    assert q.charpoly().all_coeffs() == [1, 5, 0]
    # Numerical quadrature independently checks the resolvent at s=1.
    resolvent = (s*sp.eye(2)-q).inv().applyfunc(sp.cancel)
    laplace, error = quad(lambda time: np.exp(-time)*expm(np.array(q, float)*time)[0, 0], 0, np.inf)
    assert abs(laplace-float(resolvent[0, 0].subs(s, 1))) < 1e-11
    assert sp.simplify(sp.laplace_transform(sp.exp(-2*t), t, s, noconds=True)-1/(s+2)) == 0
    assert sp.limit(s*resolvent[0, 0], s, 0, dir="+") == sp.Rational(3, 5)
    x, y = sp.symbols("x y")
    basis = sp.groebner([x-y, x*x-2], x, y, order="lex")
    eliminated = [p.as_expr() for p in basis.polys if not p.as_expr().has(x)]
    assert eliminated == [y*y-2]
    assert sp.resultant(x-y, x*x-2, x) == y*y-2
    assert sp.cancel((x*x-1)/(x-1)) == x+1  # retain original exclusion x != 1
    assert sp.series(sp.log(1+x), x, 0, 3).removeO() == x-x*x/2
    assert sp.reduce_inequalities([x*x < 1, x > 0], x).as_set() == sp.Interval.open(0, 1)
    counts = {str(n): len(list(connected_supports(n))) for n in range(1, 7)}
    assert list(counts.values()) == [1, 1, 2, 6, 21, 112]
    graphs4 = list(connected_supports(4))
    assert all(not nx.is_isomorphic(g, h) for i, g in enumerate(graphs4) for h in graphs4[i+1:])
    square = nx.cycle_graph(4)
    cycles = nx.cycle_basis(square)
    assert len(cycles) == square.number_of_edges()-len(square)+nx.number_connected_components(square) == 1
    assert len(list(observation_subsets(square, 2))) == 2
    assert len(list(observation_subsets(square, 2, quotient=False))) == 6
    assert square.to_directed().number_of_edges() == 8
    # Parameter sweep uses ordinary arrays; no continuation framework required.
    rates = np.geomspace(0.01, 100, 25)
    probabilities = [stationary([[-rate, rate], [3, -3]])[0][0] for rate in rates]
    np.testing.assert_allclose(probabilities, 3/(rates+3), atol=1e-14)
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.semilogx(rates, probabilities, marker=".")
    ax.set(xlabel="Toy forward rate (inverse time)", ylabel="Stationary probability", title="Capability test: parameter sweep")
    fig.tight_layout()
    plot = output / "sweep.png"
    fig.savefig(plot, dpi=130)
    plt.close(fig)
    smt, smt_artifacts = check_smt(output, args.require_z3)
    results = {"ctmc": {"pi": pi.tolist(), "exact_pi": list(map(str, exact)),
                         "diagnostics": diagnostics, "high_precision": precisions,
                         "symbolic_pi": str(symbolic), "eigenvalues": eigenvalues.tolist()},
               "algebra": {"groebner_elimination": list(map(str, eliminated)), "resultant": str(y*y-2),
                           "resolvent": str(resolvent), "quadrature": laplace, "quadrature_error_estimate": error,
                           "checks": ["factor", "characteristic polynomial", "Laplace", "limit", "series", "inequality"]},
               "graphs": {"connected_counts": counts, "square_cycle_basis": cycles,
                          "square_two_edge_observation_orbits": 2},
               "counterexample": counterexample(), "constraints": smt,
               "formal": "not run; Lean is optional", "status": "all requested capability checks passed"}
    sources = [Path(__file__), "analysis/capabilities/counterexample_demo.py",
               *Path("analysis/research_tools").glob("*.py"),
               *Path("analysis").glob("requirements*.txt")]
    write_manifest(output / "smoke.json", sources=sources, artifacts=[plot, *smt_artifacts],
                   settings={"command": "python -m analysis.capabilities.smoke" + (" --require-z3" if args.require_z3 else ""),
                             "seed": 20260910, "dps": [50, 100], "rtol": 1e-12,
                             "toy_generator": [[-2, 2], [3, -3]], "graph_scope": "connected simple undirected n<=6",
                             "require_z3": args.require_z3}, results=results, kind="capability-test")
    print(results["status"])
    print(output / "smoke.json")


if __name__ == "__main__":
    main()
