// Local offline browser QA. No browser account, external pages, or user profile.
// node knowledge/check_browser.mjs
import {spawn} from 'node:child_process';
import {readFile,writeFile,mkdir,access,rm} from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL,fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
const here=path.dirname(fileURLToPath(import.meta.url));
const candidates=[process.env.ATLAS_BROWSER,'C:/Program Files/Google/Chrome/Application/chrome.exe','C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'].filter(Boolean);
let executable;
for(const candidate of candidates){try{await access(candidate);executable=candidate;break;}catch{}}
if(!executable)throw Error('Set ATLAS_BROWSER to a local Chromium executable. No download is attempted.');
const profile=path.join(here,'.browser-qa');await mkdir(profile,{recursive:true});
await rm(path.join(profile,'DevToolsActivePort'),{force:true});
const child=spawn(executable,['--headless=new','--disable-gpu','--disable-background-networking','--disable-component-update','--disable-sync','--no-first-run','--no-default-browser-check','--remote-debugging-port=0','--remote-debugging-address=127.0.0.1',`--user-data-dir=${profile}`,'about:blank'],{windowsHide:true,stdio:'ignore'});
const pause=ms=>new Promise(r=>setTimeout(r,ms));
let port;
for(let i=0;i<80;i++){try{port=(await readFile(path.join(profile,'DevToolsActivePort'),'utf8')).split('\n')[0];break;}catch{await pause(150);}}
if(!port){child.kill();throw Error('Local browser did not expose its debugging port.');}
const targets=await(await fetch(`http://127.0.0.1:${port}/json`)).json();
const target=targets.find(t=>t.type==='page');
const ws=new WebSocket(target.webSocketDebuggerUrl);await new Promise((res,rej)=>{ws.addEventListener('open',res,{once:true});ws.addEventListener('error',rej,{once:true});});
let seq=0;const pending=new Map(),exceptions=[];
ws.addEventListener('message',event=>{const message=JSON.parse(event.data);if(message.id){const p=pending.get(message.id);if(p){pending.delete(message.id);message.error?p.reject(Error(JSON.stringify(message.error))):p.resolve(message.result);}}else if(message.method==='Runtime.exceptionThrown')exceptions.push(message.params.exceptionDetails.text);});
function call(method,params={}){return new Promise((resolve,reject)=>{const id=++seq;pending.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params}));});}
async function evaluate(expression){const r=await call('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true});if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;}
const results=[];function check(name,pass,detail){results.push({name,passed:Boolean(pass),detail});if(!pass)throw Error(name+': '+JSON.stringify(detail));}
async function capture(name){const shot=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});await writeFile(path.join(here,'views',name+'.png'),Buffer.from(shot.data,'base64'));}
try{
 const browserVersion=await call('Browser.getVersion');
 await call('Runtime.enable');await call('Page.enable');
 await call('Emulation.setDeviceMetricsOverride',{width:1440,height:1000,deviceScaleFactor:1,mobile:false});
 await call('Page.navigate',{url:pathToFileURL(path.join(here,'interactive/index.html')).href});
 for(let i=0;i<100;i++){if(await evaluate('Boolean(window.RESEARCH_DATA && document.querySelectorAll(".map-node").length)'))break;await pause(80);}
 check('offline data and first view',await evaluate('window.RESEARCH_DATA.nodes.length>=100 && document.querySelectorAll(".map-node").length>=10'));
 await capture('atlas-overview');
 const views=await evaluate('window.RESEARCH_DATA.views.map(v=>v.id)');
 for(const id of views){await evaluate(`document.querySelector('[data-view="${id}"]').click()`);const result=await evaluate('({title:document.getElementById("view-title").textContent,count:document.querySelectorAll(".map-node").length,geometry:!document.getElementById("geometry").hidden})');check('view '+id,Boolean(result.title)&&(result.count>0||result.geometry),result);}
 await evaluate('document.querySelector("[data-view=research_overview]").click();document.querySelector("[data-node-id=theorem_t3]").dispatchEvent(new MouseEvent("click",{bubbles:true}))');
 check('exact theorem detail',await evaluate('!document.getElementById("detail").hidden && document.getElementById("detail-body").textContent.includes("352")'));
 await evaluate('document.querySelector("[data-tab=evidence]").click()');
 check('evidence drilldown',await evaluate('document.getElementById("detail-body").textContent.includes("Independent verification")'));
 await evaluate('document.querySelector("[data-tab=sources]").click();document.querySelector("#detail-body details").open=true');
 check('exact provenance excerpt',await evaluate('document.querySelector("#detail-body pre").textContent.length>100'));
 await capture('atlas-provenance');
 await evaluate('document.getElementById("close-detail").click();document.querySelector("[data-view=literature_novelty]").click();document.querySelector("[data-node-id=prior_realization_equivalence]").dispatchEvent(new MouseEvent("click",{bubbles:true}))');
 check('individual paper links',await evaluate('document.getElementById("detail-body").textContent.includes("Individual primary papers") && document.querySelectorAll("#detail-body .node-link").length>=3'));
 await evaluate('Array.from(document.querySelectorAll("#detail-body .node-link")).find(b=>b.textContent.includes("minimal representation of Markov arrival")).click()');
 check('paper-specific scope and attribution',await evaluate('document.getElementById("detail-body").textContent.includes("M. Telek; G.") && document.getElementById("detail-body").textContent.includes("nonredundant irreducible MAPs")'));
 await capture('atlas-literature');
 await evaluate('document.getElementById("close-detail").click();document.querySelector("[data-view=theorem_dependencies]").click();document.getElementById("claim-focus").value="theorem_t6";document.getElementById("claim-focus").dispatchEvent(new Event("change"))');
 check('claim focus changes graph',await evaluate('Boolean(document.querySelector("[data-node-id=theorem_t6]"))'));
 await capture('atlas-dependencies');
 await evaluate('document.getElementById("search").value="ratio";document.getElementById("search").dispatchEvent(new Event("input"))');
 check('global semantic search',await evaluate('document.querySelectorAll("#search-results button").length>=2'));
 await evaluate('document.getElementById("search").value="";document.getElementById("search").dispatchEvent(new Event("input"));document.getElementById("status-filter").value="assumption";document.getElementById("status-filter").dispatchEvent(new Event("change"))');
 check('status filter dims other roles',await evaluate('document.querySelectorAll(".map-node.dim").length>0'));
 await evaluate('document.getElementById("status-filter").value="";document.getElementById("status-filter").dispatchEvent(new Event("change"));document.querySelector("[data-view=parameter_geometry]").click();document.querySelector("[data-regime=below]").click()');
 check('unbounded geometry regime',await evaluate('document.getElementById("fiber-entropy").textContent==="Unbounded above"'));
 await evaluate('document.querySelector("[data-regime=fold]").click()');
 check('exact two-point geometry regime',await evaluate('document.getElementById("fiber-note").textContent.includes("0.065579685966")'));
 await capture('atlas-geometry');
 await evaluate('document.getElementById("health-button").click()');
 check('graph checks disclose limits',await evaluate('document.getElementById("health-dialog").open && document.getElementById("health-dialog").textContent.includes("do not verify")'));
 await evaluate('document.getElementById("close-health").click();document.querySelector("[data-view=research_overview]").click()');
 await call('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
 await pause(100);
 check('mobile has readable list alternative',await evaluate('!document.getElementById("node-list").hidden && document.querySelectorAll(".entity-row").length>=10'));
 await evaluate('document.getElementById("status-filter").value="analytically_proved";document.getElementById("status-filter").dispatchEvent(new Event("change"))');
 check('mobile list applies the evidence-status filter',await evaluate('document.querySelectorAll(".entity-row").length===4 && Array.from(document.querySelectorAll(".entity-status")).every(e=>e.textContent==="PROVED")'));
 await evaluate('document.getElementById("status-filter").value="";document.getElementById("status-filter").dispatchEvent(new Event("change"))');
 await capture('atlas-mobile');
 await evaluate('document.getElementById("toggle-representation").click()');
 check('mobile graph toggle',await evaluate('!document.getElementById("graph-stage").hidden'));
 await evaluate('document.getElementById("toggle-representation").click()');
 check('mobile page width',await evaluate('document.documentElement.scrollWidth<=window.innerWidth+1'),await evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth})'));
 const figures=await evaluate('Array.from(document.images).every(i=>i.complete&&i.naturalWidth>0)');check('local figures load',figures);
 check('no uncaught JavaScript exceptions',exceptions.length===0,exceptions);
 const sourceHashes={};for(const file of ['graph.json','interactive/index.html','interactive/app.js','interactive/style.css','interactive/data.js','check_browser.mjs'])sourceHashes[file]=createHash('sha256').update(await readFile(path.join(here,file))).digest('hex');
 await writeFile(path.join(here,'browser-checks.json'),JSON.stringify({command:'node knowledge/check_browser.mjs',browser:executable,browserVersion,node:process.version,source_hashes:sourceHashes,transport:'Local file URL; isolated headless profile; loopback CDP',results,exceptions,passed:true},null,2)+'\n');
 console.log(JSON.stringify({checks:results.length,passed:true,screenshots:['atlas-overview','atlas-provenance','atlas-literature','atlas-geometry','atlas-dependencies','atlas-mobile']},null,2));
}finally{
 try{await call('Browser.close');}catch{}
 ws.close();child.kill();
}
