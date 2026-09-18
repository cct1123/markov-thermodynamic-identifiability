"""Read/inventory repository payloads and verify preserved theorem/output content.

Structural coverage and hashes do not constitute a semantic proof review.
Run from root: python -B analysis/revision/audit_repository.py
"""
import ast
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[2]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    names=subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT).decode().split('\0')
    inventory=[]
    parsed=0
    for name in sorted(set(names)-{''}):
        path=ROOT/name
        if not path.is_file() or name=='outputs/revision/repository-audit.json':
            continue
        data=path.read_bytes()
        kind='binary/inventory'
        if path.suffix=='.py':
            ast.parse(data.decode('utf-8-sig'),filename=name)
            parsed+=1; kind='Python AST parsed'
        elif path.suffix=='.json':
            json.loads(data.decode('utf-8-sig')); kind='JSON parsed'
        elif path.suffix in {'.md','.tex','.bib','.txt','.toml','.lean','.html','.js','.css'}:
            data.decode('utf-8-sig'); kind='text decoded/inventoried'
        inventory.append({'path':name,'bytes':len(data),'sha256':sha(data),'structural_check':kind})
    base=(ROOT/'outputs/revision/baseline/main.tex').read_text(encoding='utf-8')
    current=(ROOT/'manuscript/main.tex').read_text(encoding='utf-8')
    blocks=re.findall(r'\\begin\{(theorem|proposition|lemma|corollary)\}(.*?)\\end\{\1\}',base,re.S)
    preserved=[]
    for kind,body in blocks:
        label=re.search(r'\\label\{([^}]+)\}',body)
        assert body in current, label.group(1) if label else body[:50]
        preserved.append(label.group(1) if label else kind)
    original=(ROOT/'outputs/revision/baseline/proofs.tex').read_text(encoding='utf-8')
    assert (ROOT/'manuscript/supplementary/proofs.tex').read_text(encoding='utf-8').startswith(original)
    manifest=json.loads((ROOT/'manuscript/supplementary/computational-results.json').read_text())
    protected=manifest['historical_output_hashes']
    for name,expected in protected.items():
        assert sha((ROOT/name).read_bytes())==expected,name
        # Accepted scientific files must also agree with the committed original.
        committed=subprocess.check_output(['git','show','HEAD:'+name],cwd=ROOT)
        assert committed.decode('utf-8-sig').replace('\r\n','\n') == (ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n'),name
    for name in ('PROJECT.md','AGENTS.md'):
        committed=subprocess.check_output(['git','show','HEAD:'+name],cwd=ROOT).decode('utf-8-sig').replace('\r\n','\n')
        assert (ROOT/name).read_text(encoding='utf-8-sig').replace('\r\n','\n')==committed,name
    result={'executed_at_utc':datetime.now(timezone.utc).isoformat(),
            'command':'python -B analysis/revision/audit_repository.py',
            'scope':'Complete tracked/unignored payload inventory and structural parsing; semantic review coverage is in AUDIT.md.',
            'original_theorem_statements_preserved':preserved,
            'original_proof_appendices_preserved_as_prefix':True,
            'protected_accepted_json_count':len(protected), 'protected_json_match_HEAD_normalized_line_endings':True,
            'human_brief_and_instructions_unchanged':True,'python_sources_parsed':parsed,
            'files':inventory,'all_checks_passed':True}
    out=ROOT/'outputs/revision/repository-audit.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2))


if __name__=='__main__':
    main()
