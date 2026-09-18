"""Exact covered-vertex inversion and floor/activity counterexample.
Run from root: python -B analysis/revision/graph_checks.py
Embedded rational inputs; no random seed or numerical tolerance.
"""
if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import sympy as s
n=4
Q=s.Matrix([[-6,1,2,3],[4,-10,0,6],[7,0,-16,9],[10,11,12,-33]])
marks=[(0,1),(1,0),(2,3),(3,2),(0,2),(2,0)]
E=s.zeros(n)
for i,j in marks: E[i,j]=Q[i,j]
T=Q-E
incoming=[(1,0),(0,1),(3,2),(2,3)]
outgoing=[(0,1),(1,0),(2,3),(3,2)]
D=s.diag(*[Q[i,j] for i,j in outgoing])
R=s.Matrix([list(s.eye(n)[j,:]) for i,j in incoming])
B=s.zeros(n,len(marks))
for k,(i,j) in enumerate(marks): B[i,k]=Q[i,j]
la,lb=s.Rational(2,3),s.Rational(7,2)
Ya=R*(la*s.eye(n)-T).inv()*B
Yb=R*(lb*s.eye(n)-T).inv()*B
cols=[marks.index(j) for j in outgoing]
Fa=Ya[:,cols]; Fb=Yb[:,cols]
Dr=(lb-la)*(Fb.inv()-Fa.inv()).inv()
Tr=la*s.eye(n)-Dr*Fa.inv()
Er=s.zeros(n)
for k,(i,j) in enumerate(marks):
    z=(la*s.eye(n)-Tr)*Ya[:,k]
    assert z==Q[i,j]*s.eye(n)[:,i]
    Er[i,j]=z[i]
assert Dr==D and Tr==T and Tr+Er==Q
c=s.symbols('c', positive=True)
C=s.Matrix([[-c-1,c,1],[1,-2,1],[1,1,-2]])
pi=s.Matrix([[1/(c+2),(2*c+1)/(3*(c+2)),s.Rational(1,3)]])
assert s.simplify(sum(pi)-1)==0 and (pi*C).applyfunc(s.simplify)==s.zeros(1,3)
K=sum(-pi[i]*C[i,i] for i in range(3))
J=pi[0]*C[0,1]-pi[1]*C[1,0]
assert s.simplify(K-3*(c+1)/(c+2))==0
assert s.simplify(J-(c-1)/(3*(c+2)))==0
print(sys.version.split()[0], s.__version__)
print('covered-graph exact inverse: PASS; floor/activity counterexample: PASS')

root=Path(__file__).resolve().parents[2]
result={"executed_at_utc":datetime.now(timezone.utc).isoformat(),
        "command":"python -B analysis/revision/graph_checks.py",
        "versions":{"python":sys.version.split()[0],"sympy":s.__version__},
        "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "inputs":"embedded rational four-state covered graph with redundant observed marks; symbolic c>=1 example",
        "arithmetic":"exact SymPy rational and symbolic; no tolerances or random seeds",
        "checks":{"covered_graph_inverse":True,"stationary_floor_activity_counterexample":True},
        "scope":"Finite checks supplement conventional general proofs; not formal verification."}
(root/'outputs/revision/graph-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
