"""Replay the existing independent checker without replacing its accepted output.

Run from the repository root: python -B analysis/revision/replay_independent.py
Only the checker receipt is redirected; its original code and inputs are unchanged.
"""
if not __debug__:
    raise SystemExit("Assertions must be enabled; do not use python -O or PYTHONOPTIMIZE.")

import contextlib
import hashlib
import io
import json
from pathlib import Path
import runpy
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'analysis/manuscript-math-independent-check.py'
HISTORICAL = ROOT/'outputs/manuscript-math-independent-checks.json'
OUTPUT = ROOT/'outputs/revision/manuscript-math-independent-checks.json'


def differing_fields(current, historical):
    """Compare the complete payload, including missing or newly added fields."""
    keys = (current.keys() | historical.keys()) - {'time_utc'}
    return sorted(key for key in keys
                  if key not in current or key not in historical
                  or current[key] != historical[key])


def main():
    before = HISTORICAL.read_bytes()
    captured = []

    def capture(path, data, *args, **kwargs):
        assert path.resolve() == HISTORICAL, path
        captured.append(json.loads(data))
        return len(data)

    with patch.object(Path, 'write_text', capture), contextlib.redirect_stdout(io.StringIO()):
        runpy.run_path(str(SOURCE), run_name='__main__')
    assert len(captured) == 1 and captured[0]['all_checks_passed']
    result = captured[0]
    old = json.loads(before)
    differences = differing_fields(result, old)
    assert not differences, differences
    assert HISTORICAL.read_bytes() == before
    result['replay'] = {
        'command': 'python -B analysis/revision/replay_independent.py',
        'wrapper_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'historical_output_sha256': hashlib.sha256(before).hexdigest(),
        'historical_output_unchanged': True,
        'scientific_payload_identical': True,
        'method': 'Execute the unchanged checker with only its receipt write intercepted; compare every output field except execution time against the accepted receipt.'}
    OUTPUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('Independent exact/interval audit passed; historical receipt preserved; outputs/revision/manuscript-math-independent-checks.json')


if __name__ == '__main__':
    main()
