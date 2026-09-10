"""Exact checks of the theta-family residue reassignment in Q(sqrt(6)).

Run from the repository root:
    python -B analysis/check_theta_residue_construction.py

Standard library only. No numerical search or external input data. The five
embedded examples cover a generic point, both hidden-eigenvalue coincidences,
and the unique nonminimal point. Output is outputs/theta-residue-checks.json.
The local quadratic-number helper exists only for this focused exact check.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from fractions import Fraction
from functools import total_ordering
import hashlib
import json
import math
from pathlib import Path
import platform


@total_ordering
@dataclass(frozen=True, eq=False)
class Q6:
    r: Fraction = Fraction(0)
    s: Fraction = Fraction(0)

    def __post_init__(self):
        object.__setattr__(self, "r", Fraction(self.r))
        object.__setattr__(self, "s", Fraction(self.s))

    def __add__(self, other):
        other = number(other)
        return Q6(self.r + other.r, self.s + other.s)

    __radd__ = __add__

    def __neg__(self):
        return Q6(-self.r, -self.s)

    def __sub__(self, other):
        return self + -number(other)

    def __rsub__(self, other):
        return number(other) + -self

    def __mul__(self, other):
        other = number(other)
        return Q6(self.r * other.r + 6 * self.s * other.s,
                  self.r * other.s + self.s * other.r)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = number(other)
        norm = other.r * other.r - 6 * other.s * other.s
        if norm == 0:
            raise ZeroDivisionError("zero quadratic-field divisor")
        return Q6((self.r * other.r - 6 * self.s * other.s) / norm,
                  (self.s * other.r - self.r * other.s) / norm)

    def __rtruediv__(self, other):
        return number(other) / self

    def __bool__(self):
        return bool(self.r or self.s)

    def sign(self):
        if self.s == 0:
            return (self.r > 0) - (self.r < 0)
        if self.r == 0:
            return (self.s > 0) - (self.s < 0)
        if self.r * self.s > 0:
            return 1 if self.r > 0 else -1
        norm = self.r * self.r - 6 * self.s * self.s
        return (1 if self.r > 0 else -1) * (1 if norm > 0 else -1)

    def __eq__(self, other):
        if not isinstance(other, (Q6, int, Fraction)):
            return NotImplemented
        other = number(other)
        return self.r == other.r and self.s == other.s

    def __lt__(self, other):
        return (self - other).sign() < 0

    def __hash__(self):
        return hash(self.r) if not self.s else hash((self.r, self.s))

    def __float__(self):
        return float(self.r) + math.sqrt(6) * float(self.s)

    def encoded(self):
        return {"rational": str(self.r), "sqrt6_coefficient": str(self.s)}


def number(value):
    return value if isinstance(value, Q6) else Q6(value)


ZERO, ONE, ROOT6 = Q6(), Q6(1), Q6(0, 1)


def matrix(rows):
    return [[number(v) for v in row] for row in rows]


def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])


def transpose(a):
    return [list(row) for row in zip(*a)]


def multiply(a, b):
    assert len(a[0]) == len(b)
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), ZERO)
             for j in range(len(b[0]))] for i in range(len(a))]


def inverse(a):
    n = len(a)
    work = [row[:] + unit for row, unit in zip(a, identity(n))]
    for col in range(n):
        pivot = next(i for i in range(col, n) if work[i][col])
        work[col], work[pivot] = work[pivot], work[col]
        factor = work[col][col]
        work[col] = [v / factor for v in work[col]]
        for row in range(n):
            if row != col:
                factor = work[row][col]
                work[row] = [v - factor * w for v, w in zip(work[row], work[col])]
    return [row[n:] for row in work]


def rank(a):
    work = [row[:] for row in a]
    row = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(row, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        factor = work[row][col]
        work[row] = [v / factor for v in work[row]]
        for i in range(len(work)):
            if i != row:
                factor = work[i][col]
                work[i] = [v - factor * w for v, w in zip(work[i], work[row])]
        row += 1
        if row == len(work):
            break
    return row


def marked(q):
    n = len(q)
    t = [row[:] for row in q]
    t[0][1] = t[1][0] = ZERO
    r = [identity(n)[1], identity(n)[0]]
    b = matrix([[0, 0] for _ in range(n)])
    b[0][0], b[1][1] = q[0][1], q[1][0]
    return r, t, b


def parameters_and_ranks(q):
    r, t, b = marked(q)
    power, values, obs = identity(len(q)), [], []
    con = [[] for _ in q]
    for k in range(2 * len(q)):
        rb = multiply(r, power)
        pb = multiply(power, b)
        values.append(multiply(rb, b))
        if k < len(q):
            obs.extend(rb)
            con = [old + new for old, new in zip(con, pb)]
        power = multiply(power, t)
    return values, {"controllability": rank(con), "observability": rank(obs)}


def stationary(q):
    system = transpose(q)
    system[-1] = [ONE] * len(q)
    rhs = [[ZERO] for _ in q]
    rhs[-1] = [ONE]
    pi = [row[0] for row in multiply(inverse(system), rhs)]
    assert all(p > 0 for p in pi) and sum(pi, ZERO) == ONE
    assert multiply([pi], q) == [[ZERO] * len(q)]
    return pi


def validate(q):
    n = len(q)
    assert all(sum(row, ZERO) == ZERO for row in q)
    for i in range(n):
        for j in range(i + 1, n):
            assert q[i][j] >= 0 and q[j][i] >= 0
            assert bool(q[i][j]) == bool(q[j][i])
    reached, pending = {0}, [0]
    while pending:
        i = pending.pop()
        for j in range(n):
            if i != j and q[i][j] > 0 and j not in reached:
                reached.add(j)
                pending.append(j)
    assert len(reached) == n
    return stationary(q)


def entropy(q, pi):
    value = 0.0
    for i in range(len(q)):
        for j in range(i + 1, len(q)):
            if q[i][j]:
                forward, reverse = pi[i] * q[i][j], pi[j] * q[j][i]
                value += float(forward - reverse) * math.log(float(forward / reverse))
    return value


def theta(a, b):
    return matrix([[-11, 1, 2, 0, 8], [2, -20, 0, 7, 11],
                   [3, 0, -7, 4, 0], [0, 6, 5, -11, 0],
                   [a, b, 0, 0, -a-b]])


ALPHA, BETA = 9 - 2 * ROOT6, 9 + 2 * ROOT6
Z_ALPHA = matrix([[3 + ROOT6/2, 2*ROOT6],
                  [35*ROOT6/8, 21 - 7*ROOT6/2]])
Z_BETA = matrix([[3 - ROOT6/2, -2*ROOT6],
                 [-35*ROOT6/8, 21 + 7*ROOT6/2]])


def construct(a, b, redistribute=False):
    escape = a + b
    assert 0 < escape <= BETA
    zxx = Z_BETA[0][0]
    epsilon = None
    singleton_residue = Z_ALPHA
    x_mode = matrix([[8, Z_BETA[0][0]], [11, Z_BETA[1][0]]])
    y_mode = matrix([[a, b], [1, -2*ROOT6/zxx]])
    if redistribute:
        assert escape == ALPHA
        p = [Z_ALPHA[0][0], Z_ALPHA[1][0]]
        r = [ONE, Z_ALPHA[0][1]/Z_ALPHA[0][0]]
        epsilon = min(a, b/r[1])/2
        assert epsilon > 0
        remainder = [a-epsilon*r[0], b-epsilon*r[1]]
        assert all(v > 0 for v in remainder)
        x_mode = matrix([[p[0]+8*epsilon, Z_BETA[0][0]],
                         [p[1]+11*epsilon, Z_BETA[1][0]]])
        y_mode[0] = r
        singleton_residue = multiply(matrix([[8], [11]]), [remainder])
        redistributed = multiply([[row[0]] for row in x_mode], [r])
        original_shared = multiply(matrix([[8], [11]]), [[a, b]])
        assert all(redistributed[i][j]+singleton_residue[i][j]
                   == Z_ALPHA[i][j]+original_shared[i][j]
                   for i in range(2) for j in range(2))
    else:
        assert a > 35*ROOT6/88 and b > ROOT6/4
    t_lower = -y_mode[1][1]/y_mode[0][1]
    t_upper = x_mode[0][0]/x_mode[0][1]
    u_lower = y_mode[1][0]/y_mode[0][0]
    u_upper = x_mode[1][0]/(-x_mode[1][1])
    assert 0 < t_lower < t_upper and 0 < u_lower < u_upper
    t, u = (t_lower+t_upper)/2, (u_lower+u_upper)/2
    p = matrix([[1, 1], [-t, u]])
    h_mode = matrix([[-escape, 0], [0, -BETA]])
    p_inverse = inverse(p)
    x_raw = multiply(x_mode, p)
    y_raw = multiply(p_inverse, y_mode)
    h_raw = multiply(multiply(p_inverse, h_mode), p)
    assert all(v > 0 for rows in (x_raw, y_raw) for row in rows for v in row)
    assert h_raw[0][1] == u*(BETA-escape)/(t+u)
    assert h_raw[1][0] == t*(BETA-escape)/(t+u)
    d = [-row[0] for row in multiply(inverse(h_raw), multiply(y_raw, [[ONE], [ONE]]))]
    assert all(v > 0 for v in d)
    scaling = matrix([[d[0], 0], [0, d[1]]])
    scaling_inverse = inverse(scaling)
    x_pair = multiply(x_raw, scaling)
    y_pair = multiply(scaling_inverse, y_raw)
    h_pair = multiply(multiply(scaling_inverse, h_raw), scaling)
    assert multiply(h_pair, [[ONE], [ONE]]) == [[-sum(row, ZERO)] for row in y_pair]
    x_single = [sum(row, ZERO)/ALPHA for row in singleton_residue]
    y_single = [v/x_single[0] for v in singleton_residue[0]]
    assert sum(y_single, ZERO) == ALPHA
    assert multiply([[v] for v in x_single], [y_single]) == singleton_residue
    q = matrix([[-11, 1, *x_pair[0], x_single[0]],
                [2, -20, *x_pair[1], x_single[1]],
                [*y_pair[0], *h_pair[0], 0],
                [*y_pair[1], *h_pair[1], 0],
                [*y_single, 0, 0, -ALPHA]])
    assert all(q[i][j] > 0 and q[j][i] > 0 for i in (0, 1) for j in (2, 3, 4))
    assert (q[2][3] > 0) == (escape < BETA)
    assert (q[3][2] > 0) == (escape < BETA)
    return q, {"mode": "slow_residue_redistribution" if redistribute else "direct_residue_reassignment",
               "epsilon": epsilon, "singleton_residue": singleton_residue,
               "t_interval": [t_lower, t_upper], "u_interval": [u_lower, u_upper],
               "t": t, "u": u, "P": p, "normalizing_d": d,
               "normalized_P": multiply(p, scaling), "paired_hidden_block": h_pair}


def encode(value):
    if isinstance(value, Q6):
        return value.encoded()
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def run_case(name, a, b, expected_control, redistribute=False):
    original, candidate = theta(a, b), None
    original_pi = validate(original)
    candidate, construction = construct(a, b, redistribute)
    candidate_pi = validate(candidate)
    original_parameters, original_ranks = parameters_and_ranks(original)
    candidate_parameters, candidate_ranks = parameters_and_ranks(candidate)
    assert original_parameters == candidate_parameters
    expected = {"controllability": expected_control, "observability": 5}
    assert original_ranks == candidate_ranks == expected
    return {"name": name, "a": a, "b": b, "escape_sum": a+b,
            "source_generator": original, "candidate_generator": candidate,
            "source_stationary": original_pi, "candidate_stationary": candidate_pi,
            "construction": construction, "source_ranks": original_ranks,
            "candidate_ranks": candidate_ranks,
            "minimal_linear_dimension": expected_control,
            "equal_markov_parameters_orders": [0, 9],
            "exact_markov_parameters": original_parameters,
            "source_entropy_numeric": entropy(original, original_pi),
            "candidate_entropy_numeric": entropy(candidate, candidate_pi),
            "all_exact_checks_passed": True}


def main():
    assert ROOT6*ROOT6 == 6 and (ROOT6-2) > 0 and (ROOT6-Q6(Fraction(5, 2))) < 0
    assert (3 + ROOT6/2)*(3 - ROOT6/2) == Q6(Fraction(15, 2))
    assert rank(Z_ALPHA) == rank(Z_BETA) == 1
    cases = [run_case("theta_3_3", Q6(3), Q6(3), 5),
             run_case("slow_coincidence_minimal", Q6(1), ALPHA-1, 5),
             run_case("exceptional_nonminimal", 2*ROOT6-3, 12-4*ROOT6, 4),
             run_case("fast_coincidence", Q6(3), BETA-3, 5),
             run_case("slow_line_outside_direct_region", Q6(Fraction(1, 10)),
                      ALPHA-Q6(Fraction(1, 10)), 5, redistribute=True)]
    path = Path(__file__).resolve()
    result = {"executed_at": datetime.now(timezone.utc).isoformat(),
              "environment": {"python": platform.python_version(), "platform": platform.platform(),
                              "dependencies": "Python standard library only"},
              "script_sha256": {path.name: hashlib.sha256(path.read_bytes()).hexdigest()},
              "exact_scalar_encoding": "rational + sqrt6_coefficient * sqrt(6); coefficients are reduced rational strings",
              "inputs": "Five embedded deterministic algebraic parameter pairs; no external data or numerical search",
              "alpha": ALPHA, "beta": BETA, "Z_alpha": Z_ALPHA, "Z_beta": Z_BETA,
              "construction_domain": {"direct": "a+b <= beta, a > 35*sqrt(6)/88, b > sqrt(6)/4",
                                      "redistributed": "a+b=alpha, a,b>0; epsilon=min(a,b/r_y)/2"},
              "cases": cases,
              "scope": "Exact representative validation of the stated residue construction. No full theta-plane or topology classification and no novelty claim.",
              "all_checks_passed": True}
    destination = path.parents[1] / "outputs" / "theta-residue-checks.json"
    destination.write_text(json.dumps(encode(result), indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"executed_at": result["executed_at"], "all_checks_passed": True,
                      "cases": [{"name": c["name"], "ranks": c["candidate_ranks"],
                                 "source_entropy": c["source_entropy_numeric"],
                                 "candidate_entropy": c["candidate_entropy_numeric"]} for c in cases],
                      "output": str(destination)}, indent=2))


if __name__ == "__main__":
    main()
