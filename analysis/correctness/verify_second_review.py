"""Bounded second-review verification; preserve accepted historical evidence.

Run from root: .venv/Scripts/python.exe -B analysis/correctness/verify_second_review.py
Uses the installed Python environment and cached tmp/tectonic/tectonic.exe.
The separate verify_review_calculations.py handles the numerical review fields.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'outputs/supplied-verification-2026-09-19/verification.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if not __debug__:
        raise SystemExit('Assertions must be enabled.')
    protected = [ROOT/'PROJECT.md', ROOT/'AGENTS.md']
    protected += sorted((ROOT/'analysis').glob('*.json'))
    protected += sorted((ROOT/'outputs').glob('*.json'))
    protected += sorted((ROOT/'evidence/supplied/2026-09-18').glob('*'))
    protected += sorted((ROOT/'evidence/supplied/2026-09-19').glob('*'))
    before = {p.relative_to(ROOT).as_posix(): sha(p) for p in protected if p.is_file()}
    report = {
        'started_at_utc': datetime.now(timezone.utc).isoformat(),
        'command': '.venv/Scripts/python.exe -B analysis/correctness/verify_second_review.py',
        'python': platform.python_version(), 'script_sha256': sha(Path(__file__)),
        'protected_before': before, 'jobs': [], 'all_checks_passed': False,
        'scope': 'Second-review regression, exact replay, manuscript build and source validation. '
                 'No new Monte Carlo campaign, formal proof, or priority certification.',
    }
    jobs = [
        ('supplied standalone script', ['evidence/supplied/2026-09-18/two_laplace_counterexample.py']),
        ('41 regression and scientific tests', ['-m', 'unittest', 'analysis.capabilities.test_tools',
         'analysis.revision.test_inference', 'analysis.revision.test_continuation',
         'analysis.correctness.test_laplace_two', 'analysis.correctness.test_laplace_entropy',
         'analysis.correctness.test_validation', 'analysis.correctness.test_entrypoints', '-v']),
        ('standalone driver and 15 historical scientific payload comparisons',
         ['manuscript/scripts/reproduce.py']),
        ('manuscript compilation', ['manuscript/scripts/build.py', '--tectonic',
         'tmp/tectonic/tectonic.exe', '--offline']),
        ('source and receipt validation', ['manuscript/scripts/validate.py']),
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    for label, arguments in jobs:
        command = [sys.executable, '-B', *arguments]
        print(label, flush=True)
        start = time.perf_counter()
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, errors='replace')
        report['jobs'].append({'label': label, 'command': command,
                              'seconds': time.perf_counter()-start, 'returncode': result.returncode,
                              'stdout': result.stdout, 'stderr': result.stderr})
        OUT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
        if result.returncode:
            print(result.stdout)
            print(result.stderr)
            raise SystemExit(result.returncode)
        print('  passed', flush=True)
    after = {name: sha(ROOT/name) for name in before}
    assert after == before, 'Protected historical or supplied evidence changed'
    report.update(all_checks_passed=True, protected_unchanged=True,
                  completed_at_utc=datetime.now(timezone.utc).isoformat())
    tracked = ['manuscript/scripts/reproduce.py', 'analysis/correctness/test_validation.py',
               'manuscript/supplementary/conditioning.tex', 'manuscript/supplementary/proofs.tex',
               'manuscript/supplementary/literature-comparison.tex', 'manuscript/main.pdf',
               'manuscript/supplementary/computational-results.json',
               'manuscript/supplementary/build-report.json',
               'manuscript/supplementary/package-validation.json']
    report['verified_file_sha256'] = {name: sha(ROOT/name) for name in tracked}
    OUT.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('All bounded review jobs passed; ' + OUT.relative_to(ROOT).as_posix())


if __name__ == '__main__':
    main()
