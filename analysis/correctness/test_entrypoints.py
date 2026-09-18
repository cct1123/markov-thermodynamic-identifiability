"""Check that proof entrypoints cannot claim success with assertions disabled.

Each CLI runs from an isolated temporary copy, so a guard regression cannot
overwrite an accepted receipt or manuscript figure in the research workspace.
Run: python -B -m unittest analysis.correctness.test_entrypoints -v
"""

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
ENTRYPOINTS = (
    "analysis/revision/continuation.py",
    "analysis/revision/rare_event.py",
    "analysis/revision/graph_checks.py",
    "analysis/revision/replay_independent.py",
    "analysis/revision/audit_repository.py",
    "analysis/correctness/global_independent.py",
    "analysis/correctness/laplace_two.py",
    "analysis/correctness/mechanism.py",
)
GUARD_MESSAGE = "Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE."


class EntrypointTests(unittest.TestCase):
    def check_optimized_commands(self, flags, optimize_env):
        for relative in ENTRYPOINTS:
            with self.subTest(entrypoint=relative), tempfile.TemporaryDirectory() as directory:
                temporary = Path(directory)
                script = temporary / relative
                script.parent.mkdir(parents=True)
                original = (ROOT / relative).read_bytes()
                script.write_bytes(original)
                env = os.environ.copy()
                env.pop("PYTHONOPTIMIZE", None)
                if optimize_env is not None:
                    env["PYTHONOPTIMIZE"] = optimize_env
                env["MPLCONFIGDIR"] = str(temporary / "matplotlib-cache")
                result = subprocess.run(
                    [sys.executable, *flags, "-B", str(script)], cwd=temporary,
                    env=env, capture_output=True, text=True, timeout=15,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stderr.strip(), GUARD_MESSAGE)
                self.assertEqual(result.stdout, "")
                self.assertEqual(script.read_bytes(), original)
                self.assertEqual(
                    {path.relative_to(temporary).as_posix()
                     for path in temporary.rglob("*") if path.is_file()},
                    {relative},
                    "An optimized checker wrote files before rejecting disabled assertions",
                )

    def test_python_optimization_flag_rejected_before_output_writes(self):
        self.check_optimized_commands(["-O"], None)

    def test_pythonoptimize_environment_rejected_before_output_writes(self):
        self.check_optimized_commands([], "1")


if __name__ == "__main__":
    unittest.main()
