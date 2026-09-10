"""Seeded discovery-only continuation of complete theta(z,z) realizations.

Run: .venv/Scripts/python.exe -B analysis/probe_balanced_boundary.py
All-time equivalence is imposed by row-normalized hidden similarity, but float
positivity and optimizer outcomes remain candidates until exact verification.
This searches complete support within bounded coordinates, not every model.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import warnings

import numpy as np
import scipy
from scipy.optimize import linprog, minimize


POSITIONS = [(i,j) for i in range(3) for j in range(3) if i != j]
OFF = ~np.eye(5,dtype=bool)


def theta(z):
    return np.array([[-11,1,2,0,8],[2,-20,0,7,11],[3,0,-7,4,0],
                     [0,6,5,-11,0],[z,z,0,0,-2*z]],dtype=float)


def similarity(parameters):
    u = np.eye(3)
    for value,(i,j) in zip(parameters,POSITIONS):
        u[i,j] = value
        u[i,i] -= value
    return u


def transform(parameters,z):
    u = similarity(parameters)
    s = np.eye(5)
    s[2:,2:] = u
    return np.linalg.solve(s,theta(z)@s),u


def opening_seed(z=10):
    q = theta(z)
    missing = [(i,j) for i in range(5) for j in range(5) if i != j and q[i,j] == 0]
    columns = []
    for i,j in POSITIONS:
        k = np.zeros((5,5))
        k[i+2,j+2],k[i+2,i+2] = 1,-1
        derivative = q@k-k@q
        columns.append([derivative[i,j] for i,j in missing])
    a = np.array(columns).T
    result = linprog(np.r_[np.zeros(6),-1],A_ub=np.column_stack([-a,np.ones(len(a))]),
                     b_ub=np.zeros(len(a)),bounds=[(-1,1)]*6+[(0,None)],method="highs")
    if not result.success or result.x[-1] <= 0:
        raise RuntimeError("known strict-opening control did not open")
    for epsilon in [0.1,0.01,0.001,0.0001]:
        p = epsilon*result.x[:6]
        target,u = transform(p,z)
        if np.min(target[OFF]) > 1e-7:
            return np.r_[p,z]
    raise RuntimeError("known control has no checked small step")


def main():
    rng = np.random.default_rng(20260910)
    base = opening_seed()
    starts = [base]
    for scale in (0.01,0.1,0.5):
        starts += [base+np.r_[rng.normal(0,scale,6),0] for _ in range(4)]
    outcomes = []
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        for floor in [1e-5,1e-7]:
            def constraints(p):
                try:
                    q,u = transform(p[:6],p[6])
                except np.linalg.LinAlgError:
                    return np.full(21,-1e10)
                return np.r_[q[OFF]-floor,np.linalg.det(u)-1e-5]
            for start in starts:
                result = minimize(lambda p:-p[6],start,method="SLSQP",
                                  bounds=[(-5,5)]*6+[(7,40)],
                                  constraints={"type":"ineq","fun":constraints},
                                  options={"maxiter":1500,"ftol":1e-11})
                q,u = transform(result.x[:6],result.x[6])
                outcomes.append({"floor":floor,"success":bool(result.success),"message":str(result.message),
                                 "z":float(result.x[6]),"parameters":result.x[:6].tolist(),
                                 "minimum_offdiagonal":float(np.min(q[OFF])),
                                 "determinant":float(np.linalg.det(u)),"condition":float(np.linalg.cond(u)),
                                 "row_sum_residual":float(np.max(np.abs(q.sum(axis=1)))),
                                 "q":q.tolist()})
    output = {"kind":"numerical discovery, no nonexistence certificate",
              "executed_at_utc":datetime.now(timezone.utc).isoformat(),
              "python":platform.python_version(),"numpy":np.__version__,"scipy":scipy.__version__,
              "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "command":".venv/Scripts/python.exe -B analysis/probe_balanced_boundary.py",
              "seed":20260910,"coordinate_bounds":[-5,5],"z_bounds":[7,40],
              "determinant_floor":1e-5,"floors":[1e-5,1e-7],"maxiter":1500,"ftol":1e-11,
              "initial_seed":base.tolist(),"outcomes":outcomes,
              "warnings":sorted(set(str(w.message) for w in caught))}
    Path('analysis/balanced-boundary-probe.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    good = [row for row in outcomes if row['minimum_offdiagonal'] >= 0.5*row['floor'] and row['determinant']>0]
    print(json.dumps({"best":max(good,key=lambda r:r['z']) if good else None,
                      "runs":len(outcomes),"feasible":len(good)},indent=2))


if __name__ == '__main__':
    main()
