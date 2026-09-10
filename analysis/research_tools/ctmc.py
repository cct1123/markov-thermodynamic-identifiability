"""Row-generator CTMC checks, stationary laws and stationary edge entropy.

Rates have inverse-time units; entropy uses natural logs and k_B = 1.
Numerical residuals and arbitrary precision are diagnostics, not certificates.
No rate clipping, connectivity threshold, or stationary-law clipping is used.
"""

import warnings

import mpmath as mp
import networkx as nx
import numpy as np
import sympy as sp


def validate_generator(q, *, rtol=1e-12, irreducible=True, bidirected=False):
    """Validate finite, nonnegative off-diagonals and relative row sums.

    Strictly positive entries define support, including arbitrarily small rates.
    The returned matrix is a copy; no repair of invalid inputs is performed.
    """
    original = np.array(q, dtype=object, copy=True)
    if any(np.iscomplexobj(value) for value in original.flat):
        raise ValueError("generator entries must be finite real rates")
    try:
        q = np.array(original, dtype=float, copy=True)
    except (TypeError, OverflowError) as error:
        raise ValueError("generator entries must be finite real rates") from error
    if q.ndim != 2 or q.shape[0] != q.shape[1] or not len(q):
        raise ValueError("generator must be a nonempty square matrix")
    if not np.isfinite(q).all() or not np.isfinite(rtol) or rtol <= 0:
        raise ValueError("finite entries and a positive finite rtol are required")
    # Detect lost support before a rounded matrix can turn a finite entropy into
    # infinity, or remove a tiny edge while leaving the graph connected.
    if any(value == 0 and sp.sympify(source).is_zero is False
           for source, value in zip(original.flat, q.flat)):
        raise ArithmeticError("nonzero rate underflowed during float conversion; use exact/high precision")
    off = q.copy()
    np.fill_diagonal(off, 0)
    if np.any(off < 0) or np.any(np.diag(q) > 0):
        raise ValueError("negative off-diagonal or positive diagonal")
    scales = np.max(np.abs(q), axis=1)
    scaled = q / np.where(scales > 0, scales, 1)[:, None]
    if np.any(np.abs(scaled.sum(axis=1)) > rtol * np.abs(scaled).sum(axis=1)):
        raise ValueError("rows do not sum to zero at the requested relative tolerance")
    support = off > 0
    if bidirected and not np.array_equal(support, support.T):
        raise ValueError("support is not bidirected")
    if irreducible and not nx.is_strongly_connected(nx.from_numpy_array(support, create_using=nx.DiGraph)):
        raise ValueError("generator is reducible; stationary uniqueness is not assumed")
    return q


def stationary(q, *, rtol=1e-12):
    """Return (pi, diagnostics) using a time-rescaled linear solve."""
    q = validate_generator(q, rtol=rtol)
    scale = float(np.max(np.abs(q))) or 1.0
    a = (q / scale).T.copy()
    a[-1] = 1
    b = np.zeros(len(q))
    b[-1] = 1
    condition = float(np.linalg.cond(a))
    if condition * np.finfo(float).eps > rtol:
        warnings.warn("stationary solve is ill-conditioned; recompute from exact inputs at higher precision", RuntimeWarning)
    pi = np.linalg.solve(a, b)
    residual = float(np.max(np.abs(pi @ (q / scale))))
    normalization = float(abs(pi.sum() - 1))
    if not np.isfinite(pi).all() or np.any(pi <= 0) or residual > rtol or normalization > rtol:
        raise ArithmeticError("stationary solve failed positivity, normalization or residual check")
    return pi, {"scaled_residual_inf": residual, "normalization_error": normalization,
                "condition_number": condition, "rate_scale": scale, "rtol": rtol}


def edge_flows(q, pi=None, *, rtol=1e-12):
    """Return off-diagonal stationary fluxes and antisymmetric currents."""
    q = validate_generator(q, rtol=rtol)
    if pi is None:
        pi = stationary(q, rtol=rtol)[0]
    else:
        original = np.asarray(pi, dtype=object)
        if any(np.iscomplexobj(value) for value in original.flat):
            raise ValueError("pi must contain finite real probabilities")
        try:
            pi = np.array(original, dtype=float)
        except (TypeError, OverflowError) as error:
            raise ValueError("pi must contain finite real probabilities") from error
    if pi.shape != (len(q),) or not np.isfinite(pi).all() or np.any(pi <= 0):
        raise ValueError("pi must be a strictly positive finite probability vector")
    scale = float(np.max(np.abs(q))) or 1.0
    if abs(pi.sum() - 1) > rtol or np.max(np.abs(pi @ (q / scale))) > rtol:
        raise ValueError("pi is not normalized and stationary at the requested tolerance")
    off = q.copy()
    np.fill_diagonal(off, 0)
    with np.errstate(over="raise", invalid="raise"):
        flux = pi[:, None] * off
    if np.any((off > 0) & (flux == 0)):
        raise ArithmeticError("positive flux underflowed; use arbitrary precision")
    return flux, flux - flux.T


def entropy_production(q, pi=None, *, rtol=1e-12):
    """Sum unordered edge (f-r) log(f/r); one-way positive flux gives +inf.

    Absent pairs contribute zero. Missing reverse edges are never regularized.
    Near equilibrium, independently recompute differences at higher precision.
    """
    flux, current = edge_flows(q, pi, rtol=rtol)
    total = 0.0
    for i in range(len(flux)):
        for j in range(i + 1, len(flux)):
            f, r = flux[i, j], flux[j, i]
            if f == r == 0:
                continue
            if min(f, r) == 0:
                return float("inf")
            affinity = (np.log1p((f - r) / r) if abs(f - r) < 0.5 * r
                        else np.log(f) - np.log(r))
            total += current[i, j] * affinity
    if not np.isfinite(total):
        raise ArithmeticError("finite-support entropy overflowed; use arbitrary precision")
    return float(total)


def _exact_matrix(q):
    q = sp.Matrix(q)
    if q.rows == 0 or q.rows != q.cols or q.atoms(sp.Float):
        raise ValueError("supply a nonempty square exact matrix (Rational, integers or symbols), no floats")
    if any(sp.simplify(sum(q.row(i))) != 0 for i in range(q.rows)):
        raise ValueError("row sums must vanish identically")
    return q


def stationary_exact(q):
    """Normalized exact null vector; parameter results are generic unless stratified.

    This is algebra, not a positivity/irreducibility certificate. Record parameter
    assumptions and rank-changing or denominator-zero strata separately.
    """
    q = _exact_matrix(q)
    basis = q.T.nullspace()
    if len(basis) != 1 or sp.simplify(sum(basis[0])) == 0:
        raise ValueError("no unique normalized null vector")
    return (basis[0] / sum(basis[0])).applyfunc(sp.factor)


def stationary_mp(q, *, dps=80):
    """Solve independently with mpmath from exact rational numeric input.

    Returns a cloned context, its pi matrix, and residual diagnostics, so later
    arithmetic can retain precision. Floats are rejected, not reinterpreted.
    """
    q = _exact_matrix(q)
    if not isinstance(dps, int) or dps < 30 or not all(x.is_Rational for x in q):
        raise ValueError("dps >= 30 and exact rational numeric entries required")
    support = nx.DiGraph()
    support.add_nodes_from(range(q.rows))
    for i in range(q.rows):
        for j in range(q.cols):
            if i != j:
                if q[i, j] < 0:
                    raise ValueError("negative off-diagonal")
                if q[i, j] > 0:
                    support.add_edge(i, j)
    if not nx.is_strongly_connected(support):
        raise ValueError("generator is reducible")
    ctx = mp.mp.clone()
    ctx.dps = dps
    a = ctx.matrix([[ctx.mpf(int(x.p)) / int(x.q) for x in q.row(i)] for i in range(q.rows)])
    scale = max(abs(x) for x in a) or ctx.mpf(1)
    scaled = a / scale
    system = scaled.T.copy()
    for j in range(q.cols):
        system[q.rows - 1, j] = 1
    rhs = ctx.matrix([0] * (q.rows - 1) + [1])
    pi = ctx.lu_solve(system, rhs)
    residual = max(abs(x) for x in pi.T * scaled)
    normalization = abs(sum(pi) - 1)
    tolerance = ctx.power(10, -dps + 10)
    if min(pi) <= 0 or residual > tolerance or normalization > tolerance:
        raise ArithmeticError("high-precision stationarity check failed; increase dps")
    return ctx, pi, {"dps": dps, "scaled_residual_inf": str(residual),
                     "normalization_error": str(normalization)}
