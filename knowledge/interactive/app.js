'use strict';
(() => {
  const data=window.RESEARCH_DATA;
  if(!data){document.getElementById('view-title').textContent='Build the atlas first: knowledge/build.py';return;}
  const nodes=new Map(data.nodes.map(n=>[n.id,n]));
  const $=id=>document.getElementById(id);
  const NS='http://www.w3.org/2000/svg';
  const colors={definition:'#477296',assumption:'#947025',result:'#157763',evidence:'#577582',prior:'#7b629b',failure:'#b44844',frontier:'#987325',interpretation:'#526357'};
  const state={view:'research_overview',selected:null,tab:'understand',focus:'theorem_t3',zoom:1,dx:0,dy:0,query:'',status:'',regime:'fold',listChoice:null};
  const focusViews=new Set(['theorem_dependencies','claim_evidence','assumption_sensitivity']);
  const label=s=>String(s||'').replaceAll('_',' ');
  const matchesFilters=n=>(!state.query||`${n.title} ${n.summary} ${n.statement||''} ${n.id}`.toLowerCase().includes(state.query.toLowerCase()))&&(!state.status||n.status===state.status);
  function el(tag,text,cls){const e=document.createElement(tag);if(text!==undefined)e.textContent=text;if(cls)e.className=cls;return e;}
  function svg(tag,attrs={},text){const e=document.createElementNS(NS,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,v));if(text!==undefined)e.textContent=text;return e;}
  function href(src){return '../../'+src.path+(src.anchor?'#'+src.anchor:'');}
  function section(title,text,cls){const s=el('section');s.append(el('h3',title));if(Array.isArray(text)){const ul=el('ul');text.forEach(t=>ul.append(el('li',t)));s.append(ul);}else s.append(el('p',text||'No separate claim is made.',cls));return s;}
  function nodeButton(id,reason){const n=nodes.get(id);if(!n)return el('p','Unresolved graph reference: '+id,'failure-text');const b=el('button',n.title,'node-link');b.type='button';if(reason)b.append(el('small',reason));b.addEventListener('click',()=>selectNode(id));return b;}
  function refsSection(title,ids,empty){const s=el('section');s.append(el('h3',title));if(ids?.length)ids.forEach(id=>s.append(nodeButton(id,nodes.get(id)?.status_label)));else s.append(el('p',empty||'Not separately listed.','empty'));return s;}
  function adjacent(id){return data.edges.filter(e=>e.source===id||e.target===id);}
  function updateHash(){const p=new URLSearchParams({view:state.view});if(state.selected)p.set('node',state.selected);history.replaceState(null,'','#'+p.toString());}
  function setView(id){if(!data.views.some(v=>v.id===id))id='research_overview';state.view=id;state.zoom=1;state.dx=state.dy=0;renderView();updateHash();}
  function wrap(str,width=27){const lines=[];let current='';String(str).split(/\s+/).forEach(w=>{if((current+' '+w).trim().length>width&&current){lines.push(current);current=w;}else current=(current+' '+w).trim();});if(current)lines.push(current);return lines;}
  function layout(columns){columns=columns.filter(c=>c.length);const rows=Math.max(1,...columns.map(c=>c.length));const out={width:42+272*columns.length,height:74+rows*130,positions:{}};columns.forEach((c,i)=>c.forEach((id,j)=>out.positions[id]={x:24+i*272,y:46+(rows-c.length)*65+j*130,w:220,h:98}));return out;}
  function prepareView(base){
    if(!focusViews.has(base.id))return base;
    const n=nodes.get(state.focus);if(!n)return base;
    const seen=new Set([n.id]);const choose=ids=>ids.filter(id=>nodes.has(id)&&!seen.has(id)&&seen.add(id));
    const common=['assume_finite_irreducible','assume_bidirected','assume_even_single_channel'];
    const grouped=common.every(id=>(n.assumptions||[]).includes(id));
    const assumptions=choose(grouped?['concept_model_class',...(n.assumptions||[]).filter(id=>!common.includes(id))]:(n.assumptions||[]));
    const independent=choose(n.independent_verification||[]);
    let evidence=choose([...(n.evidence||[]),...data.edges.filter(e=>e.source===n.id&&['depends_on','derived_from','uses_method'].includes(e.relation)).map(e=>e.target)]);
    const others=choose(data.edges.filter(e=>e.source===n.id&&['implies','generalizes','leaves_open','supports','motivates'].includes(e.relation)).map(e=>e.target));
    let cols;
    if(base.id==='assumption_sensitivity'){
      const cex=choose(data.edges.filter(e=>e.target===n.id&&['limits','corrected_by','falsifies','qualifies','explains'].includes(e.relation)).map(e=>e.source));
      cols=[assumptions,[n.id],cex.concat(others).slice(0,7)];
    }else if(base.id==='claim_evidence')cols=[evidence,[n.id],independent];
    else cols=[assumptions,evidence,[n.id],independent.concat(others).slice(0,5)];
    const view={...base,layout:layout(cols)};const ids=new Set(Object.keys(view.layout.positions));view.visible_edges=data.edges.filter(e=>ids.has(e.source)&&ids.has(e.target));
    if(grouped&&ids.has('concept_model_class'))view.visible_edges.push({source:n.id,target:'concept_model_class',relation:'assumes',explanation:'Display group of the three explicitly listed baseline conditions. Open the claim for the complete assumption list and weakenings.'});
    return view;
  }
  function curve(a,b){
    if(b.x>a.x){const x1=a.x+a.w,y1=a.y+a.h/2,x2=b.x,y2=b.y+b.h/2,d=Math.max(30,(x2-x1)/2);return {d:`M${x1},${y1} C${x1+d},${y1} ${x2-d},${y2} ${x2},${y2}`,x:(x1+x2)/2,y:(y1+y2)/2};}
    if(b.x<a.x){const x1=a.x,y1=a.y+a.h/2,x2=b.x+b.w,y2=b.y+b.h/2,d=Math.max(25,(x1-x2)/2);return {d:`M${x1},${y1} C${x1-d},${y1} ${x2+d},${y2} ${x2},${y2}`,x:(x1+x2)/2,y:(y1+y2)/2};}
    const down=b.y>a.y,x=a.x+a.w/2,y1=a.y+(down?a.h:0),y2=b.y+(down?0:b.h);return {d:`M${x},${y1} L${x},${y2}`,x:x+5,y:(y1+y2)/2};
  }
  let currentLayout=null;
  function applyZoom(){if(!currentLayout)return;const {width,height}=currentLayout,w=width/state.zoom,h=height/state.zoom;$('graph').setAttribute('viewBox',`${(width-w)/2+state.dx} ${(height-h)/2+state.dy} ${w} ${h}`);}
  function renderGraph(view){
    const graph=$('graph');graph.replaceChildren(svg('title',{id:'graph-title'},view.title),svg('desc',{id:'graph-desc'},view.description+' Each node is keyboard selectable. Written statuses distinguish proof from numerical evidence.'));
    const defs=svg('defs'),marker=svg('marker',{id:'arrow',markerWidth:8,markerHeight:8,refX:7,refY:4,orient:'auto'});marker.append(svg('path',{d:'M0,0 L8,4 L0,8',fill:'#8a9e8e'}));defs.append(marker);graph.append(defs);
    const pos=view.layout.positions;currentLayout=view.layout;applyZoom();
    const connections=new Set(adjacent(state.selected).flatMap(e=>[e.source,e.target]));
    view.visible_edges.forEach(e=>{const c=curve(pos[e.source],pos[e.target]);const incident=e.source===state.selected||e.target===state.selected;
      const path=svg('path',{d:c.d,class:`graph-edge ${e.relation} ${incident?'selected':state.selected?'dim':''}`,'marker-end':'url(#arrow)'});path.append(svg('title',{},`${label(e.relation)}: ${e.explanation}`));graph.append(path);
      const show=!state.selected?view.visible_edges.length<17:incident;
      graph.append(svg('text',{x:c.x,y:c.y-5,'text-anchor':'middle',class:'edge-label'+(show?'':' hidden-label')},label(e.relation)));
    });
    Object.entries(pos).forEach(([id,b])=>{const n=nodes.get(id),dim=!matchesFilters(n),g=svg('g',{class:`map-node ${state.selected===id?'selected':''} ${dim?'dim':''}`,tabindex:0,role:'button','aria-label':`${n.title}. ${n.status_label}. Select for details.`,'data-node-id':id});
      g.append(svg('title',{},`${n.summary}\nStatus: ${n.status_label}`));g.append(svg('rect',{x:b.x,y:b.y,width:b.w,height:b.h,rx:5,class:'node-box'}));
      g.append(svg('rect',{x:b.x,y:b.y,width:4,height:b.h,rx:2,fill:colors[n.family]||colors.definition}));
      g.append(svg('text',{x:b.x+13,y:b.y+18,class:'node-status',fill:colors[n.family]||colors.definition},n.status_label));
      wrap(n.map_label||n.title).slice(0,3).forEach((line,j)=>g.append(svg('text',{x:b.x+13,y:b.y+42+18*j,class:'node-title'},line)));
      g.addEventListener('click',()=>selectNode(id));g.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();selectNode(id);}});graph.append(g);
    });
    $('view-count').textContent=`${Object.keys(pos).length} entities · ${view.visible_edges.length} typed relationships · ${data.nodes.length} entities across the atlas`;
  }
  function renderView(){
    const base=data.views.find(v=>v.id===state.view),view=prepareView(base);
    $('view-kicker').textContent=base.kicker||'SCIENTIFIC STRUCTURE';$('view-title').textContent=base.title;$('view-description').textContent=base.description;
    document.querySelectorAll('#views button').forEach(b=>{b.classList.toggle('active',b.dataset.view===state.view);b.setAttribute('aria-current',b.dataset.view===state.view?'page':'false');});
    $('claim-focus-label').hidden=!focusViews.has(state.view);$('claim-focus').value=state.focus;
    const geometry=state.view==='parameter_geometry',list=state.listChoice??window.innerWidth<700;
    $('geometry').hidden=!geometry;$('graph-stage').hidden=geometry||list;$('node-list').hidden=geometry||!list;
    $('toggle-representation').hidden=geometry;$('toggle-representation').textContent=list?'Graph':'List';$('toggle-representation').setAttribute('aria-pressed',String(list));
    document.querySelector('.zoom-controls').hidden=geometry||list;
    renderGraph(view);$('view-reading').replaceChildren();
    $('node-list').replaceChildren();Object.keys(view.layout.positions).filter(id=>matchesFilters(nodes.get(id))).forEach(id=>{const n=nodes.get(id),b=el('button',undefined,'entity-row');b.append(el('span',n.status_label,'entity-status'),el('strong',n.map_label||n.title),el('p',n.summary));b.style.setProperty('--entity-color',colors[n.family]);b.addEventListener('click',()=>selectNode(id));$('node-list').append(b);});
    if(!$('node-list').children.length)$('node-list').append(el('p','No entities in this view match the current filters. Clear the filters or use the global search results.','empty'));
    if(base.reading){$('view-reading').append(el('h2',base.reading.title),el('p',base.reading.text));}
    if(state.view==='parameter_geometry')renderRegime();
  }
  function selectNode(id){if(!nodes.has(id))return;state.selected=id;state.tab='understand';if(nodes.get(id).type.match(/Theorem|Proposition|ProjectResult|Lemma|Generalization/))state.focus=id;$('detail').hidden=false;renderDetail();renderView();updateHash();}
  function renderDetail(){
    const n=nodes.get(state.selected);if(!n)return;
    $('detail-type').textContent=label(n.type.replace(/([a-z])([A-Z])/g,'$1 $2'));$('detail-status').textContent=n.status_label;$('detail-status').style.borderColor=colors[n.family];$('detail-title').textContent=n.title;$('detail-summary').textContent=n.summary;
    document.querySelectorAll('.detail-tabs button').forEach(b=>b.setAttribute('aria-selected',String(b.dataset.tab===state.tab)));
    const body=$('detail-body');body.replaceChildren();
    if(state.tab==='understand'){
      body.append(section('Intuition',n.intuition||n.summary));if(n.statement)body.append(section('Formal statement / precise scope',n.statement,'formal'));
      body.append(section('Why it matters',n.why_it_matters||n.summary));
      if(n.assumption_kind)body.append(section('Role of this assumption',n.assumption_kind));
      if(n.assumptions?.length)body.append(refsSection('Assumptions',n.assumptions));
      if(n.assumption_notes?.length)body.append(section('Which assumptions can change?',n.assumption_notes));
      if(n.verification_scope)body.append(section('Scope of this check',n.verification_scope));
      if(n.paper_sources?.length)body.append(refsSection('Individual primary papers',n.paper_sources));
      if(n.literature){Object.entries(n.literature).forEach(([key,value])=>body.append(section(label(key),value)));}
      if(n.novelty){body.append(section('Novelty status',n.novelty.status+': '+n.novelty.summary));if(n.novelty.comparisons?.length)body.append(refsSection('Closest prior results',n.novelty.comparisons));}
      if(n.limitations?.length)body.append(section('Limitations / what would change this',n.limitations));
      if(n.falsification_condition)body.append(section('Falsification condition',n.falsification_condition));
    }else if(state.tab==='evidence'){
      body.append(refsSection('Proofs and supporting evidence',n.evidence,'See the precise artifact sources and typed relationships below.'));
      if(n.supporting_artifacts?.length){const s=el('section');s.append(el('h3','Direct derivation artifacts'));n.supporting_artifacts.forEach(p=>{const a=el('a',p.label||p.path);a.href=href(p);a.target='_blank';a.rel='noopener';const line=el('p');line.append(a);s.append(line);});body.append(s);}
      body.append(refsSection('Independent verification',n.independent_verification,'No separate independent check is listed for this entity. Definition, prior-source attribution and proof status are not interchangeable.'));
      if(n.verification_scope)body.append(section('Verification scope',n.verification_scope));
      if(n.falsification_attempts?.length)body.append(section('Counterexample attempts and their limits',n.falsification_attempts));
      const s=el('section');s.append(el('h3','Typed scientific relationships'));
      adjacent(n.id).forEach(e=>{const outgoing=e.source===n.id,other=outgoing?e.target:e.source;s.append(el('span',`${outgoing?'This entity →':'This entity ←'} ${label(e.relation)}`,'relation-label'),nodeButton(other,e.explanation));});body.append(s);
      body.append(el('p','Checks of identities, high-precision examples, complete proofs and novelty comparisons have different evidential roles. A failed numerical search is not a proof.','scope-notice'));
    }else{
      body.append(el('p','These excerpts are generated from the linked originals. Edit the research artifact first, then review the affected graph entry.','scope-notice'));
      n.provenance.forEach(src=>{const box=el('section',undefined,'source-entry');
        if(src.path){const a=el('a',src.label||'Open original artifact ↗');a.href=href(src);a.target='_blank';a.rel='noopener';box.append(a,el('span',src.path+(src.anchor?'#'+src.anchor:''),'path'));}
        if(src.url){const a=el('a','Primary source / recorded access route ↗');a.href=src.url;a.target='_blank';a.rel='noopener';box.append(a);}
        if(src.excerpt){const d=el('details');d.append(el('summary','Read the exact source excerpt'),el('pre',src.excerpt));box.append(d);}
        body.append(box);
      });
    }
    $('detail').scrollTop=0;
  }
  function renderSearch(){const box=$('search-results');box.replaceChildren();box.hidden=!state.query;if(!state.query)return;const q=state.query.toLowerCase(),matches=data.nodes.filter(n=>`${n.title} ${n.summary} ${n.statement||''} ${n.id}`.toLowerCase().includes(q)&&(!state.status||n.status===state.status));
    box.append(el('p',`${matches.length} matches across the complete atlas`));matches.slice(0,35).forEach(n=>{const b=el('button',n.title);b.append(el('small',n.status_label+' · '+label(n.type)));b.addEventListener('click',()=>{selectNode(n.id);box.hidden=true;});box.append(b);});if(matches.length>35)box.append(el('p','Refine the search to inspect the remaining matches.'));}
  function renderRegime(){const modes={below:{models:['Q₁','Q₂','…'],entropy:'Unbounded above',note:'Arbitrarily large finite compatible entropy; no infinite-rate model is admitted.'},fold:{models:['Q₀','Q*'],entropy:'Exactly two values',note:'σ₀ ∈ [0.062946400236, 0.062946400237]; σ* ∈ [0.065579685966, 0.065579685967].'},above:{models:['Q₀'],entropy:'A singleton',note:'The complete cap-five physical generator fiber is unique modulo hidden labels.'}};const m=modes[state.regime];$('fiber-models').replaceChildren(...m.models.map(t=>el('span',t,t==='…'?'':'model-dot')));$('fiber-entropy').textContent=m.entropy;$('fiber-note').textContent=m.note;document.querySelectorAll('[data-regime]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.regime===state.regime)));}
  data.views.forEach(v=>{const b=el('button');b.dataset.view=v.id;b.append(el('span',v.code||''),el('div',v.nav_title||v.title));b.addEventListener('click',()=>setView(v.id));$('views').append(b);});
  data.nodes.filter(n=>/Theorem|Proposition|ProjectResult|Lemma|Generalization/.test(n.type)&&!['falsified','superseded'].includes(n.status)).forEach(n=>{const o=el('option',n.title);o.value=n.id;$('claim-focus').append(o);});
  $('claim-focus').addEventListener('change',e=>{state.focus=e.target.value;state.zoom=1;state.dx=state.dy=0;renderView();});
  $('search').addEventListener('input',e=>{state.query=e.target.value.trim();renderSearch();renderView();});$('status-filter').addEventListener('change',e=>{state.status=e.target.value;renderSearch();renderView();});
  $('zoom-in').addEventListener('click',()=>{state.zoom=Math.min(4,state.zoom*1.3);applyZoom();});$('zoom-out').addEventListener('click',()=>{state.zoom=Math.max(.7,state.zoom/1.3);applyZoom();});$('zoom-fit').addEventListener('click',()=>{state.zoom=1;state.dx=state.dy=0;applyZoom();});
  $('toggle-representation').addEventListener('click',()=>{state.listChoice=!(state.listChoice??window.innerWidth<700);renderView();});window.addEventListener('resize',()=>renderView());
  $('close-detail').addEventListener('click',()=>{state.selected=null;$('detail').hidden=true;renderView();updateHash();});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!$('health-dialog').open)$('close-detail').click();});
  document.querySelectorAll('.detail-tabs button').forEach(b=>b.addEventListener('click',()=>{state.tab=b.dataset.tab;renderDetail();}));
  document.querySelectorAll('[data-regime]').forEach(b=>b.addEventListener('click',()=>{state.regime=b.dataset.regime;renderRegime();}));
  $('export-view').addEventListener('click',()=>window.open(`../views/${state.view==='parameter_geometry'?'parameter_geometry':state.view}.svg`,'_blank','noopener'));
  $('health-button').addEventListener('click',()=>{const h=$('health-content'),v=data.validation;h.replaceChildren(el('strong',v.passed?'Structural checks passed':'Structural checks need attention',v.passed?'pass':'failure-text'));h.append(section('What was checked',Object.entries(v.checks||{}).map(([k,x])=>label(k)+': '+x)));h.append(section('Integrity errors',(v.errors||[]).length?v.errors:['None recorded.']));h.append(section('Mapping gaps',(v.warnings||[]).length?v.warnings.map(w=>`${w.node}: ${w.message}`):['None flagged by these structural rules.']));h.append(section('Scientific risks remain',(v.scientific_risks||[]).map(r=>r.summary)));$('health-dialog').showModal();});$('close-health').addEventListener('click',()=>$('health-dialog').close());
  let drag=null;$('graph-stage').addEventListener('pointerdown',e=>{if(e.target.closest('.map-node')||e.button!==0)return;drag={x:e.clientX,y:e.clientY,dx:state.dx,dy:state.dy};$('graph-stage').setPointerCapture(e.pointerId);});$('graph-stage').addEventListener('pointermove',e=>{if(!drag||!currentLayout)return;const r=$('graph-stage').getBoundingClientRect(),scale=Math.max(currentLayout.width/r.width,currentLayout.height/r.height)/state.zoom;state.dx=drag.dx-(e.clientX-drag.x)*scale;state.dy=drag.dy-(e.clientY-drag.y)*scale;applyZoom();});$('graph-stage').addEventListener('pointerup',()=>{drag=null;});
  $('graph-stage').addEventListener('keydown',e=>{if(e.target!==$('graph-stage'))return;const d=50/state.zoom;if(e.key==='ArrowLeft')state.dx-=d;else if(e.key==='ArrowRight')state.dx+=d;else if(e.key==='ArrowUp')state.dy-=d;else if(e.key==='ArrowDown')state.dy+=d;else return;e.preventDefault();applyZoom();});
  function readHash(){const p=new URLSearchParams(location.hash.slice(1));if(data.views.some(v=>v.id===p.get('view')))state.view=p.get('view');if(nodes.has(p.get('node')))selectNode(p.get('node'));else renderView();}
  window.addEventListener('hashchange',readHash);readHash();
})();
