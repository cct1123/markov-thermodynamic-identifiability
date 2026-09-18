"""Check the stronger whole-interval bounds printed in the manuscript table.

Run from repository root with assertions enabled:
    .venv/Scripts/python.exe -B manuscript/scripts/check_table_bounds.py
The historical checker is replayed with shifted polynomial interval evaluation
and intercepted writes. No historical output is overwritten.
"""
from contextlib import redirect_stdout
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import sys
from unittest.mock import patch

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]


def main():
    if not __debug__:
        raise RuntimeError("Assertions must be enabled")
    os.chdir(ROOT)
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(ROOT / "analysis"))
    import check_balanced_cone_sufficiency as checker
    original = checker.polynomial_interval
    captured = {}

    def shifted(expr, z, zi, rho, ri):
        base = sp.Rational(zi[0].numerator, zi[0].denominator)
        return original(sp.expand(expr.subs(z, z+base)), z,
                        (Fraction(0), zi[1]-zi[0]), rho, ri)

    def intercept(path, data, *args, **kwargs):
        captured.update(json.loads(data))
        return len(data)

    transcript = io.StringIO()
    with patch.object(checker, "polynomial_interval", shifted), \
            patch.object(Path, "write_text", intercept), redirect_stdout(transcript):
        checker.main()
    printed_lower_bounds = {
        "t_positive": "18/100", "epsilon_positive": "5/100",
        "one_minus_epsilon_positive": "9/10", "right_abscissa_minus_one": "1",
        "bottom_left_output": "6/10", "right_right_output": "170",
        "input_B_above_left_lower": "8", "input_A_below_upper": "100",
        "left_origin_margin_via_tangency": "3/100",
        "right_origin_margin_via_tangency": "120",
        "bottom_left_invariance_via_tangency": "7/100",
        "bottom_right_invariance_via_tangency": "120",
    }
    for key, bound in printed_lower_bounds.items():
        exact_lower = Fraction(captured["strict_geometric_margins"][key]["rational_endpoints"][0])
        assert exact_lower > Fraction(bound), (key, exact_lower, bound)
    sources = [Path(__file__), ROOT / "analysis/check_balanced_cone_sufficiency.py",
               ROOT / "analysis/check_balanced_cone_bound.py"]
    result = {"executed_at_utc": datetime.now(timezone.utc).isoformat(),
              "command_from_root": ".venv/Scripts/python.exe -B manuscript/scripts/check_table_bounds.py",
              "environment": {"python": platform.python_version(), "sympy": sp.__version__},
              "source_sha256": {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
              "method": "Exact outward rational interval arithmetic after z=21/2+xi, with 0<=xi<=0.05714966867 and the historical rational sqrt(6) enclosure",
              "printed_rational_lower_bounds": printed_lower_bounds,
              "captured_shifted_checker_result": captured,
              "all_12_printed_bounds_certified": True,
              "limitation": "Checks the displayed finite rational interval bounds only; global support and strict-perturbation proofs remain conventional."}
    path = ROOT / "manuscript/supplementary/table-bound-checks.json"
    path.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print("PASS all 12 printed lower bounds; historical writes intercepted")


if __name__ == "__main__":
    main()
