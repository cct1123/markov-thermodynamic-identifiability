"""Regression guards for consequential numerical and enumeration behavior.

Run: python -m unittest analysis.capabilities.test_tools -v
"""

from itertools import combinations
import unittest
import warnings

import networkx as nx
import numpy as np
import sympy as sp

from analysis.research_tools.ctmc import (edge_flows, entropy_production, stationary,
                                         stationary_exact, stationary_mp, validate_generator)
from analysis.research_tools.graphs import connected_supports, observation_subsets


class CTMCTests(unittest.TestCase):
    def test_time_units_and_flux_entropy(self):
        # Irreversible circulation on a bidirected ring with known uniform law.
        q = np.array([[-3, 2, 1], [1, -3, 2], [2, 1, -3]], dtype=float)
        pi, _ = stationary(q)
        np.testing.assert_allclose(pi, np.ones(3)/3)
        flux, current = edge_flows(q, pi)
        np.testing.assert_allclose(current.sum(axis=1), 0, atol=1e-15)
        np.testing.assert_allclose(current, -current.T)
        self.assertTrue(np.all(np.diag(flux) == 0))
        self.assertAlmostEqual(entropy_production(q), np.log(2))
        for scale in [1e-100, 1e100]:
            np.testing.assert_allclose(stationary(q*scale)[0], pi)
            self.assertAlmostEqual(entropy_production(q*scale)/scale, np.log(2), places=12)

    def test_absent_edges_and_one_way_edges(self):
        reversible_path = [[-1, 1, 0], [1, -2, 1], [0, 1, -1]]
        self.assertAlmostEqual(entropy_production(reversible_path), 0)
        one_way = [[-1, 1, 0], [0, -1, 1], [1, 0, -1]]
        self.assertEqual(entropy_production(one_way), float("inf"))
        with self.assertRaises(ValueError):
            validate_generator(one_way, bidirected=True)

    def test_reducibility_is_not_positive_stationarity(self):
        q = [[-1, 1, 0, 0], [1, -1, 0, 0], [0, 0, -1, 1], [0, 0, 1, -1]]
        with self.assertRaises(ValueError):
            stationary(q)
        with self.assertRaises(ValueError):
            stationary_exact(q)
        with self.assertRaises(ValueError):
            stationary_mp(q)

    def test_validation_does_not_hide_small_rates_or_bad_rows(self):
        tiny = [[-1e-200, 1e-200], [2e-200, -2e-200]]
        np.testing.assert_allclose(stationary(tiny)[0], [2/3, 1/3])
        for q in ([[0, 1e-200], [1e-200, -1e-200]], [[1, -1], [1, -1]],
                  [[-1, np.nan], [1, -1]], [[0, 0], [0, 0]], [[1, 2, 3]], []):
            with self.assertRaises(ValueError):
                validate_generator(q)
        with self.assertRaises(ValueError):
            edge_flows([[-2, 2], [3, -3]], [0.5, 0.5])

    def test_ill_conditioning_has_an_exact_fallback(self):
        tiny = sp.Rational(1, 10**20)
        q = sp.Matrix([[-1, 1, 0], [1, -1-tiny, tiny], [0, tiny, -tiny]])
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            try:
                stationary(q)
            except ArithmeticError:
                pass  # Refusing an unreliable floating solve is also correct.
        self.assertTrue(any("ill-conditioned" in str(w.message) for w in caught))
        expected = sp.Matrix([sp.Rational(1, 3)]*3)
        self.assertEqual(stationary_exact(q), expected)
        ctx, pi, _ = stationary_mp(q, dps=100)
        self.assertLess(max(abs(p-ctx.mpf(1)/3) for p in pi), ctx.mpf("1e-75"))

    def test_exact_inputs_and_precision_context(self):
        for solver in (stationary_exact, stationary_mp):
            with self.assertRaises(ValueError):
                solver([[-2.0, 2.0], [3.0, -3.0]])
        ctx, pi, _ = stationary_mp([[-2, 2], [3, -3]], dps=90)
        self.assertEqual(ctx.dps, 90)
        self.assertLess(abs(pi[0]-ctx.mpf(3)/5), ctx.mpf("1e-85"))
        self.assertEqual(stationary([[0]])[0].tolist(), [1])
        self.assertEqual(stationary_exact([[0]]), sp.Matrix([1]))

    def test_conversion_cannot_silently_erase_support(self):
        epsilon = sp.Rational(1, 10**400)
        q = sp.Matrix([[-1-epsilon, 1, epsilon], [epsilon, -1-epsilon, 1], [1, epsilon, -1-epsilon]])
        with self.assertRaises(ArithmeticError):
            entropy_production(q)
        with self.assertRaises(ArithmeticError):
            validate_generator([["-1e-400", "1e-400"], ["1", "-1"]])
        # True zero strings remain acceptable and a one-state generator is valid.
        self.assertEqual(stationary([["0"]])[0].tolist(), [1])
        with self.assertRaises(ValueError):
            validate_generator(np.array([[-1+1j, 1], [1, -1-1j]]))
        with self.assertRaises(ValueError):
            edge_flows([[-2, 2], [3, -3]], np.array([0.6+0.1j, 0.4-0.1j]))
        # NumPy complex scalars in lists/object arrays can otherwise discard
        # imaginary parts with only a warning during float conversion.
        for scalar in (complex, np.complex64, np.complex128, np.clongdouble):
            q = [[scalar(-1+3j), scalar(1-3j)], [scalar(1), scalar(-1)]]
            pi = [scalar(0.6+1j), scalar(0.4-1j)]
            for wrap in (lambda x: x, lambda x: np.array(x, dtype=object)):
                with self.subTest(scalar=scalar, container=type(wrap(q)), input="generator"):
                    with self.assertRaises(ValueError):
                        validate_generator(wrap(q))
                with self.subTest(scalar=scalar, container=type(wrap(pi)), input="pi"):
                    with self.assertRaises(ValueError):
                        edge_flows([[-2, 2], [3, -3]], wrap(pi))


class GraphTests(unittest.TestCase):
    def test_atlas_against_independent_labelled_enumeration(self):
        # Generate every labelled simple n=4 support independently of the atlas.
        # Isomorphism comparison still trusts NetworkX in both routes.
        edges = list(combinations(range(4), 2))
        representatives = []
        connected_count = 0
        for mask in range(1 << len(edges)):
            g = nx.Graph()
            g.add_nodes_from(range(4))
            g.add_edges_from(e for i, e in enumerate(edges) if mask & (1 << i))
            if nx.is_connected(g):
                connected_count += 1
                if not any(nx.is_isomorphic(g, h) for h in representatives):
                    representatives.append(g)
        self.assertEqual(connected_count, 38)
        self.assertEqual(len(representatives), 6)
        atlas = list(connected_supports(4))
        self.assertTrue(all(sum(nx.is_isomorphic(g, h) for h in atlas) == 1 for g in representatives))

    def test_observation_orbits_preserve_non_equivalent_patterns(self):
        square = nx.cycle_graph(4)
        orbits = list(observation_subsets(square, 2))
        self.assertEqual(len(orbits), 2)  # adjacent and opposite pairs
        self.assertEqual(sorted(len(set(sum((list(e) for e in marks), []))) for marks in orbits), [3, 4])
        self.assertEqual(len(list(observation_subsets(square, 2, quotient=False))), 6)
        self.assertEqual(list(observation_subsets(square, 0)), [()])
        with self.assertRaises(ValueError):
            list(connected_supports(8))
        with self.assertRaises(ValueError):
            list(observation_subsets(square.to_directed(), 1))


if __name__ == "__main__":
    unittest.main()
