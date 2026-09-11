"""Compile the manuscript with Tectonic or a standard pdfLaTeX/BibTeX toolchain."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
MANUSCRIPT = ROOT / 'manuscript'
BUNDLE = 'https://relay.fullyjustified.net/default_bundle_v33.tar'

def main():
    parser = argparse.ArgumentParser(__doc__)
    parser.add_argument('--tectonic', help='Path to a Tectonic executable')
    parser.add_argument('--offline', action='store_true', help='Tectonic cached resources only')
    args = parser.parse_args()
    executable = args.tectonic or shutil.which('tectonic')
    environment = os.environ.copy()
    environment['SOURCE_DATE_EPOCH'] = '1789084800'
    if executable:
        executable = str(Path(executable).resolve())
        commands = [[executable, '--bundle', BUNDLE, '--keep-logs', '--keep-intermediates',
                     *(['--only-cached'] if args.offline else []), 'main.tex']]
        version = subprocess.check_output([executable, '--version'], text=True).strip()
    else:
        latex, bib = shutil.which('pdflatex'), shutil.which('bibtex')
        if not latex or not bib:
            raise SystemExit('Install Tectonic or pdfLaTeX and BibTeX; see manuscript/README.md.')
        command = [latex, '-interaction=nonstopmode', '-halt-on-error', 'main.tex']
        commands = [command, [bib, 'main'], command, command]
        version = subprocess.check_output([latex, '--version'], text=True).splitlines()[0]
    results = []
    for command in commands:
        result = subprocess.run(command, cwd=MANUSCRIPT, env=environment,
                                capture_output=True, text=True, errors='replace')
        results.append({'command': command, 'returncode': result.returncode,
                        'stdout': result.stdout, 'stderr': result.stderr})
        if result.returncode:
            print(result.stdout)
            print(result.stderr)
            raise SystemExit(result.returncode)
    log = (MANUSCRIPT / 'main.log').read_text(errors='replace')
    forbidden = ['Undefined control sequence', 'undefined references',
                 'undefined citations', 'multiply defined', 'Overfull \\hbox',
                 'Overfull \\vbox']
    for token in forbidden:
        if token.lower() in log.lower():
            raise SystemExit('Unresolved build problem: ' + token)
    tracked = ['main.tex', 'references.bib', 'supplementary/proofs.tex',
               'figures/balanced-fiber.pdf', 'figures/three-state-instability.pdf', 'main.pdf']
    report = {'executed_at_utc': datetime.now(timezone.utc).isoformat(),
              'engine': version, 'bundle': BUNDLE if executable else None,
              'source_date_epoch': environment['SOURCE_DATE_EPOCH'],
              'commands': results,
              'sha256': {p: hashlib.sha256((MANUSCRIPT/p).read_bytes()).hexdigest() for p in tracked},
              'validation': {'compiled': True, 'no_undefined_references_or_citations': True,
                             'no_overfull_boxes': True},
              'log_warnings': [line for line in log.splitlines() if 'Warning' in line or 'Underfull' in line]}
    destination = MANUSCRIPT / 'supplementary/build-report.json'
    destination.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('Compiled manuscript/main.pdf; build provenance:', destination.relative_to(ROOT))

if __name__ == '__main__':
    main()
