"""Exact regression tests against full generators and independently fixed data.

Run: python -B -m unittest analysis.correctness.test_laplace_two -v
All tuples here use (r,s,a,b,c,d), explicitly matching the user's proposal.
"""

import unittest

import sympy as sp

from analysis.correctness import laplace_two as audit


class TwoPointTests(unittest.TestCase):
    def setUp(self):
        self.first = (1, 1, 1, 1, 0, 0)
        self.second = (sp.Rational(6, 5), 1, sp.Rational(12, 5), 2, 0, 0)

    def test_user_order_and_generator_diagonal_retention(self):
        expected = sp.Matrix([[-sp.Rational(18, 5), sp.Rational(6, 5), sp.Rational(12, 5)],
                              [1, -1, 0], [2, 0, -2]])
        self.assertEqual(audit.generator(self.second), expected)
        self.assertEqual(expected*sp.ones(3, 1), sp.zeros(3, 1))

    def test_full_two_point_matrices_match_literal_rationals(self):
        for rates in (self.first, self.second):
            self.assertEqual(audit.transform(rates, 1),
                             sp.Matrix([[0, sp.Rational(1, 2)], [sp.Rational(2, 5), 0]]))
            self.assertEqual(audit.transform(rates, 2),
                             sp.Matrix([[0, sp.Rational(1, 3)], [sp.Rational(3, 11), 0]]))
            self.assertEqual(audit.transform(rates, 0), sp.Matrix([[0, 1], [1, 0]]))

    def test_third_point_and_zero_time_rate_distinguish(self):
        self.assertEqual(audit.transform(self.first, 3),
                         sp.Matrix([[0, sp.Rational(1, 4)], [sp.Rational(4, 19), 0]]))
        self.assertEqual(audit.transform(self.second, 3),
                         sp.Matrix([[0, sp.Rational(1, 4)], [sp.Rational(10, 47), 0]]))
        lam = sp.symbols("lambda", positive=True)
        difference = audit.clean(audit.transform(self.first, lam)-audit.transform(self.second, lam))
        expected = -lam*(lam-1)*(lam-2)/((lam**2+3*lam+1)*(5*lam**2+28*lam+12))
        self.assertEqual(sp.cancel(difference[1, 0]-expected), 0)
        self.assertEqual(sp.limit(lam*difference[1, 0], lam, sp.oo), -sp.Rational(1, 5))

    def test_stationary_absolute_intensity_but_not_mark_fraction_distinguishes(self):
        expected = ((sp.Rational(1, 3),)*2, (sp.Rational(6, 17),)*2)
        for rates, intensities in zip((self.first, self.second), expected):
            _, actual = audit.stationary_and_mark_intensities(rates)
            self.assertEqual(actual, intensities)
            self.assertEqual(tuple(value/sum(actual) for value in actual),
                             (sp.Rational(1, 2), sp.Rational(1, 2)))

    def test_two_reconstructs_positive_triangles_at_noninteger_points(self):
        lambdas = (sp.Rational(1, 3), sp.Rational(7, 4))
        cases = ((1, 1, 1, 1, 1, 1),
                 (sp.Rational(6, 5), sp.Rational(4, 5), sp.Rational(9, 10),
                  sp.Rational(3, 10), sp.Rational(2, 5), sp.Rational(11, 10)),
                 (sp.Rational(1, 100), 23, sp.Rational(1, 2), sp.Rational(4, 7),
                  sp.Rational(9, 2), sp.Rational(3, 13)))
        for rates in cases:
            data = [audit.transform(rates, value) for value in lambdas]
            self.assertEqual(audit.recover_two(data, lambdas), tuple(map(sp.sympify, rates)))

    def test_leaf_domain_and_calibrated_or_third_point_recovery(self):
        for rates in (self.first, self.second, (1, 2, 0, 0, 3, 4)):
            data = [audit.transform(rates, value) for value in (1, 2, 3)]
            with self.assertRaisesRegex(ValueError, "leaf"):
                audit.recover_two(data[:2], (1, 2))
            self.assertEqual(audit.recover_two_calibrated(data[:2], (1, 2), rates[0], rates[1]),
                             tuple(map(sp.sympify, rates)))
            self.assertEqual(audit.recover_three(data, (1, 2, 3)), tuple(map(sp.sympify, rates)))

    def test_one_point_does_not_identify_complete_triangles(self):
        first = (1, 1, 1, 1, 1, 1)
        second = (2, 2, 3, sp.Rational(2, 5), 3, sp.Rational(2, 5))
        expected = sp.Matrix([[sp.Rational(1, 21), sp.Rational(8, 21)],
                              [sp.Rational(8, 21), sp.Rational(1, 21)]])
        self.assertEqual(audit.transform(first, 1), expected)
        self.assertEqual(audit.transform(second, 1), expected)
        self.assertNotEqual(audit.transform(first, 2), audit.transform(second, 2))


if __name__ == "__main__":
    unittest.main()
