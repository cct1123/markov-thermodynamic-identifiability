"""Reproduce exact checks, revision experiments, tests, and publication figures.

python -B reproduce_all.py
python -B reproduce_all.py --build --tectonic /path/to/tectonic --offline

Use the scientific Python environment with assertions enabled. Default simulation:
900 trajectories (100 per model/event count). No installation or network requests.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build', action='store_true', help='Also compile and validate manuscript')
    parser.add_argument('--tectonic', help='Optional compiler path')
    parser.add_argument('--offline', action='store_true', help='Use cached TeX resources only')
    args = parser.parse_args()
    if not __debug__:
        raise SystemExit('Assertions must be enabled; do not use python -O.')
    if (args.tectonic or args.offline) and not args.build:
        parser.error('--tectonic/--offline require --build')
    jobs = [
        ('exact historical proof support', ['manuscript/scripts/reproduce.py']),
        ('exact appendix interval bounds', ['manuscript/scripts/check_table_bounds.py']),
        ('independent exact and interval audit', ['analysis/revision/replay_independent.py']),
        ('global coverage algebra and protected endpoint replays', ['analysis/correctness/global_independent.py']),
        ('exact two-point inverse and full-matrix counterexamples', ['-m','analysis.correctness.laplace_two']),
        ('complete-support exact ambiguity and entropy limit', ['analysis/correctness/mechanism.py']),
        ('exact rare-rate identities and high-precision checks', ['analysis/revision/rare_event.py']),
        ('exact graph inverse and physical-prior counterexample', ['analysis/revision/graph_checks.py']),
        ('exact local unfolding and numerical continuation', ['analysis/revision/continuation.py']),
        ('illustrative conditioning and 900 finite trajectories', ['-m','analysis.revision.inference','--replicates','100']),
        ('unit and independent numerical checks', ['-m','unittest','analysis.capabilities.test_tools',
          'analysis.revision.test_inference','analysis.revision.test_continuation',
          'analysis.correctness.test_laplace_two','analysis.correctness.test_validation',
          'analysis.correctness.test_entrypoints','-v']),
    ]
    if args.build:
        build = ['manuscript/scripts/build.py']
        if args.tectonic:
            build += ['--tectonic',args.tectonic]
        if args.offline:
            build += ['--offline']
        jobs += [('manuscript compilation',build),('source and build validation',['manuscript/scripts/validate.py'])]
    report = {'started_at_utc':datetime.now(timezone.utc).isoformat(),
              'python':platform.python_version(), 'command':['python','-B','reproduce_all.py',*sys.argv[1:]],
              'proof_status':'Conventional proofs with exact support; numerical experiments separately labeled.',
              'jobs':[], 'all_passed':False,
              'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    destination = ROOT/'outputs/correctness-2026-09-15/reproduction.json'
    destination.parent.mkdir(parents=True,exist_ok=True)
    for label, arguments in jobs:
        command = [sys.executable,'-B',*arguments]
        print(label,flush=True)
        start = time.perf_counter()
        result = subprocess.run(command,cwd=ROOT,capture_output=True,text=True,errors='replace')
        report['jobs'].append({'scope':label,'command':command,'seconds':time.perf_counter()-start,
                               'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
        destination.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        if result.returncode:
            print(result.stdout)
            print(result.stderr)
            raise SystemExit(result.returncode)
        print('  passed',flush=True)
    files = [ROOT/'PROJECT.md', ROOT/'reproduce_all.py']
    files += sorted((ROOT/'analysis/revision').glob('*.py'))
    files += sorted((ROOT/'analysis/correctness').glob('*.py'))
    files += sorted((ROOT/'manuscript/figures').glob('*.pdf'))
    files += [ROOT/'outputs/revision/statistics.json', ROOT/'outputs/revision/continuation.json',
              ROOT/'outputs/revision/rare-event.json', ROOT/'outputs/revision/graph-checks.json']
    files += [ROOT/'outputs/correctness-2026-09-15'/name for name in
              ('global-independent.json','laplace-two.json','mechanism.json')]
    if args.build:
        files += [ROOT/'manuscript/main.pdf']
    report.update(all_passed=True,finished_at_utc=datetime.now(timezone.utc).isoformat(),
                  output_sha256={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    destination.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print('All requested checks passed; outputs/correctness-2026-09-15/reproduction.json',flush=True)


if __name__=='__main__':
    main()
