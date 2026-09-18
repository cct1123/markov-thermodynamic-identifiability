"""Exact checks supporting the separate two-point entropy corollary.

Run: python -B -m unittest analysis.correctness.test_laplace_entropy -v
These direct resolvent and stationary-flux checks cover symbolic tree strata
and rational triangles; they do not replace the conventional support proof.
Rate tuples passed to the existing inverse use (r,s,a,b,c,d).
"""

import unittest

import sympy as sp

from analysis.correctness import laplace_two as audit


def direct_transform(q, lam):
    """Joint next-mark transform in (+,-) row order, for two or three states."""
    killed = q.copy()
    killed[0, 1] = killed[1, 0] = 0
    reset = sp.zeros(2, q.rows)
    reset[0, 1] = reset[1, 0] = 1
    marks = sp.zeros(q.rows, 2)
    marks[0, 0], marks[1, 1] = q[0, 1], q[1, 0]
    return (reset * (lam * sp.eye(q.rows) - killed).inv() * marks).applyfunc(sp.cancel)


def stationary_fluxes(q):
    """Solve stationarity directly, independently of the reconstruction."""
    system = q.T.copy()
    system[q.rows - 1, :] = sp.ones(1, q.rows)
    rhs = sp.zeros(q.rows, 1)
    rhs[q.rows - 1] = 1
    pi = (system.inv() * rhs).applyfunc(sp.cancel)
    return pi, sp.diag(*pi) * q


def flux_entropy(q, flux):
    """Exact edge-flux definition; callers supply reciprocal supported rates."""
    terms = []
    for i in range(q.rows):
        for j in range(i + 1, q.rows):
            if q[i, j] != 0:
                current = sp.cancel(flux[i, j] - flux[j, i])
                ratio = sp.cancel(flux[i, j] / flux[j, i])
                terms.append(current * sp.log(ratio))
    return sp.simplify(sum(terms, sp.S.Zero))


class TwoPointEntropyTests(unittest.TestCase):
    def assert_stationary(self, q, pi):
        self.assertEqual((pi.T * q).applyfunc(sp.cancel), sp.zeros(1, q.rows))
        self.assertEqual(sp.cancel(sum(pi)), 1)
        self.assertTrue(all(value.is_positive is True for value in pi))

    def assert_tree_data_convention(self, q, lam):
        psi = direct_transform(q, lam)
        f = sp.Matrix([[0, 1], [1, 0]]) * psi
        m = f.inv().applyfunc(sp.cancel)
        self.assertEqual(f[0, 1], 0)
        self.assertEqual(f[1, 0], 0)
        self.assertEqual(m[0, 1], 0)
        self.assertEqual(m[1, 0], 0)
        self.assertTrue(psi[0, 1].is_positive is True)
        self.assertTrue(psi[1, 0].is_positive is True)

    def test_symbolic_leaf_strata_have_zero_entropy(self):
        r, s, a, b, c, d, lam = sp.symbols("r s a b c d lambda", positive=True)
        cases = {
            "x_leaf": sp.Matrix([[-r-a, r, a], [s, -s, 0], [b, 0, -b]]),
            "y_leaf": sp.Matrix([[-r, r, 0], [s, -s-c, c], [0, d, -d]]),
        }
        for name, q in cases.items():
            with self.subTest(support=name):
                pi, flux = stationary_fluxes(q)
                self.assert_stationary(q, pi)
                self.assertEqual((flux - flux.T).applyfunc(sp.cancel), sp.zeros(3))
                self.assertEqual(flux_entropy(q, flux), 0)
                self.assert_tree_data_convention(q, lam)

    def test_symbolic_two_state_stratum_has_zero_entropy(self):
        r, s, lam = sp.symbols("r s lambda", positive=True)
        q = sp.Matrix([[-r, r], [s, -s]])
        pi, flux = stationary_fluxes(q)
        self.assert_stationary(q, pi)
        self.assertEqual(pi, sp.Matrix([s / (r+s), r / (r+s)]))
        self.assertEqual((flux - flux.T).applyfunc(sp.cancel), sp.zeros(2))
        self.assertEqual(flux_entropy(q, flux), 0)
        self.assert_tree_data_convention(q, lam)

    def test_two_points_restore_triangle_generator_and_flux_entropy(self):
        lambdas = (sp.Rational(1, 3), sp.Rational(7, 4))
        cases = (
            ("equilibrium", (2, 1, 3, 1, 3, 2),
             sp.Matrix([[-5, 2, 3], [1, -4, 3], [1, 2, -3]]), sp.S.Zero),
            ("nonequilibrium", (2, 3, 4, 5, 6, 7),
             sp.Matrix([[-6, 2, 4], [3, -9, 6], [5, 7, -12]]),
             sp.Rational(12, 83) * sp.log(sp.Rational(7, 5))),
        )
        for name, rates, q, expected_entropy in cases:
            with self.subTest(source=name):
                data = [direct_transform(q, lam) for lam in lambdas]
                for psi in data:
                    f = sp.Matrix([[0, 1], [1, 0]]) * psi
                    self.assertGreater(f[0, 1], 0)
                    self.assertGreater(f[1, 0], 0)
                recovered = audit.recover_two(data, lambdas)
                self.assertEqual(recovered, rates)
                recovered_q = audit.generator(recovered)
                self.assertEqual(recovered_q, q)
                pi, flux = stationary_fluxes(q)
                self.assert_stationary(q, pi)
                restored_pi, restored_flux = stationary_fluxes(recovered_q)
                self.assertEqual(restored_pi, pi)
                self.assertEqual(restored_flux, flux)
                entropy = flux_entropy(q, flux)
                self.assertEqual(sp.simplify(entropy - expected_entropy), 0)
                self.assertEqual(flux_entropy(recovered_q, restored_flux), entropy)
                if name == "equilibrium":
                    self.assertEqual(flux - flux.T, sp.zeros(3))
                else:
                    self.assertNotEqual(flux - flux.T, sp.zeros(3))
                    self.assertGreater(entropy, 0)


if __name__ == "__main__":
    unittest.main()
