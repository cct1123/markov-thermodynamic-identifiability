"""Exact two-Laplace-point ambiguity for three-state trees.
Requires SymPy. Run: python two_laplace_counterexample.py
The data are only two full matrix-valued Laplace evaluations.
Observed rates are not independently supplied. No repository modules used.
"""
import sympy as sp

def reordered_transform(q: sp.Matrix, lam: sp.Expr) -> sp.Matrix:
    """F = P Psi_hat, reset rows reordered into state order (x, y)."""
    if q.shape != (3, 3) or lam.is_positive is not True:
        raise ValueError("Expected a 3x3 row generator and positive argument.")
    if q * sp.ones(3, 1) != sp.zeros(3, 1):
        raise ValueError("Generator rows must sum to zero.")
    killed = q.copy()
    killed[0, 1] = killed[1, 0] = 0  # Preserve original diagonals.
    select = sp.Matrix([[1, 0, 0], [0, 1, 0]])
    marks = sp.Matrix([[q[0, 1], 0], [0, q[1, 0]], [0, 0]])
    return (select * (lam * sp.eye(3) - killed).inv() * marks).applyfunc(sp.cancel)

def main() -> None:
    a = sp.Matrix([[-2, 1, 1], [1, -1, 0], [1, 0, -1]])
    b = sp.Matrix([
        [-sp.Rational(18, 5), sp.Rational(6, 5), sp.Rational(12, 5)],
        [1, -1, 0], [2, 0, -2],
    ])
    for lam in (sp.Integer(1), sp.Integer(2)):
        fa, fb = reordered_transform(a, lam), reordered_transform(b, lam)
        if fa != fb:
            raise AssertionError(f"Transforms differ at {lam}")
        print(f"lambda={lam}: common F={fa}")
    fa, fb = (reordered_transform(q, sp.Integer(3)) for q in (a, b))
    if fa == fb:
        raise AssertionError("Full transform functions must differ.")
    print(f"lambda=3: F_A={fa}; F_B={fb}")

    # ANY distinct positive arguments l1<l2, in a leaf model:
    # G(lambda)=u+v/(lambda+h). Vary h near the source.
    l1, l2, h, g1, g2 = sp.symbols("l1 l2 h g1 g2", positive=True)
    v = (g1-g2)*(l1+h)*(l2+h)/(l2-l1)
    u = g1-v/(l1+h)
    for lam, target in ((l1, g1), (l2, g2)):
        if sp.cancel(u+v/(lam+h)-target) != 0:
            raise AssertionError("General construction failed.")
    print("General two-point leaf construction: both identities verified.")
    print("Positivity persists locally at a source with u>0, v>0, h>0.")
    print("Not a counterexample with separately fixed observed rates.")

if __name__ == "__main__":
    main()
