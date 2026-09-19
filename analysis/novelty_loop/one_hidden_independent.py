"""Exact independent checks for a one-fully-hidden-vertex inverse.

Run from root: .venv\Scripts\python.exe -B analysis/novelty_loop/one_hidden_independent.py
Writes only outputs/novelty-loop-2026-09-19/one-hidden-independent.json.
All rational inputs are embedded below; no random search or optimization is used.
"""
if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import platform
import sys

import mpmath as mp
import sympy as sp


def generator(n, rates):
    q = sp.zeros(n)
    for (i, j), rate in rates.items():
        q[i, j] = sp.Rational(rate)
    for i in range(n):
        q[i, i] = -sum(q[i, j] for j in range(n) if j != i)
    assert q * sp.ones(n, 1) == sp.zeros(n, 1)
    for i in range(n):
        for j in range(i + 1, n):
            assert (q[i, j] > 0) == (q[j, i] > 0)
    # Directed reachability; positivity of a stationary solution alone is insufficient.
    reached = {0}
    for _ in range(n):
        reached |= {j for i in reached for j in range(n) if i != j and q[i, j] > 0}
    assert len(reached) == n
    return q


def killed(q, marks):
    t = q.copy()
    for i, j in marks:
        assert q[i, j] > 0
        t[i, j] = 0
    return t


def full_mark_matrix(q, marks, s):
    resolvent = (s * sp.eye(q.rows) - killed(q, marks)).inv()
    return sp.Matrix([[resolvent[b, c] * q[c, d]
                       for c, d in marks] for a, b in marks])


def aggregate(full, marks, m):
    resets = [next(j for j, edge in enumerate(marks) if edge[1] == i)
              for i in range(m)]
    f = sp.Matrix([[sum(full[resets[i], j] for j, edge in enumerate(marks)
                        if edge[0] == k) for k in range(m)] for i in range(m)])
    return f, resets


def recover(matrices, marks, samples, m, two_point_complete=False):
    """Uses only supplied full Laplace matrices and labelled observed edges."""
    fs = [aggregate(mat, marks, m)[0] for mat in matrices]
    hs = [f.inv() for f in fs]
    ys = [(h * sp.ones(m, 1) - sp.ones(m, 1)) / s
          for h, s in zip(hs, samples)]
    s1, s2 = samples[:2]
    if two_point_complete:
        i, j = next((i, j) for i, j in marks if hs[0][i, j] != 0)
        ratio = hs[0][i, j] / hs[1][i, j]
        d = sp.cancel((s2 - ratio * s1) / (ratio - 1))
    else:
        s3 = samples[2]
        pivot = next(i for i in range(m) if ys[0][i] != ys[1][i])
        ratio = ((ys[0][pivot] - ys[1][pivot]) /
                 (ys[1][pivot] - ys[2][pivot])) * (s3 - s2) / (s2 - s1)
        d = sp.cancel((s3 - ratio * s1) / (ratio - 1))
    bs = [(ys[0][i] - ys[1][i]) * (s1 + d) * (s2 + d) / (s2 - s1)
          for i in range(m)]
    aa = [sp.cancel(ys[0][i] - bs[i] / (s1 + d)) for i in range(m)]
    ks = [1 / a for a in aa]
    us = sp.Matrix([sp.cancel(bs[i] / aa[i]) for i in range(m)])
    diagonal = sp.diag(*ks)
    w = (diagonal * ((hs[1] - hs[0]) / (s2 - s1)) - sp.eye(m)) * (s1 + d) * (s2 + d)
    pivot = next(i for i in range(m) if us[i] > 0)
    vs = sp.Matrix(1, m, [sp.cancel(w[pivot, j] / us[pivot]) for j in range(m)])
    assert sum(vs) == d
    assert w == us * vs
    a = s1 * sp.eye(m) - diagonal * hs[0] - w / (s1 + d)
    q = a.row_join(us).col_join(vs.row_join(sp.Matrix([[-d]])))
    _, resets = aggregate(matrices[0], marks, m)
    for col, (i, j) in enumerate(marks):
        q[i, j] = ks[i] * matrices[0][resets[i], col] / fs[0][i, i]
    return q.applyfunc(sp.cancel)


def stationary(q):
    basis = q.T.nullspace()
    assert len(basis) == 1
    pi = basis[0] / sum(basis[0])
    assert all(x > 0 for x in pi)
    assert q.T * pi == sp.zeros(q.rows, 1)
    return pi


def matrix_strings(mat):
    return [[str(x) for x in row] for row in mat.tolist()]


def entropy_numeric(q, digits=100):
    pi = stationary(q)
    with mp.workdps(digits):
        def cv(x):
            return mp.mpf(str(sp.numer(x))) / mp.mpf(str(sp.denom(x)))
        value = mp.mpf(0)
        for i in range(q.rows):
            for j in range(i + 1, q.rows):
                if q[i, j]:
                    f, r = cv(pi[i] * q[i, j]), cv(pi[j] * q[j, i])
                    value += (f - r) * (mp.log(f) - mp.log(r))
        return mp.nstr(value, 60)


def small_support_checks():
    results = []
    for n in (4, 5, 6):
        m = n - 1
        marks = sorted([(i, i + 1) for i in range(m - 1)] +
                       [(i + 1, i) for i in range(m - 1)])
        for label, hidden_neighbors, complete_visible in (
            ('hidden-leaf', [0], False),
            ('partial-hidden-incidence', [0, m - 1], False),
            ('full-hidden-incidence-visible-sparse', list(range(m)), False),
            ('complete-generator', list(range(m)), True),
        ):
            pairs = {(i, i + 1) for i in range(m - 1)}
            if complete_visible:
                pairs |= {(i, j) for i in range(m) for j in range(i + 1, m)}
            pairs |= {(i, m) for i in hidden_neighbors}
            rates = {}
            for i, j in sorted(pairs):
                rates[i, j] = sp.Rational(2 * i + j + 3, j + 2)
                rates[j, i] = sp.Rational(i + 3 * j + 2, i + 2)
            q = generator(n, rates)
            ss = list(map(sp.Rational, (1, 2, 5)))
            mats = [full_mark_matrix(q, marks, s) for s in ss]
            assert recover(mats, marks, ss, m) == q
            two = None
            if len(hidden_neighbors) == m:
                assert recover(mats[:2], marks, ss[:2], m, True) == q
                two = True
            results.append({'N': n, 'stratum': label, 'rates': matrix_strings(q),
                            'observed_marks': marks, 'samples': [str(s) for s in ss],
                            'three_point_exact_recovery': True,
                            'two_point_exact_recovery': two})
    return results


def entropy_sharpness():
    marks = [(i, j) for i in range(3) for j in range(3) if i != j]
    def leaf(k, u, v):
        return generator(4, {(0, 1): k / 2, (0, 2): k / 2,
                             (1, 0): 2, (1, 2): 1, (2, 0): 1, (2, 1): 1,
                             (0, 3): u, (3, 0): v})
    q1 = leaf(sp.Rational(2), sp.Rational(1), sp.Rational(1))
    q2 = leaf(sp.Rational(12, 5), sp.Rational(12, 5), sp.Rational(2))
    mats1 = [full_mark_matrix(q1, marks, sp.Rational(s)) for s in (1, 2, 3)]
    mats2 = [full_mark_matrix(q2, marks, sp.Rational(s)) for s in (1, 2, 3)]
    assert mats1[0] == mats2[0] and mats1[1] == mats2[1]
    assert mats1[2] != mats2[2]
    pis = [stationary(q) for q in (q1, q2)]
    coefficients = []
    for q, pi in zip((q1, q2), pis):
        # A single visible cycle has affinity log(2); the hidden leaf has zero current.
        assert pi[0] * q[0, 3] == pi[3] * q[3, 0]
        current = pi[1] * q[1, 0] - pi[0] * q[0, 1]
        assert current == pi[0] * q[0, 2] - pi[2] * q[2, 0]
        assert current == pi[2] * q[2, 1] - pi[1] * q[1, 2]
        affinity_argument = (q[1, 0] * q[0, 2] * q[2, 1] /
                             (q[0, 1] * q[2, 0] * q[1, 2]))
        assert affinity_argument == 2
        coefficients.append(current)
    assert coefficients == [sp.Rational(1, 17), sp.Rational(6, 97)]
    assert coefficients[1] - coefficients[0] == sp.Rational(5, 1649)
    assert recover(mats1, marks, list(map(sp.Rational, (1, 2, 3))), 3) == q1
    assert recover(mats2, marks, list(map(sp.Rational, (1, 2, 3))), 3) == q2
    # Calibrated rates: one point remains insufficient; two points distinguish.
    qc = leaf(sp.Rational(2), sp.Rational(3, 2), sp.Rational(2))
    assert full_mark_matrix(qc, marks, sp.Rational(1)) == mats1[0]
    assert full_mark_matrix(qc, marks, sp.Rational(2)) != mats1[1]
    pc = stationary(qc)
    assert pc[1] * qc[1, 0] - pc[0] * qc[0, 1] == sp.Rational(4, 63)
    extensions = []
    for n in (5, 6):
        m = n - 1
        def extend(q):
            rates = {(i, j): q[i, j] for i in range(3) for j in range(3) if i != j}
            rates[0, m], rates[m, 0] = q[0, 3], q[3, 0]
            for visible_leaf in range(3, m):
                rates[1, visible_leaf] = rates[visible_leaf, 1] = sp.Rational(1)
            return generator(n, rates)
        eq1, eq2 = extend(q1), extend(q2)
        emarks = [(i, j) for i in range(m) for j in range(m)
                  if i != j and eq1[i, j] > 0]
        for s in map(sp.Rational, (1, 2)):
            assert full_mark_matrix(eq1, emarks, s) == full_mark_matrix(eq2, emarks, s)
        assert full_mark_matrix(eq1, emarks, sp.Rational(3)) != full_mark_matrix(eq2, emarks, sp.Rational(3))
        epis = [stationary(eq) for eq in (eq1, eq2)]
        ecs = [p[1] * eq[1, 0] - p[0] * eq[0, 1] for eq, p in zip((eq1, eq2), epis)]
        assert ecs == [1 / sp.Rational(17 + 3 * (n - 4)),
                       6 / sp.Rational(97 + 18 * (n - 4))]
        assert ecs[1] > ecs[0]
        extensions.append({'N': n, 'Q1': matrix_strings(eq1), 'Q2': matrix_strings(eq2),
                           'observed_marks': emarks,
                           'entropy_coefficients_of_log2': list(map(str, ecs)),
                           'exact_agreement_at_1_2': True, 'exact_disagreement_at_3': True})
    return {'Q1': matrix_strings(q1), 'Q2': matrix_strings(q2),
            'observed_marks': marks, 'stationary_vectors': [list(map(str, pi)) for pi in pis],
            'entropy_coefficients_of_log2': list(map(str, coefficients)),
            'entropy_gap': '5*log(2)/1649',
            'full_mark_matrices_Q1': [matrix_strings(x) for x in mats1],
            'full_mark_matrices_Q2': [matrix_strings(x) for x in mats2],
            'agreement_samples': ['1', '2'], 'disagreement_sample': '3',
            'extensions': extensions,
            'calibrated_one_point_witness': {'Q': matrix_strings(qc),
                'stationary': list(map(str, pc)), 'entropy': '4*log(2)/63',
                'agrees_with_Q1_at': '1', 'differs_from_Q1_at': '2'}}


def missing_visible_pair():
    marks = [(0, 1), (1, 0), (1, 2), (2, 1)]
    pairs = [(0, 1), (1, 2), (0, 3), (1, 3), (2, 3)]
    base_rates = {(i, j): sp.Rational(1) for pair in pairs for i, j in (pair, pair[::-1])}
    q0 = generator(4, base_rates)
    assert stationary(q0) == sp.ones(4, 1) / 4
    results = []
    for n in (2, 4, 8, 16, 32):
        rates = base_rates.copy()
        eps, reverse = sp.Rational(1, n), sp.Rational(1, 2 ** (n * n))
        rates[0, 2], rates[2, 0] = eps, reverse
        rates[0, 3] -= eps + reverse
        q = generator(4, rates)
        assert sp.trace(q) == sp.trace(q0)
        assert all(q[i, j] == q0[i, j] for i, j in marks)
        assert max(q[i, j] for i in range(4) for j in range(4) if i != j) <= 1
        pi = stationary(q)
        sigma = entropy_numeric(q)
        results.append({'n': n, 'epsilon': str(eps), 'reverse_rate': str(reverse),
                        'stationary': list(map(str, pi)), 'entropy_100dps': sigma,
                        'fixed_trace': str(sp.trace(q)),
                        'observed_rates_unchanged': True, 'rate_cap_one': True})
    return {'source_Q': matrix_strings(q0), 'observed_marks': marks,
            'source_hidden_adjacent_to_every_visible': True,
            'missing_visible_pair': [0, 2],
            'construction': 'q02=1/n; q20=2**(-n*n); q03=1-1/n-2**(-n*n)',
            'divergence_proved_in_note': 'sigma/n -> log(2)/4', 'samples': results}


def larger_state_cap():
    n = 4
    marks = [(0, 1), (1, 0), (1, 2), (2, 1)]
    rates = {(i, j): sp.Rational(i + 2 * j + 2, i + j + 2)
             for i in range(n) for j in range(n) if i != j}
    q = generator(n, rates)
    membership = sp.zeros(n + 1, n)
    for i in range(n):
        membership[i, i] = 1
    membership[n, n - 1] = 1
    results = []
    for reverse in (sp.Rational(1), sp.Rational(1, 10), sp.Rational(1, 100)):
        split_rates = {}
        for i in range(n - 1):
            for j in range(n - 1):
                if i != j:
                    split_rates[i, j] = q[i, j]
            split_rates[i, n - 1] = q[i, n - 1] / 2
            split_rates[i, n] = q[i, n - 1] / 2
            split_rates[n - 1, i] = q[n - 1, i]
            split_rates[n, i] = q[n - 1, i]
        split_rates[n - 1, n], split_rates[n, n - 1] = sp.Rational(1), reverse
        qp = generator(n + 1, split_rates)
        assert qp * membership == membership * q
        assert killed(qp, marks) * membership == membership * killed(q, marks)
        for s in map(sp.Rational, (1, 2, 5)):
            assert full_mark_matrix(qp, marks, s) == full_mark_matrix(q, marks, s)
        # Equality for all s and all times follows from the exact intertwining,
        # rather than from the three spot checks.
        pi = stationary(qp)
        results.append({'reverse_internal_rate': str(reverse),
                        'split_Q': matrix_strings(qp), 'stationary': list(map(str, pi)),
                        'exact_killed_intertwining': True,
                        'three_laplace_spot_checks': True,
                        'entropy_100dps': entropy_numeric(qp)})
    return {'source_Q': matrix_strings(q), 'observed_marks': marks,
            'membership_matrix': matrix_strings(membership), 'samples': results,
            'all_time_equality_certificate': 'T_split*C=C*T; C*B=B_split; R_split*C=R',
            'unboundedness': 'internal reverse t->0; forward=1; pi_clone1(t)->positive'}


def main():
    output = {
        'status': 'all asserted exact checks passed; conventional proofs in companion note',
        'falsification_scope': {
            'claim': 'Three distinct positive full marked Laplace matrices recover a reciprocal irreducible generator with a fixed labelled covered set and exactly one extra hidden vertex.',
            'checks': 'N=4,5,6 selected rational support strata; no exhaustive continuous-rate search claimed.',
            'tolerance': 'zero for rational matrix identities; numerical entropy diagnostics use 100 decimal digits',
            'optimizer': None, 'rng': None,
            'counterexample_condition': 'Different valid Q with exactly equal sample matrices; exact all-time claims need intertwining or rational identities.',
        },
        'support_checks': small_support_checks(),
        'two_point_entropy_counterexample': entropy_sharpness(),
        'missing_visible_pair_counterexample': missing_visible_pair(),
        'larger_state_cap_counterexample': larger_state_cap(),
        'provenance': {
            'utc': datetime.now(timezone.utc).isoformat(),
            'command': '.venv\\Scripts\\python.exe -B analysis/novelty_loop/one_hidden_independent.py',
            'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
            'python': sys.version, 'platform': platform.platform(),
            'sympy': sp.__version__, 'mpmath': mp.__version__,
            'inputs': 'Exact rational matrices constructed in this self-contained script; no imported local scientific helpers.',
        },
    }
    root = Path(__file__).resolve().parents[2]
    path = root / 'outputs/novelty-loop-2026-09-19/one-hidden-independent.json'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(output, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(path), 'support_cases': len(output['support_checks']),
                      'exact_checks': 'passed', 'script_sha256': output['provenance']['script_sha256']}))


if __name__ == '__main__':
    main()
