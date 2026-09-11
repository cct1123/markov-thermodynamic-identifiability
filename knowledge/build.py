"""Build offline views from graph.json and accepted research formulas.

Run from root: .venv/Scripts/python.exe -B knowledge/build.py
No network, new research search, or writes to accepted scientific outputs.
"""
import hashlib
import html
import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / 'knowledge'
COLORS = {'definition':'#477296', 'assumption':'#9b7431', 'prior':'#7b629b',
          'result':'#157763', 'evidence':'#577582', 'failure':'#b44844',
          'frontier':'#987325', 'interpretation':'#526357'}

def family(node):
    t = node['type'].lower()
    if node['status'] in ('falsified','superseded') or t in ('counterexample','failuremode'): return 'failure'
    if t in ('assumption','parameterconstraint'): return 'assumption'
    if t in ('literaturesource','knownpriorresult','literature'): return 'prior'
    if t in ('openquestion','noveltyrisk','frontier','risk'): return 'frontier'
    if t in ('theorem','lemma','proposition','projectresult','generalization','theoremcandidate'): return 'result'
    if t in ('evidencerecord','symbolicresult','numericalresult','method','formalproof'): return 'evidence'
    if t in ('publicationclaim','interpretation','researchaction'): return 'interpretation'
    return 'definition'

def status_label(status):
    return {'analytically_proved':'PROVED', 'independently_verified':'INDEPENDENT CHECK',
            'established_prior_result':'KNOWN PRIOR RESULT','reproduced_prior_result':'REPRODUCED',
            'numerical_observation':'NUMERICAL', 'strong_numerical_evidence':'NUMERICAL',
            'definition':'DEFINITION', 'assumption':'ASSUMPTION','unresolved':'UNRESOLVED','provenance_checked':'SAVED PROVENANCE',
            'interpretation':'INTERPRETATION','falsified':'FALSIFIED','superseded':'SUPERSEDED',
            'conjecture':'CONJECTURE','theorem_candidate':'CANDIDATE','formally_verified':'FORMAL PROOF'
            }.get(status,status.replace('_',' ').upper())

def layout(view, nodes):
    columns = [[n for n in col if n in nodes] for col in view.get('columns',[])]
    columns = [col for col in columns if col]
    max_rows = max(map(len,columns), default=1)
    width, height = 42 + 272 * len(columns), 74 + max_rows * 130
    pos={}
    for ci,col in enumerate(columns):
        offset = (max_rows-len(col))*65
        for ri,id in enumerate(col):
            pos[id]=dict(x=24+ci*272,y=46+offset+ri*130,w=220,h=98)
    return dict(width=width,height=height,positions=pos)

def connection(a,b):
    if b['x'] > a['x']:
        x1,y1=a['x']+a['w'],a['y']+a['h']/2; x2,y2=b['x'],b['y']+b['h']/2
        dx=max(30,(x2-x1)*0.5)
        return f'M{x1},{y1} C{x1+dx},{y1} {x2-dx},{y2} {x2},{y2}',(x1+x2)/2,(y1+y2)/2
    if b['x'] < a['x']:
        x1,y1=a['x'],a['y']+a['h']/2; x2,y2=b['x']+b['w'],b['y']+b['h']/2
        dx=max(25,(x1-x2)*.5)
        return f'M{x1},{y1} C{x1-dx},{y1} {x2+dx},{y2} {x2},{y2}',(x1+x2)/2,(y1+y2)/2
    down=b['y']>a['y']
    x1,y1=a['x']+a['w']/2,a['y']+(a['h'] if down else 0)
    x2,y2=b['x']+b['w']/2,b['y']+(0 if down else b['h'])
    return f'M{x1},{y1} L{x2},{y2}',x1+4,(y1+y2)/2

def svg_view(view,nodes,edges):
    lay=layout(view,nodes); view['layout']=lay
    p=lay['positions']; vis=[e for e in edges if e['source'] in p and e['target'] in p]
    if view.get('edge_relations'): vis=[e for e in vis if e['relation'] in view['edge_relations']]
    view['visible_edges']=vis
    esc=html.escape
    body=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{lay["width"]}" height="{lay["height"]+78}" viewBox="0 0 {lay["width"]} {lay["height"]+78}" role="img" aria-labelledby="title desc">',
          f'<title id="title">{esc(view["title"])}</title><desc id="desc">{esc(view["description"])}</desc>',
          '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#8a948f"/></marker></defs>',
          '<rect width="100%" height="100%" fill="#fafaf6"/>',
          f'<text x="24" y="25" font-family="DejaVu Sans,sans-serif" font-size="18" fill="#21372f">{esc(view["title"])}</text>']
    for e in vis:
        path,x,y=connection(p[e['source']],p[e['target']])
        color='#b44844' if e['relation'] in ('falsifies','contradicts') else '#a0aaa5'
        body.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="1.2" marker-end="url(#arrow)"><title>{esc(e["relation"]+": "+e["explanation"])}</title></path>')
        if len(vis)<18:
            body.append(f'<text x="{x}" y="{y-4}" text-anchor="middle" font-family="DejaVu Sans,sans-serif" font-size="8" fill="#51635b" style="paint-order:stroke;stroke:#fafaf6;stroke-width:4px">{esc(e["relation"].replace("_"," "))}</text>')
    for id,b in p.items():
        n=nodes[id]; color=COLORS[family(n)]
        body.append(f'<g><title>{esc(n["summary"])}</title><rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" rx="5" fill="white" stroke="#d4dcd5"/><rect x="{b["x"]}" y="{b["y"]}" width="4" height="{b["h"]}" rx="2" fill="{color}"/>')
        body.append(f'<text x="{b["x"]+13}" y="{b["y"]+18}" font-family="DejaVu Sans,sans-serif" font-size="9" font-weight="bold" fill="{color}">{esc(status_label(n["status"]))}</text>')
        for j,line in enumerate(textwrap.wrap(n.get('map_label',n['title']),27)[:3]):
            body.append(f'<text x="{b["x"]+13}" y="{b["y"]+42+18*j}" font-family="DejaVu Sans,sans-serif" font-size="13" fill="#21372f">{esc(line)}</text>')
        body.append('</g>')
    body.append(f'<text x="24" y="{lay["height"]+8}" font-family="DejaVu Sans,sans-serif" font-size="11" fill="#51635b">Proof, numerical checks and novelty have separate statuses. Arrows use the relations in graph.json.</text>')
    body.append(f'<text x="24" y="{lay["height"]+29}" font-family="DejaVu Sans,sans-serif" font-size="11" fill="#51635b">Interactive companion: select a node to read assumptions, typed relationships and exact provenance.</text></svg>')
    return '\n'.join(body)

def excerpt(source):
    if not source.get('path'): return ''
    p=ROOT/source['path']
    if not p.exists() or p.suffix not in ('.md','.py','.json','.txt'): return ''
    text=p.read_text(encoding='utf-8-sig')
    if p.suffix=='.md' and source.get('anchor'):
        lines=text.splitlines(); start=None; depth=0
        for i,line in enumerate(lines):
            m=re.match(r'^(#{1,6})\s+(.+?)\s*#*$',line)
            if not m: continue
            slug=re.sub(r'[^\w\- ]','',m.group(2).lower()).replace(' ','-')
            if start is None and slug==source['anchor']: start=i;depth=len(m.group(1))
            elif start is not None and len(m.group(1))<=depth:
                text='\n'.join(lines[start:i]);break
        else:
            if start is not None: text='\n'.join(lines[start:])
    cap=16000
    return text if len(text)<=cap else text[:cap]+'\n\n[Excerpt truncated; open the linked original for the complete artifact.]'

def quantitative_geometry():
    import mpmath as mp
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    mp.mp.dps=100
    data=[]
    for e_float in np.geomspace(.025,.30,70):
        e=mp.mpf(str(e_float));k=mp.exp(-1/e**2)
        z=3+e+2*k-e**2-e*k-k**2
        sigma=(e-k)*(1-e-k)/z*(mp.log(e)+mp.log(1-e)+1/e**2-mp.log(1-k))
        data.append(dict(e=str(e),k=str(k),entropy=str(sigma),scaled_entropy=str(e*sigma),row_tv_upper=str(4*e)))
    meta=dict(source='analysis/three-state-fixed-trace-audit.md', evidence='E057',
              purpose='Illustration of an already proved limit; no new parameter search or proof.',
              formula='k=exp(-1/e^2); sigma=(e-k)(1-e-k)/(3+e+2k-e^2-ek-k^2) * log[e(1-e)/(k(1-k))]',
              command='.venv/Scripts/python.exe -B knowledge/build.py',precision_digits=100,seed=None,
              input_sha256=hashlib.sha256((ROOT/'analysis/three-state-fixed-trace-audit.md').read_bytes()).hexdigest(),
              build_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),points=data)
    (HERE/'views/geometry-data.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path'})
    fig,axes=plt.subplots(1,2,figsize=(10.8,3.9),layout='constrained',facecolor='#fafaf6')
    for ax in axes: ax.set_facecolor('#fafaf6')
    es=[float(d['e']) for d in data]
    axes[0].plot(es,[float(d['scaled_entropy']) for d in data],color='#157763',lw=2)
    axes[0].axhline(1/3,color='#526357',lw=1,ls='--')
    axes[0].text(.14,.336,'Proved limit: 1/3',fontsize=9,color='#526357')
    axes[0].set(xlabel='Chord opening e (e → 0 to the left)',ylabel='e × entropy rate (fixed units)',title='Divergent entropy near an identifiable tree',ylim=(.93*min(float(d['scaled_entropy']) for d in data),.35),xlim=(0,.315))
    axes[1].plot(es,[min(1,float(d['row_tv_upper'])) for d in data],color='#477296',lw=2)
    axes[1].set(xlabel='Chord opening e',ylabel='Upper bound on row total variation',title='Observed laws approach the tree',ylim=(0,1.08))
    axes[1].text(.025,.92,'d_TV < 4e; TV also ≤ 1',fontsize=9,color='#526357')
    fig.suptitle('Exact three-state family • trace −4 • rates ≤ 1 • k = exp(−1/e²)',fontsize=12,fontweight='medium')
    for ext in ('svg','png'): fig.savefig(HERE/f'views/parameter_geometry.{ext}',dpi=170)
    plt.close(fig)
    return meta

def main():
    graph=json.loads((HERE/'graph.json').read_text(encoding='utf-8'))
    nodes={n['id']:n for n in graph['nodes']}
    for n in nodes.values():
        n['family']=family(n);n['status_label']=status_label(n['status'])
        for src in n['provenance']: src['excerpt']=excerpt(src)
    for view in graph['views']:
        svg=svg_view(view,nodes,graph['edges'])
        if view['id']!='parameter_geometry':
            (HERE/f'views/{view["id"]}.svg').write_text(svg,encoding='utf-8')
    graph['geometry']=quantitative_geometry()
    vp=HERE/'validation.json'
    graph['validation']=json.loads(vp.read_text()) if vp.exists() else {'errors':['Validation has not run.'],'warnings':[]}
    raw=json.dumps(graph,ensure_ascii=False,separators=(',',':')).replace('</','<\/')
    (HERE/'interactive/data.js').write_text('window.RESEARCH_DATA='+raw+';\n',encoding='utf-8')
    print(f'Built {len(graph["views"])} views: 11 static SVG maps, quantitative SVG/PNG/data, and offline browser data for {len(nodes)} nodes.')

if __name__=='__main__': main()
