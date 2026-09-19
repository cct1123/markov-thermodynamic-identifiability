"""Fresh bounded check of supplied review calculations; never writes accepted outputs.

Run from root: .venv/Scripts/python.exe -B analysis/correctness/verify_review_calculations.py
Exact definitions are transcribed from the cited manuscript/audits. Historical
checkers and accepted JSON results are neither imported nor executed. No RNG.
High-precision endpoint checks are not new interval certificates.
"""
if not __debug__:
    raise SystemExit('Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.')

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp
import sympy as s
from sympy.polys.matrices import DomainMatrix


OUT = Path('outputs/supplied-verification-2026-09-19/calculations.json')
SUPPLIED = Path('evidence/supplied/2026-09-18/independent_checks.json')
INPUTS = [SUPPLIED, Path('evidence/supplied/2026-09-19/second-academic-review.txt'),
          Path('manuscript/main.tex'), Path('manuscript/supplementary/proofs.tex'),
          Path('manuscript/supplementary/conditioning.tex'),
          Path('analysis/balanced-cone-bound.md'),
          Path('analysis/three-state-fixed-trace-audit.md'),
          Path('analysis/check_balanced_fold.py'), Path('analysis/derive_balanced_path.py'),
          Path('analysis/manuscript-math-independent-check.py')]


def exact_checks(supplied):
    z, t, eps, kap = s.symbols('z t eps kap', real=True)
    p = 352*z**4 - 3168*z**3 - 4644*z**2 - 11340*z - 7623
    x = s.Matrix([[2, 0, 8], [0, 7, 11]])
    y = s.Matrix([[3, 0], [0, 6], [z, z]])
    h = s.Matrix([[-7, 4, 0], [5, -11, 0], [0, 0, -2*z]])
    minors = [y.row_join(h*y[:, 0]).det(), y.row_join(h*y[:, 1]).det(),
              x.col_join((x*h)[1, :]).det()]
    assert all(s.expand(got-s.sympify(want, locals={'z': z})) == 0
               for got, want in zip(minors, supplied['minors']))
    assert s.gcd(minors[0], minors[1]) == 9*z
    assert s.Poly(minors[2], z).all_coeffs() == [-308, -266]

    rho = s.sqrt(6)
    a0, b0, m = z, 5*z/(4*(rho-1)), (7+2*rho)/5
    ell, right = (3-rho/2)/8, 35*rho/88
    k = (2*z-9+2*rho)/(4*rho)
    a = k-1
    j = a*m+k
    f0 = a0*right*m/ell-b0*j**2
    f1 = a0*(right/ell+k-a*m)+ell*j**2+right*j-2*b0*j*a
    f2 = a*(ell*j+right-a0*(1+ell*k/right)-b0*a)
    cone_discriminant = s.simplify(f1**2-4*f0*f2)
    cone_factor = -(s.Rational(11, 1200)+11*rho/4200)*(z+s.Rational(19, 22))**2/352
    assert s.simplify(cone_discriminant-cone_factor*p) == 0

    aa = 100*z**4-840*z**3+3741*z**2-6867*z+3978
    bb = -408*z**4-2916*z**3+8766*z**2+3105*z-12474
    cc = 2412*z**4-5724*z**3+891*z**2+3402*z
    path_disc = s.factor(s.discriminant(aa*t**2+bb*t+cc, t))
    assert s.expand(path_disc+567*(z-2)**2*(2*z-3)**2*p) == 0
    assert s.Poly(p, z).count_roots(0, s.oo) == 1
    assert s.Poly(p, z).count_roots(-s.oo, 0) == 1
    assert p.subs(z, s.Rational(1055, 100)) < 0 < p.subs(z, s.Rational(1056, 100))

    q3 = s.Matrix([[-1-eps, 1, eps], [1, -2+kap, 1-kap],
                   [kap, 1-eps, -1+eps-kap]])
    weights = [s.expand((-q3).minor_submatrix(i, i).det()) for i in range(3)]
    assert all(s.expand(got-s.sympify(want, locals={'eps': eps, 'kap': kap})) == 0
               for got, want in zip(weights, supplied['three_state_weights']))
    total = s.factor(sum(weights))
    pi = s.Matrix([weights])/total
    assert all(s.cancel(v) == 0 for v in pi*q3)
    assert s.cancel(sum(pi)-1) == 0
    assert q3*s.ones(3, 1) == s.zeros(3, 1) and s.trace(q3) == -4
    current = (eps-kap)*(1-eps-kap)/total
    cycle = [(0, 2), (2, 1), (1, 0)]
    currents = [s.factor(pi[i]*q3[i, j]-pi[j]*q3[j, i]) for i, j in cycle]
    assert all(s.cancel(value-current) == 0 for value in currents)
    affinity_argument = s.cancel(s.prod(pi[i]*q3[i, j]/(pi[j]*q3[j, i]) for i, j in cycle))
    assert s.cancel(affinity_argument-eps*(1-eps)/(kap*(1-kap))) == 0
    ratio = s.Symbol('R', real=True)
    l1, l3, li, lj, hidden_rate, baseline, amplitude = s.symbols('lambda1 lambda3 lambda_i lambda_j h u v', positive=True)
    inverse_h = (l3-ratio*l1)/(ratio-1)
    derivative = s.diff(inverse_h, ratio).subs(ratio, (l3+hidden_rate)/(l1+hidden_rate))
    derivative_expected = -(l1+hidden_rate)**2/(l3-l1)
    assert s.cancel(derivative-derivative_expected) == 0
    g = lambda point: baseline+amplitude/(point+hidden_rate)
    difference_expected = amplitude*(lj-li)/((li+hidden_rate)*(lj+hidden_rate))
    assert s.cancel(g(li)-g(lj)-difference_expected) == 0
    return z, p, aa, bb, cc, {
        'minors': list(map(lambda v: str(s.factor(v)), minors)),
        'minors_match_supplied': True,
        'first_two_common_root': 'z=0 only; excluded by z>0',
        'third_minor_strictly_negative_for_positive_z': True,
        'cone_discriminant_identity': True, 'cone_multiplier_of_P': str(cone_factor),
        'path_discriminant_identity': True, 'path_discriminant': str(path_disc),
        'unique_positive_quartic_root_exact': True,
        'three_state_weights': list(map(str, weights)),
        'three_state_weights_match_supplied': True,
        'three_state_stationarity_exact': True, 'three_state_trace': '-4',
        'three_state_normalizer': str(total), 'three_state_cycle_currents': list(map(str, currents)),
        'three_state_affinity_argument': str(affinity_argument),
        'three_state_domain': '0 < kap < eps < 1/2; all offdiagonal rates strictly positive, weights and normalizer positive',
        'scalar_conditioning_inverse_derivative': str(derivative_expected),
        'scalar_conditioning_transform_difference': str(difference_expected),
        'both_scalar_conditioning_identities_exact': True,
        'scalar_conditioning_domain': 'positive Laplace arguments and h; lambda3 != lambda1, hence R != 1 for the inverse formula',
        'scope': 'Exact algebraic identities; these alone do not prove global support exhaustion or endpoint uniqueness.'}


def exact_endpoint(z, p, aa, bb, cc):
    # Algebraic reduction prevents numerical near-zero entries from being used
    # as positive rates in entropy. This shares the historical field formulation.
    root = s.CRootOf(p, 1)
    field = s.QQ.algebraic_field(root)
    zz = field.from_sympy(root)
    def dm(rows):
        return DomainMatrix([[field.convert(v) for v in row] for row in rows],
                            (len(rows), len(rows[0])), field)
    def val(expr): return field.from_sympy(expr.subs(z, root))
    q = dm([[-11, 1, 2, 0, 8], [2, -20, 0, 7, 11], [3, 0, -7, 4, 0],
            [0, 6, 5, -11, 0], [zz, zz, 0, 0, -2*zz]])
    c = dm([[3, 0, 1], [0, 6, 1], [zz, zz, 1]])
    h = dm([[-7, 4, 0], [5, -11, 0], [0, 0, -2*zz]])
    d = (c.inv()*h*c).to_list()
    assert val(bb)**2-4*val(aa)*val(cc) == field.zero
    u = -val(bb)/(2*val(aa))
    a1, a2, b1, b2, c1, c2 = d[1][1], d[1][0], d[0][1], d[0][0], d[2][1], d[2][0]
    v = -u*(a2*u+c2)/(u*u+a1*u+c1)
    px, py, qx, qy = (42+11*zz)/18, 11*zz/18, 8*zz/10, (6+8*zz)/10
    s1, s2 = (px-u)/py, (qy-v)/qx
    apex_a, apex_b = (u+s1*v)/(1-s1*s2), (v+s2*u)/(1-s1*s2)
    cp = dm([[0, u, 1], [v, 0, 1], [apex_b, apex_a, 1]])
    hidden = c*cp.inv()
    sr = [[int(i == j) for j in range(5)] for i in range(5)]
    for i, row in enumerate(hidden.to_list()): sr[i+2][2:] = row
    similarity = dm(sr)
    target = similarity.inv()*q*similarity
    assert similarity*dm([[1]]*5) == dm([[1]]*5)
    assert target*dm([[1]]*5) == dm([[0]]*5)
    reset, exits = dm([[0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]), dm([[1, 0], [0, 2], [0, 0], [0, 0], [0, 0]])
    assert reset*similarity == reset and similarity*exits == exits
    marked = dm([[0, 1, 0, 0, 0], [2, 0, 0, 0, 0], [0]*5, [0]*5, [0]*5])
    assert marked*similarity == similarity*marked
    support = []
    rows = target.to_list()
    for i in range(5):
        for j in range(i+1, 5):
            assert (rows[i][j] == field.zero) == (rows[j][i] == field.zero)
            if rows[i][j] != field.zero: support.append([i, j])
    assert support == [[0, 1], [0, 3], [0, 4], [1, 2], [1, 4], [2, 3], [3, 4]]
    # Exact similarity supplies all-time kernel equality, not a finite grid.
    return q, target, similarity, support


def numerical_endpoint(dps, source, target, similarity, supplied):
    ctx = mp.mp.clone()
    ctx.dps = dps
    pp = lambda z: 352*z**4-3168*z**3-4644*z**2-11340*z-7623
    root = ctx.findroot(pp, (ctx.mpf('10.5'), ctx.mpf('10.6')))
    def encode(value): return ctx.nstr(value, dps)
    def matrix_encode(matrix): return [[encode(matrix[i, j]) for j in range(matrix.cols)] for i in range(matrix.rows)]
    def evaluate(value):
        result = ctx.mpf(0)
        for coefficient in value.to_list():
            result = result*root + ctx.mpf(int(coefficient.numerator))/int(coefficient.denominator)
        return result
    def numeric(matrix): return ctx.matrix([[evaluate(v) for v in row] for row in matrix.to_list()])
    def norm(matrix): return max(abs(v) for v in matrix)
    qs, qt, sim = map(numeric, [source, target, similarity])
    # Direct floating matrix conjugation is a second route to target entries.
    direct_target = sim**-1*qs*sim
    matrix_residual = norm(direct_target-qt)
    stationary, entropies, directed_entropies, stationary_residuals, cofactor_residuals = [], [], [], [], []
    positivity = []
    for exact, q in ((source, qs), (target, qt)):
        lhs, rhs = q.T.copy(), ctx.matrix([0, 0, 0, 0, 1])
        for j in range(5): lhs[4, j] = 1
        pi = ctx.lu_solve(lhs, rhs)
        stationary.append(pi)
        stationary_residuals.append(max(norm(pi.T*q), abs(sum(pi)-1)))
        weights = [ctx.det(ctx.matrix([[-q[i, j] for j in range(5) if j != k]
                                      for i in range(5) if i != k])) for k in range(5)]
        cofactor_pi = ctx.matrix(weights)/sum(weights)
        cofactor_residuals.append(norm(cofactor_pi-pi))
        exact_rows = exact.to_list()
        edges = [(i, j) for i in range(5) for j in range(i+1, 5) if exact_rows[i][j] != exact.domain.zero]
        assert all(pi[i] > 0 for i in range(5))
        assert all(q[i, j] > 0 and q[j, i] > 0 for i, j in edges)
        positivity.append(min([pi[i] for i in range(5)] + [q[a, b] for i, j in edges for a, b in ((i, j), (j, i))]))
        sigma = ctx.mpf(0)
        for i, j in edges:
            f, r = pi[i]*q[i, j], pi[j]*q[j, i]
            sigma += (f-r)*ctx.log(f/r)
        direct_sigma = sum((pi[i]*q[i, j]-pi[j]*q[j, i])*ctx.log(q[i, j]/q[j, i]) for i, j in edges)
        entropies.append(sigma)
        directed_entropies.append(direct_sigma)
    reset, exits = ctx.matrix([[0, 1, 0, 0, 0], [1, 0, 0, 0, 0]]), ctx.matrix([[1, 0], [0, 2], [0, 0], [0, 0], [0, 0]])
    killed = [q.copy() for q in [qs, qt]]
    for q in killed: q[0, 1] = 0; q[1, 0] = 0
    grid = [ctx.mpf(1)/10, ctx.mpf(1), ctx.mpf(2), ctx.mpf(3), ctx.mpf(10), ctx.mpf(100)]
    residuals = [norm(reset*(lam*ctx.eye(5)-killed[0])**-1*exits-reset*(lam*ctx.eye(5)-killed[1])**-1*exits) for lam in grid]
    observed = {'z_star': root, 'sigma_source': entropies[0], 'sigma_target': entropies[1],
                'delta_sigma': entropies[1]-entropies[0]}
    differences = {key: abs(value-ctx.mpf(supplied['endpoint_high_precision'][key])) for key, value in observed.items()}
    assert all(value < ctx.mpf('1e-64') for value in differences.values())
    tolerance = ctx.power(10, -dps+12)
    checked_residuals = stationary_residuals+cofactor_residuals+residuals+[matrix_residual]
    checked_residuals += [abs(a-b) for a, b in zip(entropies, directed_entropies)]
    assert all(value < tolerance for value in checked_residuals)
    assert abs(pp(root)) < ctx.power(10, -dps+8)
    return {
        'precision_digits': dps, **{key: encode(value) for key, value in observed.items()},
        'relative_entropy_separation_percent': encode(100*(entropies[1]-entropies[0])/entropies[0]),
        'absolute_differences_from_supplied_decimals': {key: encode(value) for key, value in differences.items()},
        'comparison_tolerance_supplied_decimal_values': '1e-64',
        'root_polynomial_residual': encode(abs(pp(root))),
        'source_generator': matrix_encode(qs), 'target_generator': matrix_encode(qt),
        'source_stationary_law': matrix_encode(stationary[0]), 'target_stationary_law': matrix_encode(stationary[1]),
        'stationary_equation_and_normalization_residuals': list(map(encode, stationary_residuals)),
        'stationary_cofactor_vs_lu_residuals': list(map(encode, cofactor_residuals)),
        'pair_flux_vs_directed_rate_entropy_residuals': [encode(abs(a-b)) for a, b in zip(entropies, directed_entropies)],
        'smallest_checked_stationary_mass_or_supported_rate': list(map(encode, positivity)),
        'numerical_conjugation_vs_exact_field_evaluation_residual': encode(matrix_residual),
        'fresh_resolvent_argument_grid': list(map(encode, grid)),
        'fresh_resolvent_grid_residuals': list(map(encode, residuals)),
        'fresh_max_resolvent_discrepancy': encode(max(residuals)),
        'residual_acceptance_threshold': encode(tolerance),
        'limitation': 'Arbitrary precision numerical cross-check, not a new rigorous interval or global support certificate.'}


def main():
    supplied = json.loads(SUPPLIED.read_text(encoding='utf-8'))
    z, p, aa, bb, cc, symbolic = exact_checks(supplied)
    print('Exact minors, discriminants, weights, stationarity, and current identities passed.', flush=True)
    source, target, similarity, support = exact_endpoint(z, p, aa, bb, cc)
    print('Exact endpoint conjugation, support zeros, normalization, and kernel-invariance identities passed.', flush=True)
    calculations = [numerical_endpoint(dps, source, target, similarity, supplied) for dps in (80, 120)]
    ctx = mp.mp.clone(); ctx.dps = 130
    cross_precision = {key: str(abs(ctx.mpf(calculations[0][key])-ctx.mpf(calculations[1][key])))
                       for key in ('z_star', 'sigma_source', 'sigma_target', 'delta_sigma')}
    assert all(ctx.mpf(value) < ctx.mpf('1e-76') for value in cross_precision.values())
    output = {
        'kind': 'reproduced exact identities and high-precision numerical checks of supplied review',
        'executed_at_utc': datetime.now(timezone.utc).isoformat(),
        'command': '.venv/Scripts/python.exe -B analysis/correctness/verify_review_calculations.py',
        'environment': {'python': platform.python_version(), 'sympy': s.__version__,
                        'mpmath': mp.__version__, 'platform': platform.platform()},
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256': {p.as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in INPUTS},
        'input_and_method_provenance': 'Definitions transcribed from current manuscript and named local audits/checkers. No historical checker imports or execution, and no historical accepted JSON values used as inputs. Supplied decimals used only for post-calculation comparison. No random input, optimizer or topology search.',
        'independence_limits': 'Exact endpoint algebra shares the Q[z*] field/conjugation formulation of check_balanced_fold.py and displayed definitions; it is not independent evidence for those definitions. Fresh LU stationary solves are checked against cofactors at each precision. Pair-flux entropy is checked against the stationary directed-rate expression. Symbolic discriminants share the displayed polynomials.',
        'symbolic_checks': symbolic,
        'exact_endpoint_checks': {'row_normalization': True, 'reciprocal_support_zeros': True,
                                  'support_pairs_zero_based': support,
                                  'marked_matrix_commutation_and_reset_exit_invariance': True,
                                  'meaning': 'Algebraic similarity proves all-time marked-kernel equality for this candidate when physical; numerical positivity is checked below. No enumeration of all physical realizations.'},
        'endpoint_calculations': calculations,
        'absolute_cross_precision_differences': cross_precision,
        'not_reproduced': {
            'endpoint_high_precision.max_tested_resolvent_discrepancy': 'Original 2.454546733e-91 value cannot be reproduced as stated because original argument grid and generating script were not supplied. Fresh grid results are reported separately.',
            'three_laplace_inverse_test_errors': 'Exact original complete/leaf inputs, argument grids and numerical implementation were not supplied. These three historical floating errors are not reproducible from this JSON alone; Laplace identities are audited separately.',
            'review_scope.method': 'Reviewer provenance assertion; this checker verifies selected results, not who performed the earlier work.',
            'global proof and priority': 'Not assessed or certified by these calculations.'},
        'scope_exclusions': ['Laplace generator/entropy recovery is assigned to the separate scope audit',
                             'No new rigorous endpoint entropy interval certificate',
                             'No global support-exhaustion or uniqueness proof', 'No literature priority certification'],
        'all_checks_passed': True}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(output, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'all_checks_passed': True, 'output': OUT.as_posix(),
                      'endpoint_120_digits': {key: calculations[-1][key] for key in ('z_star', 'sigma_source', 'sigma_target', 'delta_sigma', 'relative_entropy_separation_percent')},
                      'cross_precision_differences': cross_precision}, indent=2))


if __name__ == '__main__':
    main()
