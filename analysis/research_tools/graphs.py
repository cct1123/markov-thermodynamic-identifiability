"""Small simple undirected support enumeration using trusted NetworkX routines."""

from itertools import combinations

import networkx as nx


def connected_supports(n):
    """One graph per unlabelled connected simple graph, 1 <= n <= 7.

    This exhausts support topologies only, not rates, directed graphs or marks.
    """
    if not isinstance(n, int) or not 1 <= n <= 7:
        raise ValueError("NetworkX atlas supports integer sizes 1 through 7")
    for g in nx.graph_atlas_g():
        if len(g) == n and nx.is_connected(g):
            yield g.copy()


def observation_subsets(g, k, *, quotient=True):
    """k unordered observed edges, optionally modulo automorphisms of support.

    Each selected edge represents BOTH directed marks. Only valid when state
    labels, edge identities, colors and attached rates are scientifically
    interchangeable; otherwise set quotient=False (all labelled subsets).
    The small-graph orbit reduction uses NetworkX GraphMatcher, not a custom
    graph-isomorphism implementation. It does not canonically label graphs.
    """
    if g.is_directed() or g.is_multigraph() or nx.number_of_selfloops(g):
        raise ValueError("requires a simple undirected support")
    if set(g.nodes) != set(range(len(g))):
        raise ValueError("nodes must be integers 0 through n-1")
    if not isinstance(k, int) or not 0 <= k <= g.number_of_edges():
        raise ValueError("k must be between zero and the number of edges")
    edges = sorted(tuple(sorted(e)) for e in g.edges)
    automorphisms = list(nx.algorithms.isomorphism.GraphMatcher(g, g).isomorphisms_iter()) if quotient else []
    seen = set()
    for subset in combinations(edges, k):
        key = (min(tuple(sorted(tuple(sorted((a[u], a[v]))) for u, v in subset))
                   for a in automorphisms) if quotient else subset)
        if key not in seen:
            seen.add(key)
            yield subset
