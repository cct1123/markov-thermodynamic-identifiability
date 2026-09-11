"""Structural and provenance checks for the semantic research map, not proof checking."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import re
from pathlib import Path

import networkx as nx

ROOT=Path(__file__).resolve().parents[1]
HERE=ROOT/'knowledge'
CLAIM_TYPES={'Theorem','Proposition','ProjectResult','Generalization','TheoremCandidate','Lemma'}
EVIDENCE_TYPES={'EvidenceRecord','SymbolicResult','NumericalResult','FormalProof'}
LIVE={'analytically_proved','independently_verified','theorem_candidate','conjecture'}
STATUSES={'established_prior_result','reproduced_prior_result','numerical_observation','strong_numerical_evidence','conjecture','theorem_candidate','analytically_proved','independently_verified','provenance_checked','formally_verified','falsified','superseded','unresolved','interpretation','assumption','definition'}
RELATIONS={'defines','depends_on','assumes','implies','supports','strongly_supports','tests','contradicts','falsifies','limits','explains','derived_from','verified_by','generalizes','special_case_of','equivalent_to','distinguished_from','motivates','resolves','leaves_open','novelty_compared_with','extends','reproduces','uses_method','emerges_from','differs_from','potentially_overlaps','novelty_unresolved','revises','next_action','weakens','requires_review','documents'}

def anchors(path):
    text=path.read_text(encoding='utf-8-sig')
    text=re.sub(r'(?ms)^(`{3,}|~{3,}).*?^\1[^\n]*$','',text)
    found=set();counts={}
    for h in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',text,re.M):
        slug=re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-')
        c=counts.get(slug,0);counts[slug]=c+1
        found.add(slug+(f'-{c}' if c else ''))
    return found

def validate(g,check_sources=True):
    errors=[];warnings=[];checks={};ns=g.get('nodes',[]);ids=[n.get('id') for n in ns];by={n['id']:n for n in ns}
    if len(set(ids))!=len(ids): errors.append('Duplicate node IDs.')
    network=nx.MultiDiGraph();network.add_nodes_from(ids)
    dep=nx.DiGraph();dep.add_nodes_from(ids)
    support=nx.DiGraph();support.add_nodes_from(ids)
    def issue(msg): errors.append(msg)
    for n in ns:
        id=n['id']
        for f in ('id','type','title','status','summary','provenance'):
            if not n.get(f): issue(f'{id}: missing {f}')
        if n.get('level') not in (0,1,2,3): issue(f'{id}: missing or invalid drill-down level')
        if not re.fullmatch(r'[a-z][a-z0-9_]*',id): issue(f'{id}: unstable identifier format')
        if n['status'] not in STATUSES: issue(f'{id}: unrecognized status {n["status"]}')
        if n['status']=='formally_verified':
            certificate=n.get('formal_certificate',{})
            for f in ('theorem','build_log','axiom_audit'):
                if not certificate.get(f): issue(f'{id}: formal status requires an inspected {f}')
            for f in ('build_log','axiom_audit'):
                if certificate.get(f) and not (ROOT/certificate[f]).exists(): issue(f'{id}: missing formal evidence file {certificate[f]}')
        for p in n.get('provenance',[]):
            if not p.get('path') and not p.get('url'): issue(f'{id}: provenance has neither path nor URL')
            if p.get('path'):
                target=(ROOT/p['path']).resolve()
                if ROOT not in target.parents and target!=ROOT: issue(f'{id}: source path escapes repository')
                elif not target.exists(): issue(f'{id}: missing source {p["path"]}')
                elif p.get('anchor') and target.suffix=='.md' and p['anchor'] not in anchors(target): issue(f'{id}: missing anchor {p["path"]}#{p["anchor"]}')
        for f in ('assumptions','evidence','independent_verification','paper_sources'):
            for ref in n.get(f,[]):
                if ref not in by: issue(f'{id}: unknown {f} reference {ref}')
        for ref in n.get('paper_sources',[]):
            if ref in by and by[ref]['type']!='LiteratureSource': issue(f'{id}: paper source is not an individual LiteratureSource: {ref}')
        for ref in n.get('novelty',{}).get('comparisons',[]):
            if ref not in by: issue(f'{id}: unknown literature comparison {ref}')
        if n['type'] in CLAIM_TYPES and n['status'] in LIVE:
            for f in ('statement','assumptions','evidence'):
                if not n.get(f) and not (f=='evidence' and n.get('supporting_artifacts')): warnings.append(dict(code='claim_gap',node=id,message=f'Claim lacks explicit {f}.'))
            for ref in n.get('independent_verification',[]):
                if ref in by and by[ref]['status']=='provenance_checked': warnings.append(dict(code='metadata_is_not_verification',node=id,message='A manifest or saved-output inspection is being presented as independent scientific verification.'))
            if not n.get('independent_verification'): warnings.append(dict(code='independent_check_gap',node=id,message='No separate independent verification node is listed. Check the recorded scope; do not infer that the result is false.'))
            if not n.get('novelty',{}).get('comparisons'): warnings.append(dict(code='novelty_comparison_gap',node=id,message='No closest-prior comparison node is listed.'))
    for e in g.get('edges',[]):
        a,b=e['source'],e['target']
        if a not in by or b not in by: issue(f'Edge has unknown endpoint: {a} {e["relation"]} {b}');continue
        if e['relation'] not in RELATIONS: issue(f'Unknown edge relation {e["relation"]}')
        if not e.get('explanation'): issue(f'Edge lacks scientific explanation: {a}→{b}')
        network.add_edge(a,b,**e)
        if e['relation'] in ('depends_on','derived_from'): dep.add_edge(a,b)
        if e['relation'] in ('depends_on','derived_from','verified_by'): support.add_edge(b,a)
        elif e['relation'] in ('supports','strongly_supports','implies'): support.add_edge(a,b)
        if e['relation']=='contradicts' and by[a]['status'] not in ('falsified','superseded') and by[b]['status'] not in ('falsified','superseded') and not e.get('resolution'):
            warnings.append(dict(code='unresolved_contradiction',node=b,message=f'{a} contradicts {b}, with no resolution recorded.'))
    for n in ns:
        id=n['id']
        if n['status'] in ('falsified','superseded'):
            bad=[d for d in nx.descendants(support,id) if by[d]['status'] in LIVE]
            if bad: issue(f'{id}: rejected statement supports accepted claims {bad}; use a historical relation instead')
        if n['status'] in LIVE:
            bad=[d for d in nx.descendants(dep,id) if by[d]['status'] in ('falsified','superseded')]
            if bad: issue(f'{id}: logical dependency on falsified/superseded nodes {bad}')
        if n['type'] in EVIDENCE_TYPES and network.degree(id)==0: warnings.append(dict(code='orphan_evidence',node=id,message='Evidence is not linked to a scientific claim.'))
        if n['type']=='OpenQuestion' and not any(e.get('relation') in ('motivates','leaves_open','limits') for _,_,e in network.in_edges(id,data=True)):
            warnings.append(dict(code='unmotivated_frontier',node=id,message='Open question lacks a motivating result relationship.'))
    checks['nodes']=len(ns);checks['typed_edges']=network.number_of_edges();checks['logical_dependency_dag']=nx.is_directed_acyclic_graph(dep)
    if not checks['logical_dependency_dag']: issue('Logical proof dependency graph contains a cycle; review edge directions.')
    for v in g.get('views',[]):
        vi=[id for col in v.get('columns',[]) for id in col]
        if len(vi)!=len(set(vi)): issue(f'{v["id"]}: duplicate nodes in view')
        for id in vi:
            if id not in by: issue(f'{v["id"]}: missing node {id}')
    checks['views']=len(g.get('views',[]))
    overview=next((v for v in g.get('views',[]) if v['id']=='research_overview'),None)
    if not overview or not 10<=sum(map(len,overview['columns']))<=20: issue('Executive map must contain 10–20 major nodes.')
    report=(ROOT/'outputs/REPORT.md').read_text(encoding='utf-8')
    for c in g.get('report_coverage',[]):
        if c['locator'] not in report: issue(f'Report coverage locator changed: {c["locator"]}')
        for id in c['nodes']:
            if id not in by: issue(f'Report claim missing from graph: {id}')
    checks['report_sections_mapped']=len(g.get('report_coverage',[]))
    checks['report_coverage_method']='Human-reviewed section/claim mapping plus source hash drift detection; not automatic semantic completeness.'
    if check_sources:
        for path,sha in g.get('source_hashes',{}).items():
            p=ROOT/path
            if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha: issue(f'Source changed since map review: {path}. Review affected nodes before accepting a new snapshot.')
    checks['source_snapshots']=len(g.get('source_hashes',{}))
    risks=[dict(node=n['id'],title=n['title'],summary=n['summary']) for n in ns if n['type']=='NoveltyRisk']
    return dict(meaning='Structural integrity and provenance audit. A clean graph does not verify a proof or establish novelty.',checks=checks,errors=errors,warnings=warnings,scientific_risks=risks,passed=not errors)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--graph',default=str(HERE/'graph.json'));parser.add_argument('--no-write',action='store_true');parser.add_argument('--accept-reviewed-sources',action='store_true',help='Refresh source fingerprints only after a human/agent has reviewed changes and updated affected nodes. This does not perform that review.');args=parser.parse_args()
    gp=Path(args.graph);g=json.loads(gp.read_text(encoding='utf-8'))
    if args.accept_reviewed_sources:
        if args.no_write:parser.error('--accept-reviewed-sources cannot be combined with --no-write')
        paths=set(g.get('source_hashes',{}))|{p['path'] for n in g['nodes'] for p in n.get('provenance',[]) if p.get('path')}
        if any(not (ROOT/p).exists() for p in paths):parser.error('A source is missing; repair the reference before accepting a snapshot.')
        g['source_hashes']={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(paths)}
        g['source_snapshot_reviewed_utc']=datetime.now(timezone.utc).isoformat()
        with gp.open('w',encoding='utf-8',newline='\n') as f:json.dump(g,f,ensure_ascii=False,indent=2);f.write('\n')
    out=validate(g)
    if not args.no_write:
        (HERE/'validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,ensure_ascii=True,indent=2))
    raise SystemExit(0 if out['passed'] else 1)

if __name__=='__main__': main()
