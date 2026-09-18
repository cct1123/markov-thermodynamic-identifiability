"""Read-only package/source validation; writes only its validation report."""
import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
M = ROOT / 'manuscript'

def main():
    tex_files = [M/'main.tex', *sorted((M/'supplementary').glob('*.tex'))]
    sources = '\n'.join(p.read_text(encoding='utf-8') for p in tex_files)
    labels = re.findall(r'\\label\{([^}]+)\}', sources)
    assert len(labels) == len(set(labels)), 'duplicate LaTeX labels'
    references = re.findall(r'\\(?:eqref|ref)\{([^}]+)\}', sources)
    assert not set(references)-set(labels), set(references)-set(labels)
    bib = (M/'references.bib').read_text(encoding='utf-8')
    keys = re.findall(r'@(?:article|book|incollection|inproceedings|misc)\{([^,]+),', bib, re.I)
    assert len(keys) == len(set(keys))
    citations = {key.strip() for group in re.findall(r'\\cite\{([^}]+)\}', sources) for key in group.split(',')}
    assert citations == set(keys), {'unused': set(keys)-citations, 'missing': citations-set(keys)}
    for path in re.findall(r'\\input\{([^}]+)\}', sources):
        assert (M/path).is_file(), path
    for path in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', sources):
        assert (M/path).is_file(), path
    for p in tex_files:
        assert not [c for c in p.read_bytes() if c<32 and c not in (9,10,13)], p
    assert not re.search(r'TODO|FIXME|citation needed|\\cite\{\s*\}', sources, re.I)
    parsed = []
    for directory in [ROOT/'analysis', M/'scripts']:
        for p in directory.rglob('*.py'):
            if '__pycache__' not in p.parts:
                ast.parse(p.read_text(encoding='utf-8-sig'), filename=str(p))
                parsed.append(p.relative_to(ROOT).as_posix())
    build = json.loads((M/'supplementary/build-report.json').read_text())
    for p, expected in build['sha256'].items():
        assert hashlib.sha256((M/p).read_bytes()).hexdigest() == expected, p
    assert all(build['validation'].values())
    manifest = json.loads((M/'supplementary/computational-results.json').read_text())
    # The computational manifest is preserved in full; its assertions were
    # executed by reproduce.py. This validator only checks its source identity.
    manuscript_md = [M/'README.md', ROOT/'analysis/manuscript-audit.md',
                     ROOT/'outputs/PUBLICATION-READINESS.md']
    links = []
    outer_archive_links = []
    for p in manuscript_md:
        for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
            if re.match(r'https?://|mailto:|#', target):
                continue
            target = target.split('#')[0]
            resolved = (p.parent/target).resolve()
            # A delivered ZIP cannot contain itself. In a fresh extraction,
            # permit only that specific link when the package manifest exists.
            if (resolved == ROOT/'outputs/manuscript-package.zip'
                    and not resolved.exists() and (ROOT/'PACKAGE-MANIFEST.json').is_file()):
                outer_archive_links.append(target)
                continue
            assert resolved.exists(), (p, target)
            links.append(target)
    report = {'executed_at_utc': datetime.now(timezone.utc).isoformat(),
              'latex_labels': len(labels), 'latex_references': len(references),
              'verified_bibliography_entries_all_cited': len(keys),
              'python_sources_parsed': parsed, 'local_document_links_checked': len(links),
              'outer_archive_links_recognized_in_extraction': outer_archive_links,
              'build_hashes_match': True, 'all_checks_passed': True,
              'scope': 'Source/package validation, not an independent proof or web-source verification.'}
    (M/'supplementary/package-validation.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='python_sources_parsed'},indent=2))

if __name__ == '__main__':
    main()
