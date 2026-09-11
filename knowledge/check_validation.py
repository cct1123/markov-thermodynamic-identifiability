"""Adversarial checks that the atlas validator catches consequential map mistakes."""
import copy
import hashlib
import json
from pathlib import Path
from validate import validate

K=Path(__file__).resolve().parent
g=json.loads((K/'graph.json').read_text(encoding='utf-8'))
cases=[]
def run(name,change,predicate):
    altered=copy.deepcopy(g);change(altered);out=validate(altered,check_sources=False)
    assert predicate(out), (name,out)
    cases.append(dict(name=name,detected=True))
def node(x,id):return next(n for n in x['nodes'] if n['id']==id)
run('Unsupported theorem',lambda x:node(x,'theorem_t3').update(evidence=[]),lambda o:any(w['node']=='theorem_t3' and 'evidence' in w['message'] for w in o['warnings']))
run('Missing theorem assumptions',lambda x:node(x,'theorem_t3').update(assumptions=[]),lambda o:any(w['node']=='theorem_t3' and 'assumptions' in w['message'] for w in o['warnings']))
run('Falsified statement used as proof',lambda x:x['edges'].append(dict(source='hypothesis_first_order_threshold',target='theorem_t3',relation='supports',explanation='Intentional adversarial corruption.')),lambda o:any('rejected statement supports' in e for e in o['errors']))
run('Missing novelty comparison',lambda x:node(x,'theorem_t3')['novelty'].update(comparisons=[]),lambda o:any(w['code']=='novelty_comparison_gap' and w['node']=='theorem_t3' for w in o['warnings']))
run('Metadata promoted to independent science',lambda x:node(x,'theorem_t3').update(independent_verification=['check_legacy_saved']),lambda o:any(w['code']=='metadata_is_not_verification' for w in o['warnings']))
run('Unresolved live contradiction',lambda x:x['edges'].append(dict(source='theorem_t3',target='theorem_t6',relation='contradicts',explanation='Intentional adversarial corruption.')),lambda o:any(w['code']=='unresolved_contradiction' for w in o['warnings']))
run('Orphan evidence',lambda x:x['edges'].__setitem__(slice(None),[e for e in x['edges'] if 'search_balanced' not in (e['source'],e['target'])]),lambda o:any(w['code']=='orphan_evidence' for w in o['warnings']))
run('Unmotivated open question',lambda x:x['edges'].__setitem__(slice(None),[e for e in x['edges'] if e['target']!='open_window_continuity']),lambda o:any(w['node']=='open_window_continuity' and w['code']=='unmotivated_frontier' for w in o['warnings']))
run('Report claim absent from graph',lambda x:x['nodes'].__setitem__(slice(None),[n for n in x['nodes'] if n['id']!='theorem_t3']),lambda o:any('Report claim missing' in e for e in o['errors']))
run('Unsupported formal-proof badge',lambda x:node(x,'theorem_t3').update(status='formally_verified'),lambda o:any('formal status requires' in e for e in o['errors']))
out=dict(command='.venv/Scripts/python.exe -B knowledge/check_validation.py',validator_sha256=hashlib.sha256((K/'validate.py').read_bytes()).hexdigest(),graph_sha256=hashlib.sha256((K/'graph.json').read_bytes()).hexdigest(),tests=cases,passed=True,meaning='Injected graph corruptions were detected. No scientific statement was mutated on disk or re-proved.')
(K/'validation-checks.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(f'{len(cases)} consequential graph-corruption checks passed.')
