"""Independent checks for the perturbed five-state construction.

Run: .venv/Scripts/python.exe -B -m unittest analysis.revision.test_continuation
"""
import json
from pathlib import Path
import unittest

import mpmath as mp
import numpy as np
import sympy as sp

from analysis.revision import continuation as c


class ContinuationTests(unittest.TestCase):
    def test_exact_interval_arithmetic_and_denominator_domain(self):
        from fractions import Fraction as F
        a=c.Interval(F(1,3),F(2,3))
        b=c.Interval(-2,-1)
        product=a*b
        self.assertLessEqual(product.lo,F(-4,3))
        self.assertGreaterEqual(product.hi,F(-1,3))
        reciprocal=1/b
        self.assertLessEqual(reciprocal.lo,-1)
        self.assertGreaterEqual(reciprocal.hi,F(-1,2))
        self.assertEqual((c.Interval(-2,3)**2).lo,0)
        self.assertEqual((c.Interval(-2,3)**2).hi,9)
        with self.assertRaises(AssertionError):
            _=a/c.Interval(-1,1)

    def test_generic_envelope_identity_independent_of_theta_constants(self):
        # Derive H directly from the extremal vertices with independent symbols.
        # This independently catches coefficient or substitution mistakes.
        A,B,L,R,m,k,t=sp.symbols("A B L R m k t",positive=True)
        a=k-1;J=a*m+k
        E=L*t*(J+a*t)
        D=R*m+(k*L+R)*t
        # Q=N/(a E) and c=k N/(a M), obtained by substituting epsilon=E/D.
        # Clear known nonzero denominators before expansion, avoiding generic
        # multivariate rational GCD computations with no scientific benefit.
        N=A*D+(R-A)*E
        M=A*D+R*E
        numerator=t*(L*E*(k*N+a*M*m)+N*M)
        denominator=E*(a*M*(m+t)+k*N)
        f0=A*R*m/L-B*J**2
        f1=A*(R/L+k-a*m)+L*J**2+R*J-2*B*J*a
        f2=a*(L*J+R-A*(1+L*k/R)-B*a)
        self.assertEqual(sp.expand(numerator*(J+a*t)**2
                                  -(B*(J+a*t)**2+f0+f1*t+f2*t*t)*denominator),0)

    def test_critical_triangle_matches_preserved_exact_path_witness(self):
        ctx=mp.mp.clone();ctx.dps=90
        z=c.critical(ctx,ctx.mpf(0))
        V,_=c.triangle(ctx,z,ctx.mpf(0));q,_=c.realize(ctx,z,ctx.mpf(0),V)
        old=json.loads((c.ROOT/"outputs/balanced-fold-checks.json").read_text())
        def decode(coeffs):
            value=ctx.mpf(0)
            for coef in coeffs:
                numerator,_,denominator=coef.partition("/")
                value=value*z+ctx.mpf(numerator)/ctx.mpf(denominator or 1)
            return value
        reference=ctx.matrix([[decode(coefs) for coefs in row] for row in old["target"]])
        permutation=[0,1,2,4,3]
        err=max(abs(q[permutation[i],permutation[j]]-reference[i,j]) for i in range(5) for j in range(5))
        self.assertLess(err,ctx.mpf("1e-80"))

    def test_offbalanced_root_slope_and_rate_data_agreement(self):
        ctx=mp.mp.clone();ctx.dps=80
        z=c.critical(ctx,ctx.mpf(0))
        Pprime=1408*z**3-9504*z**2-9288*z-11340
        exact=(20160*z+14112)/Pprime
        h=ctx.mpf("1e-20")
        central=(c.critical(ctx,h)-c.critical(ctx,-h))/(2*h)
        self.assertLess(abs(exact-central),ctx.mpf("1e-35"))
        for delta in map(ctx.mpf,("-.005","0",".005")):
            zc=c.critical(ctx,delta)
            self.assertTrue(ctx.mpf("10.55")<zc<ctx.mpf("10.565"))
            for dz,expected_count in ((ctx.mpf("-.001"),2),(ctx.mpf(0),1),(ctx.mpf(".001"),0)):
                p=c.numeric_parameters(ctx,zc+dz,delta)
                disc=p["f1"]**2-4*p["f0"]*p["f2"]
                self.assertEqual((2 if disc>ctx.mpf("1e-60") else 0 if disc<-ctx.mpf("1e-60") else 1),expected_count)
            V,_=c.triangle(ctx,zc,delta);q,_=c.realize(ctx,zc,delta,V)
            d=c.diagnostics(ctx,zc,delta,q,True)
            self.assertEqual(d["active_zero_jacobian_rank_at_relative_1e-10"],5)
            self.assertEqual(d["orbit_jacobian_rank_at_relative_1e-10"],6)

    def test_uniform_interval_certificate_has_strict_margins(self):
        result=c.exact_certificate()
        self.assertTrue(all(float(v["decimal_diagnostic"][0])>0 for v in result["strict_margins"].values()))


if __name__=="__main__":
    unittest.main()
