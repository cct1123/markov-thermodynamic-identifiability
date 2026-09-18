"""Replay the inspected supplied leaf example and reconcile matrix conventions.

Run from root: python -B analysis/correctness/replay_supplied_review.py
The other supplied JSON claims remain attributed results, not replayed evidence.
"""
if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

from contextlib import redirect_stdout
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import platform
import runpy
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from analysis.correctness import laplace_two as audit


def main():
    supplied = ROOT/'evidence/supplied/2026-09-18'
    manifest = json.loads((supplied/'manifest.json').read_text(encoding='utf-8'))
    for name, record in manifest['files'].items():
        assert hashlib.sha256((supplied/name).read_bytes()).hexdigest() == record['sha256'], name
    source = supplied/'two_laplace_counterexample.py'
    # This fixed source was inspected before integration; no commands or code
    # are taken from the accompanying JSON review assertions.
    namespace = runpy.run_path(str(source))
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        namespace['main']()
    summary = json.loads((supplied/'independent_checks.json').read_text(encoding='utf-8'))
    expected = summary['two_laplace_counterexample']
    cases = ((1, 1, 1, 1, 0, 0),
             (sp.Rational(6, 5), 1, sp.Rational(12, 5), 2, 0, 0))
    checks = []
    for index, rates in enumerate(cases):
        q = audit.generator(rates)
        assert str(q) == expected['Q_A' if index == 0 else 'Q_B']
        for point in (1, 2, 3):
            actual = namespace['reordered_transform'](q, sp.Integer(point))
            assert actual == audit.P*audit.transform(rates, point)
            key = f'F_{point}' if point != 3 else ('F_A_3' if index == 0 else 'F_B_3')
            assert str(actual) == expected[key], key
            checks.append({'model': index+1, 'lambda': point, 'F': str(actual)})
    result = {
        'executed_at_utc': datetime.now(timezone.utc).isoformat(),
        'command': 'python -B analysis/correctness/replay_supplied_review.py',
        'environment': {'python': platform.python_version(), 'sympy': sp.__version__},
        'wrapper_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'supplied_file_hashes': {name: record['sha256'] for name, record in manifest['files'].items()},
        'supplied_script_stdout': stdout.getvalue(),
        'exact_matrix_checks': checks,
        'convention': 'Supplied F = P times manuscript Psi_hat. Tree F off-diagonals vanish; Psi_hat off-diagonals do not.',
        'other_JSON_fields': 'Attributed user-supplied review results; not reproduced by this wrapper. In particular endpoint decimals are not interval certificates.',
        'entropy_status': 'Conventional support/detailed-balance proof in the manuscript, supported by test_laplace_entropy.py; not inferred from numerical endpoint checks.',
        'all_checks_passed': True,
    }
    destination = ROOT/'outputs/laplace-review-2026-09-18/supplied-replay.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('Supplied script and all six exact matrix comparisons passed; original hashes unchanged.')


if __name__ == '__main__':
    main()
