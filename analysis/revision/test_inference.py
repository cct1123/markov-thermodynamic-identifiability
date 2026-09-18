"""Independent numerical checks; run python -B -m unittest analysis.revision.test_inference -v."""

import unittest
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm

from analysis.revision import inference as inf


class InferenceTests(unittest.TestCase):
    def setUp(self):
        self.p = np.array([1.2, .8, .9, .4, .3, 1.1])

    def test_resolvent_against_time_domain_quadrature(self):
        q = inf.generator(self.p)
        q[0, 1] = q[1, 0] = 0
        b = np.array([[self.p[0], 0.], [0., self.p[1]], [0., 0.]])
        observed = inf.laplace(self.p, [.2, 1., 5.])
        for row, destination, index in ((0, 0, 0), (0, 1, 1), (1, 0, 2), (1, 1, 0)):
            rate = [.2, 1., 5.][index]
            integral = quad(lambda t: np.exp(-rate*t)*(inf.RESET@expm(q*t)@b)[row, destination],
                            0., np.inf, epsabs=1e-11, epsrel=1e-11)[0]
            self.assertAlmostEqual(integral, observed[row, index, destination], places=10)

    def test_full_six_rate_jacobian_complex_step(self):
        for p in (self.p, inf.fixed_trace_rates(.2, .01), inf.fixed_trace_rates(0., 0.)):
            analytic = inf.laplace(p, [.2, 1., 5.], True)[1]
            independent = np.empty_like(analytic)
            for j in range(6):
                perturbed = p.astype(complex)
                perturbed[j] += 1e-25j
                independent[:, j] = inf.laplace(perturbed, [.2, 1., 5.]).ravel().imag/1e-25
            np.testing.assert_allclose(analytic, independent, rtol=2e-12, atol=1e-14)

    def test_entropy_cycle_against_stationary_edge_sum(self):
        for p in (self.p, inf.fixed_trace_rates(.2, np.exp(-25.)), np.ones(6)):
            q, pi = inf.generator(p), inf.stationary(p)
            direct = 0.
            for i, j in ((0, 1), (0, 2), (1, 2)):
                f, reverse = pi[i]*q[i, j], pi[j]*q[j, i]
                direct += (f-reverse)*(np.log(f)-np.log(reverse))
            self.assertAlmostEqual(inf.entropy(p), direct, places=12)
            np.testing.assert_allclose(pi@q, 0., atol=2e-15)

    def test_entropy_gradient_complex_step(self):
        _, gradient = inf.entropy(self.p, True)
        independent = []
        for j in range(6):
            p = self.p.astype(complex)
            p[j] += 1e-25j
            independent.append(inf.entropy(p).imag/1e-25)
        np.testing.assert_allclose(gradient, independent, rtol=1e-12, atol=1e-14)

    def test_noiseless_recovery_all_six_unknown_rates(self):
        for p in (self.p, inf.fixed_trace_rates(.2, .01)):
            fitted = inf.fit_rates(inf.laplace(p, inf.DEFAULT_LAMBDAS))
            self.assertTrue(fitted["success"])
            self.assertFalse(fitted["boundary"])
            np.testing.assert_allclose(fitted["rates"], p, atol=2e-7, rtol=2e-6)
            self.assertLess(fitted["cost"], 1e-17)

    def test_absolute_inverse_regular_at_tree_relative_inverse_degrades(self):
        _, jt = inf.laplace(inf.fixed_trace_rates(0., 0.), inf.DEFAULT_LAMBDAS, True)
        self.assertGreater(np.linalg.svd(jt, compute_uv=False)[-1], .001)
        values = []
        for k in (1e-4, 1e-6, 1e-8):
            p = inf.fixed_trace_rates(.2, k)
            _, j = inf.laplace(p, inf.DEFAULT_LAMBDAS, True)
            values.append(np.linalg.svd(j*p, compute_uv=False)[-1]/k)
        np.testing.assert_allclose(values, values[-1], rtol=.002)

    def test_stationary_marked_trajectory_against_exact_joint_moments(self):
        record = inf.simulate_marked_ctmc(self.p, 40000, np.random.default_rng(371824))
        means, covariance, counts = inf.empirical_moments(record, inf.DEFAULT_LAMBDAS)
        truth = inf.laplace(self.p, inf.DEFAULT_LAMBDAS)
        asymptotic = inf.theoretical_moment_covariance(self.p, inf.DEFAULT_LAMBDAS)/40000
        self.assertEqual(sum(counts), 40000)
        self.assertTrue(np.all(record["times"] > 0))
        np.testing.assert_array_equal(record["incoming"][1:], record["outgoing"][:-1])
        self.assertLess(np.max(np.abs(means.ravel()-truth.ravel())/np.sqrt(np.diag(asymptotic))), 6.)
        # High-lambda same-mark features are rare: relative error of an almost
        # zero variance is not a calibrated accuracy criterion. Compare the
        # covariance in absolute spectral scale, alongside standardized means.
        self.assertLess(np.linalg.norm(covariance-asymptotic)/np.linalg.norm(asymptotic), .04)
        pi = inf.stationary(self.p)
        exact_frequency = (pi[:2]*self.p[:2]).sum()
        self.assertLess(abs(40001/record["horizon"]-exact_frequency), .025)


if __name__ == "__main__":
    unittest.main()
