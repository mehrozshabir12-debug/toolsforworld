/* Tools for World file tools: everything runs in the browser, files never leave the device. */
const $=s=>document.querySelector(s);
const I={pdf:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg>'};
/* Libraries load only when a tool needs them (pinned versions + Subresource Integrity). */
const LIB={
 pdflib:['https://cdnjs.cloudflare.com/ajax/libs/pdf-lib/1.17.1/pdf-lib.min.js','sha384-weMABwrltA6jWR8DDe9Jp5blk+tZQh7ugpCsF3JwSA53WZM9/14PjS5LAJNHNjAI'],
 pdfjs:['https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js','sha384-/1qUCSGwTur9vjf/z9lmu/eCUYbpOTgSjmpbMQZ1/CtX2v/WcAIKqRv+U1DUCG6e'],
 mammoth:['https://cdn.jsdelivr.net/npm/mammoth@1.8.0/mammoth.browser.min.js','sha384-/cXAMbzovUIKbBERjPmR3SnPTh8siWr5lsvFYj1Uq4XP0yaJUZJmsh0YXyGv5P0y'],
 h2pdf:['https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js','sha384-Yv5O+t3uE3hunW8uyrbpPW3iw6/5/Y7HitWJBLgqfMoA36NogMmy+8wWZMpn3HWc'],
 tess:['https://cdn.jsdelivr.net/npm/tesseract.js@5.1.0/dist/tesseract.min.js','sha384-1zP4ZOtlk2FXAOiUArpMuWf7INJJKe/ROfYFAVSeUa11DEfXdKWGiPI3dVma2Gt0'],
 heic:['https://cdn.jsdelivr.net/npm/heic2any@0.0.4/dist/heic2any.min.js','sha384-OTofQ0MEeiSgh62havBcemCIK0gqj809wX6UA0uPISNMRnR6NZyCdGzX3SbLrgwL'],
 lame:['https://cdn.jsdelivr.net/npm/lamejs@1.2.1/lame.min.js','sha384-xuasJXVcyv3hZq0eYpelEkBC8l4yufatZXDsKuyCU2rqfhDCb+ftuE/mSfZAteiK'],
 jszip:['https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js','sha384-+mbV2IY1Zk/X1p/nWllGySJSUN8uMs+gUAN10Or95UBH0fpj6GfKgPmgC5EXieXG']
};
const PDFWORKER='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
const NET_ERR='A part of this tool could not load. Check your internet connection and try again.';
const libP={};
function need(...names){return Promise.all(names.map(n=>libP[n]||(libP[n]=new Promise((res,rej)=>{
  const sc=document.createElement('script');sc.src=LIB[n][0];sc.integrity=LIB[n][1];sc.crossOrigin='anonymous';
  sc.onload=res;sc.onerror=()=>{delete libP[n];sc.remove();rej(new Error(NET_ERR))};document.head.appendChild(sc)}))))}

const IMG_EXT=['jpg','jpeg','jfif','png','webp','gif','bmp','avif'];
const TOOLS={
 compress:{accept:'image/*',exts:IMG_EXT,multi:true,go:'Compress',fmt:'JPG, PNG, WebP, GIF, BMP',warn:40},
 resize:{accept:'image/*',exts:IMG_EXT,multi:true,go:'Resize',fmt:'JPG, PNG, WebP, GIF, BMP',warn:40},
 convert:{accept:'image/*',exts:IMG_EXT,multi:true,go:'Convert',fmt:'JPG, PNG, WebP',warn:40},
 passport:{accept:'image/*',exts:IMG_EXT,multi:false,go:'Make sheet',fmt:'JPG, PNG, WebP',warn:40},
 img2pdf:{accept:'image/jpeg,image/png,image/webp',exts:['jpg','jpeg','jfif','png','webp'],multi:true,go:'Create PDF',libs:['pdflib'],fmt:'JPG, PNG, WebP',warn:40},
 merge:{accept:'application/pdf',exts:['pdf'],multi:true,go:'Merge PDFs',libs:['pdflib'],fmt:'PDF',warn:200},
 split:{accept:'application/pdf',exts:['pdf'],multi:false,go:'Split PDF',libs:['pdflib'],fmt:'PDF',warn:200},
 pdf2jpg:{accept:'application/pdf',exts:['pdf'],multi:false,go:'Convert to JPG',libs:['pdfjs'],fmt:'PDF',warn:150},
 word2pdf:{accept:'application/vnd.openxmlformats-officedocument.wordprocessingml.document,.docx',exts:['docx'],multi:false,go:'Convert to PDF',libs:['mammoth','h2pdf'],fmt:'Word .docx',warn:40},
 png2jpg:{accept:'image/png',exts:['png'],multi:true,go:'Convert to JPG',fmt:'PNG',warn:40},
 jpg2png:{accept:'image/jpeg',exts:['jpg','jpeg','jfif'],multi:true,go:'Convert to PNG',fmt:'JPG / JPEG',warn:40},
 webp2jpg:{accept:'image/webp',exts:['webp'],multi:true,go:'Convert to JPG',fmt:'WebP',warn:40},
 heic2jpg:{accept:'image/heic,image/heif,.heic,.heif',exts:['heic','heif'],multi:true,go:'Convert to JPG',libs:['heic'],fmt:'HEIC / HEIF (iPhone photos)',warn:40},
 pdfcompress:{accept:'application/pdf',exts:['pdf'],multi:false,go:'Compress PDF',libs:['pdflib','pdfjs'],fmt:'PDF',warn:150},
 ocr:{accept:'image/*',exts:IMG_EXT,multi:false,go:'Extract text',libs:['tess'],fmt:'JPG, PNG, WebP, BMP',warn:30},
 bgremove:{accept:'image/*',exts:IMG_EXT,multi:false,go:'Remove background',fmt:'JPG, PNG, WebP',warn:30},
 mp4mp3:{accept:'video/*,audio/*,.mp4,.m4a,.mov,.webm,.mkv',exts:['mp4','m4a','mov','webm','mkv','m4v','3gp','mp3','wav','ogg','aac'],multi:false,go:'Convert to MP3',libs:['lame'],fmt:'MP4, MOV, WebM, M4A',warn:300},
 pdf2word:{accept:'application/pdf',exts:['pdf'],multi:false,go:'Convert to Word',libs:['pdfjs','jszip'],fmt:'PDF',warn:150}
};
let cur=null, files=[], outs=[], results=[], thumbs=[];
const kb=n=>n<1048576?(n/1024).toFixed(0)+' KB':(n/1048576).toFixed(2)+' MB';
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const base=n=>n.replace(/\.[^.]+$/,'');
const extOf=n=>(n.match(/\.([^.]+)$/)||['',''])[1].toLowerCase();
function status(t,err,html){const s=$('#status');if(html)s.innerHTML=t;else s.textContent=t||'';s.className='note'+(err?' err':'');prog(t)}
/* progress bar: follows "45%" or "page 3 of 10" in status messages */
function prog(t){const p=$('#prog');if(!p||p.hidden)return;const m=/(\d+)%/.exec(t||'')||null,n=/(\d+) of (\d+)/.exec(t||'');
  if(m)p.value=Math.min(100,+m[1]);else if(n)p.value=Math.round(+n[1]/+n[2]*100);else p.removeAttribute('value')}
/* raw browser errors become a plain-language message */
function friendly(e){const m=(e&&e.message)||'';
  if(/allocation failed|out of memory|Array buffer allocation|Invalid array length|Maximum call stack|Invalid string length/i.test(m))return 'This file is too large for this device to process. Try a smaller file, or use a computer.';
  if(!m||/undefined|null|Cannot read|is not a function|is not defined|Failed to execute|Overload|TypeError|RangeError|\[object/i.test(m))return 'Something went wrong with this file. It may be damaged or in an unusual format. Try another file.';
  return m}

/* canvas limits: iPhone/iPad Safari fails above ~16.7 million pixels; others above ~268M (we stay well below) */
const IOS=/iP(hone|ad|od)/.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
const MAXPX=IOS?16.7e6:(navigator.maxTouchPoints>0?60e6:120e6),MAXSIDE=IOS?8192:32000;
let shrunk='';
function fitLimit(w,h){let s=Math.min(1,Math.sqrt(MAXPX/(w*h)),MAXSIDE/w,MAXSIDE/h);if(s<1){const W=Math.max(1,Math.floor(w*s)),H=Math.max(1,Math.floor(h*s));shrunk=` Reduced to ${W}×${H} px, the largest size this device can process.`;return[W,H]}return[w,h]}

function addFiles(list){
  const t=TOOLS[cur];list=[...list];
  const heic=f=>/^image\/hei[cf]/.test(f.type)||/^hei[cf]$/.test(extOf(f.name));
  if(cur!=='heic2jpg'&&list.some(heic)){
    status(`iPhone HEIC photos can't be opened here directly. Convert them with <a href="../heic-to-jpg/">HEIC to JPG</a> first, then come back.`,true,true);
    list=list.filter(f=>!heic(f));if(!list.length)return}
  const ok=f=>t.accept.split(',').some(a=>a.startsWith('.')?f.name.toLowerCase().endsWith(a):a.endsWith('/*')?f.type.startsWith(a.slice(0,-1)):f.type===a)||(!f.type||f.type==='application/octet-stream')&&(t.exts||[]).includes(extOf(f.name));
  const added=list.filter(ok);
  if(!added.length){status(`That file type is not supported here. Supported: ${t.fmt}.`,true);return}
  files=t.multi?files.concat(added):[added[0]];
  const big=files.filter(f=>f.size>t.warn*1048576);
  status(added.length<list.length?`Some files were skipped (not ${t.fmt}).`:big.length?`Large file (${kb(big[0].size)}): this may be slow on phones. A computer works best.`:'');
  render();
  if(cur==='passport')ppLoad().catch(e=>{files=[];ppImg=null;render();status((e.message||'Could not read this photo.')+' Choose a JPG or PNG photo.',true)});
  if(t.libs)need(...t.libs).catch(()=>{});            // start downloading the converter early
}
$('#fin').addEventListener('change',e=>{addFiles(e.target.files);e.target.value=''});
const drop=$('#drop');
['dragenter','dragover'].forEach(ev=>drop.addEventListener(ev,e=>{e.preventDefault();drop.classList.add('over')}));
['dragleave','drop'].forEach(ev=>drop.addEventListener(ev,e=>{e.preventDefault();drop.classList.remove('over')}));
drop.addEventListener('drop',e=>addFiles(e.dataTransfer.files));
drop.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();$('#fin').click()}});
function clearOut(){outs.forEach(u=>URL.revokeObjectURL(u));outs=[];results=[];$('#out').innerHTML=''}
$('#clear').onclick=()=>{files=[];ppImg=null;clearOut();status('');render()};

function render(){
  $('#panel').hidden=!files.length;
  thumbs.forEach(u=>URL.revokeObjectURL(u));thumbs=[];
  const L=$('#list');L.innerHTML='';
  const reorder=['img2pdf','merge'].includes(cur);
  files.forEach((f,i)=>{
    const d=document.createElement('div');d.className='file';
    let th=`<span class="ic" style="color:var(--accent)">${I.pdf}</span>`;
    if(f.type.startsWith('image/')&&f.size<25e6){const u=URL.createObjectURL(f);thumbs.push(u);th=`<img alt="" src="${u}">`}
    d.innerHTML=`${th}<span class="nm">${esc(f.name)}</span><span class="sz">${kb(f.size)}</span>`+
      (reorder?`<button class="mv" aria-label="Move up" data-u="${i}">▲</button><button class="mv" aria-label="Move down" data-d="${i}">▼</button>`:'')+
      `<button class="x" aria-label="Remove ${esc(f.name)}" data-x="${i}">×</button>`;
    L.appendChild(d);
  });
  L.querySelectorAll('[data-x]').forEach(b=>b.onclick=()=>{files.splice(+b.dataset.x,1);if(cur==='passport')ppImg=null;render()});
  L.querySelectorAll('[data-u]').forEach(b=>b.onclick=()=>{const i=+b.dataset.u;if(i>0){[files[i-1],files[i]]=[files[i],files[i-1]];render()}});
  L.querySelectorAll('[data-d]').forEach(b=>b.onclick=()=>{const i=+b.dataset.d;if(i<files.length-1){[files[i+1],files[i]]=[files[i],files[i+1]];render()}});
  $('#go').disabled=!files.length||(cur==='merge'&&files.length<2);
  if(cur==='merge'&&files.length===1)status('Add at least one more PDF to merge.');
}

function renderOpts(){
  const o=$('#opts');
  const fmt=(id,def)=>`<label>Format <select id="${id}"><option value="image/jpeg"${def==='jpg'?' selected':''}>JPG</option><option value="image/png"${def==='png'?' selected':''}>PNG</option><option value="image/webp"${def==='webp'?' selected':''}>WebP</option></select></label>`;
  o.innerHTML={
   compress:`<div class="row"><label>Quality <input type="range" id="q" min="10" max="95" value="70"> <span id="qv" class="sz">70%</span></label><label>Max width <input type="number" id="mw" placeholder="Original" min="50"> px</label><label>Output <select id="cf"><option value="image/jpeg">JPG</option><option value="image/webp">WebP</option></select></label></div><div class="row"><label>Target size <input type="number" id="tkb" placeholder="Any" min="5" step="1"> KB</label><span class="note">Set a target (like 100) and the photo is made just under that size. Quality is then chosen for you.</span></div>`,
   resize:`<div class="row"><label><select id="rm" aria-label="Resize by"><option value="px">Pixels</option><option value="pc">Percent</option></select></label><label>Width <input type="number" id="rw" min="1" max="20000"></label><label>Height <input type="number" id="rh" min="1" max="20000"></label><label><input type="checkbox" id="rk" checked> Keep ratio</label><label>If the shape differs <select id="rf"><option value="crop">Crop to fill</option><option value="pad">Fit with white border</option><option value="stretch">Stretch</option></select></label><label>Percent <input type="number" id="rp" value="50" min="1" max="1000"> %</label></div><p class="note">With "Keep ratio", fill only width or height and the other is calculated for each image.</p>`,
   convert:`<div class="row">${fmt('tf','png')}<label>Quality <input type="range" id="tq" min="10" max="100" value="92"></label></div>`,
   passport:`<div class="pp"><canvas id="ppc" width="350" height="450" aria-label="Passport photo preview"></canvas><div class="panel" style="margin:0">
     <label>Size <select id="ps"><option value="35x45">35 × 45 mm (UK, EU, Australia, India, Pakistan)</option><option value="50.8x50.8">2 × 2 in (USA)</option><option value="50x70">50 × 70 mm (Canada)</option><option value="33x48">33 × 48 mm (China visa)</option><option value="40x50">40 × 50 mm</option><option value="30x40">30 × 40 mm</option></select></label>
     <label>Zoom <input type="range" id="pz" min="100" max="400" value="100"></label>
     <label>Left / right <input type="range" id="px" min="-100" max="100" value="0"></label>
     <label>Up / down <input type="range" id="py" min="-100" max="100" value="0"></label>
     <label>Copies on 4×6 sheet <select id="pn"><option>4</option><option selected>6</option><option>8</option></select></label>
     <p class="note">Line guides: the top of the head near the upper line, the chin near the lower line.</p></div></div>`,
   img2pdf:`<div class="row"><label>Page <select id="pg"><option value="a4">A4</option><option value="letter">Letter</option><option value="fit">Same as image</option></select></label><label>Margin <select id="pm"><option value="0">None</option><option value="20" selected>Small</option><option value="40">Large</option></select></label></div>`,
   word2pdf:`<div class="row"><label>Page <select id="wp"><option value="a4">A4</option><option value="letter">Letter</option><option value="legal">Legal</option></select></label><label>Orientation <select id="wo"><option value="portrait">Portrait</option><option value="landscape">Landscape</option></select></label></div><p class="note">Best for simple documents (text, headings, lists, small tables, pictures). Complex layouts may look slightly different.</p>`,
   merge:'',
   split:`<div class="row"><label><input type="radio" name="sm" value="range" checked> Pages</label><input type="text" id="sr" placeholder="e.g. 1-3, 5, 8-10" aria-label="Pages to extract"><label><input type="radio" name="sm" value="each"> Every page as a separate PDF</label></div>`,
   pdf2jpg:`<div class="row"><label>Quality <select id="dq"><option value="1.5">Normal</option><option value="2" selected>High</option><option value="3">Very high</option></select></label></div>`
  }[cur]||(OPTX[cur]||'');
  if(cur==='compress'){const q=$('#q');q.oninput=()=>$('#qv').textContent=q.value+'%'}
  if(cur==='passport'){['ps','pz','px','py'].forEach(id=>$('#'+id).oninput=ppDraw)}
}

function addOut(blob,name){
  if(!blob||!blob.size)throw new Error('This file is too large for this device to process. Try a smaller size or file.');
  const u=URL.createObjectURL(blob);outs.push(u);results.push({blob,name});
  const d=document.createElement('div');d.className='file';
  const th=blob.type.startsWith('image/')?`<img alt="" src="${u}">`:`<span class="ic" style="color:var(--accent)">${I.pdf}</span>`;
  d.innerHTML=`${th}<span class="nm">${esc(name)}</span><span class="sz">${kb(blob.size)}</span><a class="save" href="${u}" download="${esc(name)}">Download</a>`;
  $('#out').appendChild(d);
}
const loadImg=f=>new Promise((res,rej)=>{const i=new Image(),u=URL.createObjectURL(f);i.onload=()=>{URL.revokeObjectURL(u);res(i)};i.onerror=()=>{URL.revokeObjectURL(u);rej(new Error(`Could not read ${f.name}. The image may be damaged or in an unsupported format.`))};i.src=u});
const toBlob=(c,type,q)=>new Promise((res,rej)=>c.toBlob(b=>b?res(b):rej(new Error('This image is too large for this device to process. Try a smaller size.')),type,q));
function draw(img,w,h,type){[w,h]=fitLimit(w,h);const c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');if(!x)throw new Error('This image is too large for this device to process.');if(type==='image/jpeg'){x.fillStyle='#fff';x.fillRect(0,0,w,h)}x.drawImage(img,0,0,w,h);return c}
const ext={'image/jpeg':'jpg','image/png':'png','image/webp':'webp'};

/* "Download all" as one ZIP when a tool makes several files */
async function zipAll(){const b=$('#zipall');b.disabled=true;b.textContent='Zipping…';
  try{await need('jszip');const z=new JSZip(),seen={};for(const r of results){let n=r.name;if(seen[n]){n=base(n)+'-'+(++seen[n])+'.'+extOf(n)}else seen[n]=1;z.file(n,r.blob)}
    const blob=await z.generateAsync({type:'blob'}),a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=(files[0]?base(files[0].name):'files')+'-all.zip';document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(a.href),60000)}
  catch(e){status(friendly(e),true)}b.disabled=false;b.textContent=`Download all (${results.length} files, .zip)`}

$('#go').onclick=async()=>{
  const go=$('#go'),label=go.textContent,p=$('#prog');go.disabled=true;go.textContent='Working…';clearOut();shrunk='';
  if(p){p.hidden=false;p.removeAttribute('value')}const t0=Date.now();status('Working…');
  try{const t=TOOLS[cur];if(t.libs){status('Loading the converter…');await need(...t.libs)}
    await RUN[cur]();
    const st=$('#status').textContent,keep=/→|smaller|already|fit on|under/.test(st);
    status((keep?(/^Done/.test(st)?st:'Done. '+st):'Done. Your files are ready below.')+shrunk);
    if(results.length>1){const b=document.createElement('button');b.className='btn ghost';b.id='zipall';b.type='button';b.textContent=`Download all (${results.length} files, .zip)`;b.onclick=zipAll;$('#out').appendChild(b)}
    try{if(window.TFW)TFW.used()}catch(e){}
  }catch(e){console.error(e);status(friendly(e),true)}
  if(p)p.hidden=true;go.textContent=label;go.disabled=false;
  if(results.length&&Date.now()-t0>1500)$('#out').scrollIntoView({behavior:'smooth',block:'nearest'});
};
const RUN={
 async compress(){
  const q=$('#q').value/100,mw=+$('#mw').value||0,type=$('#cf').value,target=(+$('#tkb').value||0)*1024;
  for(const f of files){const i=await loadImg(f);let w=i.naturalWidth,h=i.naturalHeight;if(mw&&w>mw){h=Math.round(h*mw/w);w=mw}
   let b;
   if(target){ // best quality (and size, if needed) that fits under the target
     let best=null;
     for(let pass=0;pass<12&&!best;pass++){
       const c=draw(i,w,h,type);let lo=0.05,hi=0.95;
       const low=await toBlob(c,type,lo);
       if(low.size<=target){best=low;for(let k=0;k<7;k++){const mid=(lo+hi)/2,t=await toBlob(c,type,mid);if(t.size<=target){best=t;lo=mid}else hi=mid}}
       else{w=Math.max(16,Math.round(w*0.82));h=Math.max(16,Math.round(h*0.82))}
     }
     b=best||await toBlob(draw(i,w,h,type),type,0.05);
   } else b=await toBlob(draw(i,w,h,type),type,q);
   if(b.size>=f.size&&(!mw||i.naturalWidth<=mw)&&(!target||f.size<=target)){   // never hand back a bigger "compressed" file
     addOut(f,f.name);status(`${f.name} is already ${kb(f.size)}: compressing would make it bigger, so the original is kept.`);continue}
   addOut(b,base(f.name)+'-compressed.'+ext[type]);
   status(`${f.name}: ${kb(f.size)} → ${kb(b.size)}${target?` (target ${Math.round(target/1024)} KB, ${w}×${h})`:''}`)}
 },
 async resize(){
  const m=$('#rm').value,W=+$('#rw').value,H=+$('#rh').value,k=$('#rk').checked,p=+$('#rp').value/100;
  if(m==='px'&&!W&&!H)throw new Error('Enter a width or a height.');
  if(m==='px'&&[W,H].some(v=>v&&(v<1||v>20000||!Number.isFinite(v))))throw new Error('Width and height must be between 1 and 20,000 pixels.');
  if(m==='pc'&&!(p>=0.01&&p<=10))throw new Error('Percent must be between 1 and 1000.');
  for(const f of files){const i=await loadImg(f),r=i.naturalWidth/i.naturalHeight;let w,h;
   if(m==='pc'){w=i.naturalWidth*p;h=i.naturalHeight*p}
   else if(k){w=W||H*r;h=W?W/r:H}else{w=W||i.naturalWidth;h=H||i.naturalHeight}
   w=Math.max(1,Math.round(w));h=Math.max(1,Math.round(h));
   if(w*h>MAXPX||w>MAXSIDE||h>MAXSIDE)throw new Error(`${w}×${h} px is too large for this device to create. Choose a smaller size.`);
   const type=f.type==='image/png'?'image/png':f.type==='image/webp'?'image/webp':'image/jpeg';
   let c;const fit=$('#rf').value;
   if(m==='px'&&!k&&W&&H&&fit!=='stretch'){
     c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,w,h);
     const sc=fit==='crop'?Math.max(w/i.naturalWidth,h/i.naturalHeight):Math.min(w/i.naturalWidth,h/i.naturalHeight);
     const dw=i.naturalWidth*sc,dh=i.naturalHeight*sc;x.drawImage(i,(w-dw)/2,(h-dh)/2,dw,dh);
   } else c=draw(i,w,h,type);
   addOut(await toBlob(c,type,.92),`${base(f.name)}-${w}x${h}.${ext[type]}`)}
 },
 async convert(){
  const type=$('#tf').value,q=$('#tq').value/100;
  for(const f of files){const i=await loadImg(f);addOut(await toBlob(draw(i,i.naturalWidth,i.naturalHeight,type),type,q),base(f.name)+'.'+ext[type])}
 },
 async passport(){
  if(!ppImg)throw new Error('The photo could not be read. Choose a JPG or PNG photo.');
  const one=ppCanvas(600);const want=+$('#pn').value;
  const [mw,mh]=ppSize(),dpi=300,pw=Math.round(mw/25.4*dpi),ph=Math.round(mh/25.4*dpi),gap=0;
  // 4x6 inch sheet at 300 dpi: pick the orientation that fits the most photos
  const fit=(W,H)=>{const c=Math.floor((W-gap)/(pw+gap)),r=Math.floor((H-gap)/(ph+gap));return{W,H,c,r,n:c*r}};
  const L=fit(1800,1200),P=fit(1200,1800),o=P.n>L.n?P:L;
  let cols=o.c,rows=o.r;while(cols*rows>want){if(cols>=rows&&cols>1)cols--;else if(rows>1)rows--;else break}
  const S=document.createElement('canvas');S.width=o.W;S.height=o.H;const x=S.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,o.W,o.H);
  const gx=(o.W-cols*pw)/(cols+1),gy=(o.H-rows*ph)/(rows+1);
  for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){const X=gx+c*(gx+pw),Y=gy+r*(gy+ph);x.drawImage(one,X,Y,pw,ph);x.strokeStyle='#bbb';x.lineWidth=1;x.strokeRect(X,Y,pw,ph)}
  if(cols*rows<want)setTimeout(()=>status(`Done. ${cols*rows} photos of this size fit on a 4×6 sheet.`),0);
  addOut(await toBlob(ppCanvas(Math.round(mw/25.4*dpi)),'image/jpeg',.95),'passport-photo.jpg');
  addOut(await toBlob(S,'image/jpeg',.95),'passport-sheet-4x6.jpg');
 },
 async img2pdf(){
  const {PDFDocument}=PDFLib,doc=await PDFDocument.create(),pg=$('#pg').value,mg=+$('#pm').value;
  const sizes={a4:[595.28,841.89],letter:[612,792]};
  for(const f of files){
   let bytes=await f.arrayBuffer(),em;
   if(f.type==='image/png')em=await doc.embedPng(bytes);
   else if(f.type==='image/jpeg')em=await doc.embedJpg(bytes);
   else{const i=await loadImg(f);const b=await toBlob(draw(i,i.naturalWidth,i.naturalHeight,'image/jpeg'),'image/jpeg',.92);em=await doc.embedJpg(await b.arrayBuffer())}
   let [W,H]=pg==='fit'?[em.width+mg*2,em.height+mg*2]:sizes[pg];
   if(pg!=='fit'&&em.width>em.height)[W,H]=[H,W];
   const s=Math.min((W-mg*2)/em.width,(H-mg*2)/em.height),w=em.width*s,h=em.height*s;
   doc.addPage([W,H]).drawImage(em,{x:(W-w)/2,y:(H-h)/2,width:w,height:h});
  }
  addOut(new Blob([await doc.save()],{type:'application/pdf'}),'images.pdf');
 },
 async merge(){
  const {PDFDocument}=PDFLib,out=await PDFDocument.create();
  for(const f of files){let src;try{src=await PDFDocument.load(await f.arrayBuffer())}catch(e){throw new Error(f.name+' is password-protected or damaged.')}
   (await out.copyPages(src,src.getPageIndices())).forEach(p=>out.addPage(p))}
  addOut(new Blob([await out.save()],{type:'application/pdf'}),'merged.pdf');
 },
 async split(){
  const {PDFDocument}=PDFLib,f=files[0];let src;
  try{src=await PDFDocument.load(await f.arrayBuffer())}catch(e){throw new Error('This PDF is password-protected or damaged.')}
  const n=src.getPageCount(),mode=document.querySelector('input[name=sm]:checked').value;
  const make=async(idx,name)=>{const d=await PDFDocument.create();(await d.copyPages(src,idx)).forEach(p=>d.addPage(p));addOut(new Blob([await d.save()],{type:'application/pdf'}),name)};
  if(mode==='each'){for(let i=0;i<n;i++)await make([i],`${base(f.name)}-page-${i+1}.pdf`);return}
  const idx=[];for(const part of $('#sr').value.split(',')){const m=part.trim().match(/^(\d+)\s*(?:-\s*(\d+))?$/);if(!m)continue;
   let a=+m[1],b=+(m[2]||m[1]);if(a>b)[a,b]=[b,a];for(let i=a;i<=b;i++)if(i>=1&&i<=n&&!idx.includes(i-1))idx.push(i-1)}
  if(!idx.length)throw new Error(`Enter pages between 1 and ${n}, like 1-3, 5.`);
  await make(idx,`${base(f.name)}-pages.pdf`);
 },
 async pdf2jpg(){
  pdfjsLib.GlobalWorkerOptions.workerSrc=PDFWORKER;
  const f=files[0],sc=+$('#dq').value;let pdf;
  try{pdf=await pdfjsLib.getDocument({data:await f.arrayBuffer()}).promise}catch(e){throw new Error('This PDF is password-protected or damaged.')}
  for(let p=1;p<=pdf.numPages;p++){status(`Page ${p} of ${pdf.numPages}…`);const pg=await pdf.getPage(p),vp=pg.getViewport({scale:sc});
   const c=document.createElement('canvas');c.width=vp.width;c.height=vp.height;const x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,c.width,c.height);
   await pg.render({canvasContext:x,viewport:vp}).promise;addOut(await toBlob(c,'image/jpeg',.92),`${base(f.name)}-page-${p}.jpg`)}
 }
};

/* passport */
let ppImg=null;
const ppSize=()=>$('#ps').value.split('x').map(Number);
async function ppLoad(){ppImg=null;$('#go').disabled=true;ppImg=await loadImg(files[0]);$('#go').disabled=false;ppDraw()}
function ppCanvas(w){
  const [mw,mh]=ppSize(),h=Math.round(w*mh/mw),c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');
  x.fillStyle='#fff';x.fillRect(0,0,w,h);if(!ppImg)return c;
  const z=$('#pz').value/100,base=Math.max(w/ppImg.naturalWidth,h/ppImg.naturalHeight)*z,dw=ppImg.naturalWidth*base,dh=ppImg.naturalHeight*base;
  const ox=(w-dw)/2+($('#px').value/100)*(dw/2),oy=(h-dh)/2+($('#py').value/100)*(dh/2);
  x.drawImage(ppImg,ox,oy,dw,dh);return c;
}
function ppDraw(){
  const cv=$('#ppc');if(!cv)return;const [mw,mh]=ppSize();cv.width=350;cv.height=Math.round(350*mh/mw);
  const x=cv.getContext('2d');x.drawImage(ppCanvas(350),0,0);
  x.strokeStyle='rgba(13,122,85,.85)';x.setLineDash([6,5]);x.lineWidth=1.5;
  [0.1,0.8].forEach(f=>{x.beginPath();x.moveTo(0,cv.height*f);x.lineTo(cv.width,cv.height*f);x.stroke()});
  x.beginPath();x.moveTo(cv.width/2,0);x.lineTo(cv.width/2,cv.height);x.stroke();
}


/* keep only safe markup from a document (no scripts, event handlers or javascript: links) */
function clean(html){const d=new DOMParser().parseFromString(html,'text/html');
  d.querySelectorAll('script,iframe,object,embed,style,link,meta,form,base').forEach(e=>e.remove());
  d.querySelectorAll('*').forEach(e=>[...e.attributes].forEach(a=>{const n=a.name.toLowerCase(),v=a.value.trim().toLowerCase();
    if(n.startsWith('on')||((n==='href'||n==='src'||n==='xlink:href')&&/^(javascript|vbscript|data:(?!image\/))/.test(v)))e.removeAttribute(a.name)}));
  return d.body.innerHTML}

/* Word (.docx) to PDF: mammoth turns the document into HTML, html2pdf draws it on A4 pages. */
RUN.word2pdf=async function(){
  const f=files[0];
  if(!/\.docx$/i.test(f.name))throw new Error('Please choose a .docx file (older .doc files: open in Word and "Save as" .docx first).');
  let res;
  try{res=await mammoth.convertToHtml({arrayBuffer:await f.arrayBuffer()})}catch(e){throw new Error('Could not read this Word file. It may be damaged or password-protected.')}
  const html=clean(res.value)||'<p>(empty document)</p>';
  const pv=$('#doc-preview');pv.hidden=false;pv.innerHTML=html;
  // page geometry (mm) -> content width in CSS px, so we can measure where pages fall
  const fmt=$('#wp').value,land=$('#wo').value==='landscape',M=[12,12,14,12];
  let [W,H]={a4:[210,297],letter:[215.9,279.4],legal:[215.9,355.6]}[fmt];if(land)[W,H]=[H,W];
  const iw=W-M[1]-M[3],ih=H-M[0]-M[2],wpx=Math.round(iw*96/25.4),P=wpx*ih/iw;
  const box=document.createElement('div');box.className='docrender';box.style.cssText=`position:absolute;left:-99999px;top:0;width:${wpx}px`;box.innerHTML=html;document.body.appendChild(box);
  await Promise.all([...box.querySelectorAll('img')].map(im=>im.complete?0:new Promise(r=>{im.onload=im.onerror=r})));
  // split the document into chunks of about 4 pages, ending each chunk where its last page is nearly full.
  // (one huge canvas fails on long documents: browsers cap canvas height)
  const kids=[...box.children],tops=kids.map(k=>k.offsetTop),ends=kids.map(k=>k.offsetTop+k.offsetHeight),groups=[];
  let start=0;
  while(start<kids.length){
    const t0=tops[start];let best=start,bestFill=-1,last=start;
    for(let k=start;k<kids.length;k++){const h=ends[k]-t0;if(h>5*P&&k>start)break;last=k;
      const fill=(h%P)/P;if(h>=2.5*P&&fill>bestFill){bestFill=fill;best=k}}
    if(bestFill<0)best=last;                       // short tail, or the next block is very tall
    groups.push(kids.slice(start,best+1));start=best+1}
  box.remove();
  const chunks=groups.map(g=>{const d=document.createElement('div');d.className='docrender';g.forEach(n=>d.appendChild(n));return d});
  const scale=IOS?1.6:2;
  const opt={margin:M,image:{type:'jpeg',quality:.92},html2canvas:{scale,useCORS:true,backgroundColor:'#ffffff'},jsPDF:{unit:'mm',format:fmt,orientation:land?'landscape':'portrait'},pagebreak:{mode:['css','legacy']}};
  status(`Making PDF… part 1 of ${chunks.length}`);
  let w=html2pdf().set(opt).from(chunks[0]).toPdf();
  chunks.slice(1).forEach((c,i)=>{w=w.get('pdf').then(pdf=>{status(`Making PDF… part ${i+2} of ${chunks.length}`);pdf.addPage()}).from(c).toContainer().toCanvas().toPdf()});
  const blob=await w.outputPdf('blob');
  addOut(blob,base(f.name)+'.pdf');
  $('#printbtn').hidden=false;
};

/* ------------------------------------------------------------------ more tools */
const OPTX={
 png2jpg:`<div class="row"><label>Quality <input type="range" id="tq" min="10" max="100" value="92"></label><span class="note">Transparent areas become white.</span></div>`,
 jpg2png:'',
 webp2jpg:`<div class="row"><label>Quality <input type="range" id="tq" min="10" max="100" value="92"></label></div>`,
 heic2jpg:`<div class="row"><label>Quality <input type="range" id="tq" min="10" max="100" value="92"></label><span class="note">iPhone photos (.heic). Conversion can take a few seconds per photo.</span></div>`,
 pdfcompress:`<div class="row"><label>Level <select id="pc"><option value="150|0.75">Recommended (150 dpi)</option><option value="110|0.6" selected>Strong (110 dpi)</option><option value="200|0.85">Light (200 dpi)</option><option value="80|0.5">Extreme (80 dpi)</option></select></label><label>Target size <input type="number" id="ptkb" placeholder="Any" min="20" step="1"> KB</label></div><p class="note">Set a target (like 200) and the best level that fits under it is chosen for you. Best for scanned PDFs and PDFs full of photos. Pages are re-saved as images, so text can no longer be selected or searched.</p>`,
 ocr:`<div class="row"><label>Language <select id="ol"><option value="eng">English</option><option value="urd">Urdu</option><option value="eng+urd">English + Urdu</option><option value="ara">Arabic</option><option value="hin">Hindi</option><option value="spa">Spanish</option><option value="fra">French</option><option value="deu">German</option><option value="por">Portuguese</option><option value="ita">Italian</option><option value="rus">Russian</option><option value="tur">Turkish</option><option value="ben">Bengali</option><option value="ind">Indonesian</option><option value="chi_sim">Chinese (Simplified)</option></select></label></div><p class="note">The first run downloads the language data (about 10–20 MB). Clear, straight photos give the best results.</p><textarea id="ocrout" rows="10" style="width:100%;font:inherit;padding:10px;border-radius:10px;border:1px solid var(--line);background:var(--sunk);color:var(--fg)" placeholder="Text will appear here" hidden></textarea><p><button class="btn ghost" id="ocrcopy" type="button" hidden>Copy text</button></p>`,
 bgremove:`<p class="note">An AI model runs inside your browser. The first run downloads it (about 40–80 MB), then it is cached. Works best on people, products and animals.</p>`,
 mp4mp3:`<div class="row"><label>Quality <select id="mb"><option value="128">128 kbps (small)</option><option value="192" selected>192 kbps</option><option value="320">320 kbps (best)</option></select></label></div><p class="note">Works with MP4, MOV, WebM, M4A and most videos your browser can play. Very long videos may be slow on phones.</p>`,
 pdf2word:`<p class="note">Copies the text and paragraphs of each page into an editable Word file. Pictures, columns and exact layout are not kept. Scanned PDFs have no text: use Image to Text (OCR) first.</p>`
};
const conv=type=>async function(){
  const q=($('#tq')||{value:92}).value/100;
  for(const f of files){const i=await loadImg(f);addOut(await toBlob(draw(i,i.naturalWidth,i.naturalHeight,type),type,q),base(f.name)+'.'+ext[type])}
};
RUN.png2jpg=conv('image/jpeg');RUN.jpg2png=conv('image/png');RUN.webp2jpg=conv('image/jpeg');

RUN.heic2jpg=async function(){
  const q=$('#tq').value/100;
  for(const f of files){status('Converting '+f.name+'…');
    let out;try{out=await heic2any({blob:f,toType:'image/jpeg',quality:q})}catch(e){throw new Error(f.name+' could not be read as a HEIC photo.')}
    (Array.isArray(out)?out:[out]).forEach((b,i,a)=>addOut(b,base(f.name)+(a.length>1?'-'+(i+1):'')+'.jpg'))}
};

RUN.pdfcompress=async function(){
  pdfjsLib.GlobalWorkerOptions.workerSrc=PDFWORKER;
  const f=files[0],target=(+($('#ptkb')||{}).value||0)*1024;
  let pdf;try{pdf=await pdfjsLib.getDocument({data:await f.arrayBuffer()}).promise}catch(e){throw new Error('This PDF is password-protected or damaged.')}
  const {PDFDocument}=PDFLib;
  const build=async(dpi,q,label)=>{const doc=await PDFDocument.create();
    for(let p=1;p<=pdf.numPages;p++){status(`${label}page ${p} of ${pdf.numPages}…`);
      const pg=await pdf.getPage(p),v1=pg.getViewport({scale:1}),vp=pg.getViewport({scale:dpi/72});
      const c=document.createElement('canvas');c.width=Math.ceil(vp.width);c.height=Math.ceil(vp.height);const x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,c.width,c.height);
      await pg.render({canvasContext:x,viewport:vp}).promise;
      const jpg=await doc.embedJpg(await (await toBlob(c,'image/jpeg',q)).arrayBuffer());
      doc.addPage([v1.width,v1.height]).drawImage(jpg,{x:0,y:0,width:v1.width,height:v1.height});c.width=c.height=0}
    return new Blob([await doc.save()],{type:'application/pdf'})};
  let out;
  if(target){
    if(f.size<=target){addOut(f,f.name);setTimeout(()=>status(`This PDF is already ${kb(f.size)}, under ${kb(target)}. No compression needed.`),0);return}
    // quality ladder from best to smallest; binary search for the best level that fits
    const L=[[200,.85],[170,.8],[150,.75],[130,.7],[110,.6],[96,.55],[84,.5],[72,.45],[60,.4],[50,.35],[42,.3],[36,.25]];
    let lo=0,hi=L.length-1,best=null,smallest=null,tries=0;
    while(lo<=hi){const m=(lo+hi)>>1;tries++;const b=await build(L[m][0],L[m][1],`Try ${tries}: `);
      if(!smallest||b.size<smallest.size)smallest=b;
      if(b.size<=target){best=b;hi=m-1}else lo=m+1}
    if(!best){addOut(smallest,base(f.name)+'-compressed.pdf');throw new Error(`Could not get under ${kb(target)}. The smallest possible is ${kb(smallest.size)}. Try a higher target or split the PDF into parts.`)}
    out=best;
  }else{const [dpi,q]=$('#pc').value.split('|').map(Number);out=await build(dpi,q,'')}
  if(out.size>=f.size){addOut(f,f.name);throw new Error(`This PDF is already well compressed (new size ${kb(out.size)} would not be smaller). Try a stronger level.`)}
  addOut(out,base(f.name)+'-compressed.pdf');
  setTimeout(()=>status(`${kb(f.size)} → ${kb(out.size)} (${Math.round((1-out.size/f.size)*100)}% smaller)`),0);
};

RUN.ocr=async function(){
  const lang=$('#ol').value,box=$('#ocrout');
  const img=await loadImg(files[0]);let w=img.naturalWidth,h=img.naturalHeight;const sc=Math.min(1,4000/Math.max(w,h));
  const cv=draw(img,Math.round(w*sc),Math.round(h*sc),'image/png');
  const r=await Tesseract.recognize(cv,lang,{logger:m=>{if(m.status)status(m.status.replace(/^./,c=>c.toUpperCase())+(m.progress?' '+Math.round(m.progress*100)+'%':''))}});
  const t=(r.data.text||'').trim();
  box.hidden=false;box.value=t||'(No text found. Try a clearer photo.)';box.dir=/urd|ara/.test(lang)?'rtl':'ltr';
  $('#ocrcopy').hidden=false;$('#ocrcopy').onclick=()=>{navigator.clipboard.writeText(box.value).then(()=>status('Copied.'),()=>{box.select();status('Press Ctrl+C to copy.')})};
  addOut(new Blob([t],{type:'text/plain'}),base(files[0].name)+'.txt');
};

RUN.bgremove=async function(){
  status('Loading the AI model (first time only)…');
  let mod,err;
  for(const v of ['1.7.0','1.5.8']){try{mod=await import(`https://cdn.jsdelivr.net/npm/@imgly/background-removal@${v}/+esm`);mod.__v=v;break}catch(e){err=e;console.warn('bg-removal',v,e)}}
  if(!mod)throw new Error('The background remover could not load ('+((err&&err.message)||'network')+'). Check your internet connection and try again.');
  const blob=await mod.removeBackground(files[0],{progress:(k,c,t)=>status((String(k).includes('fetch')?'Downloading AI model ':'Working ')+(t?Math.round(c/t*100)+'%':''))});
  addOut(blob,base(files[0].name)+'-no-background.png');
};

function floatTo16(f){const o=new Int16Array(f.length);for(let i=0;i<f.length;i++){const s=Math.max(-1,Math.min(1,f[i]));o[i]=s<0?s*0x8000:s*0x7FFF}return o}
RUN.mp4mp3=async function(){
  const f=files[0];status('Reading audio…');
  const AC=window.AudioContext||window.webkitAudioContext;let ac;try{ac=new AC({sampleRate:44100})}catch(e){ac=new AC()}
  if(f.size>300*1048576)status('Reading a large file. This can take a while and needs a lot of memory…');
  let buf;try{buf=await ac.decodeAudioData(await f.arrayBuffer())}catch(e){throw new Error('This file has no audio track your browser can read. Try another video.')}
  if(![8000,11025,12000,16000,22050,24000,32000,44100,48000].includes(buf.sampleRate))throw new Error('This audio sample rate is not supported by MP3. Try another file or browser.');
  const ch=Math.min(2,buf.numberOfChannels),sr=buf.sampleRate,enc=new lamejs.Mp3Encoder(ch,sr,+$('#mb').value),parts=[],L=floatTo16(buf.getChannelData(0)),R=ch>1?floatTo16(buf.getChannelData(1)):null,step=1152;
  for(let i=0;i<L.length;i+=step){const d=ch>1?enc.encodeBuffer(L.subarray(i,i+step),R.subarray(i,i+step)):enc.encodeBuffer(L.subarray(i,i+step));if(d.length)parts.push(new Uint8Array(d));
    if(i%(step*400)===0){status('Encoding '+Math.round(i/L.length*100)+'%');await new Promise(r=>setTimeout(r))}}
  const e=enc.flush();if(e.length)parts.push(new Uint8Array(e));ac.close&&ac.close();
  addOut(new Blob(parts,{type:'audio/mpeg'}),base(f.name)+'.mp3');
};

const xesc=s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g,'');
RUN.pdf2word=async function(){
  pdfjsLib.GlobalWorkerOptions.workerSrc=PDFWORKER;
  const f=files[0];let pdf;try{pdf=await pdfjsLib.getDocument({data:await f.arrayBuffer()}).promise}catch(e){throw new Error('This PDF is password-protected or damaged.')}
  let body='',chars=0;
  for(let p=1;p<=pdf.numPages;p++){status(`Reading page ${p} of ${pdf.numPages}…`);
    const tc=await (await pdf.getPage(p)).getTextContent();
    const lines=[];
    for(const it of tc.items){if(!it.str||!it.str.trim())continue;const y=it.transform[5],h=Math.hypot(it.transform[2],it.transform[3])||10;
      let ln=lines.find(l=>Math.abs(l.y-y)<h*0.5);if(!ln){ln={y,h,items:[]};lines.push(ln)}ln.items.push(it);ln.h=Math.max(ln.h,h)}
    lines.sort((a,b)=>b.y-a.y);
    const hs=lines.map(l=>l.h).sort((a,b)=>a-b),med=hs[Math.floor(hs.length/2)]||10;
    const paras=[];let prev=null;
    for(const l of lines){l.items.sort((a,b)=>a.transform[4]-b.transform[4]);
      let txt='',endX=null;for(const it of l.items){const x=it.transform[4];if(endX!==null&&x-endX>l.h*0.25&&!txt.endsWith(' '))txt+=' ';txt+=it.str;endX=x+(it.width||0)}
      txt=txt.replace(/\s+/g,' ').trim();const big=l.h>med*1.3;
      if(prev&&!big&&!prev.big&&prev.y-l.y<l.h*1.75&&!/^([•\-–•]|\d+[.)])\s/.test(txt))prev.text+=(prev.text.endsWith('-')?'':' ')+txt,prev.y=l.y;
      else{prev={text:txt,y:l.y,big,h:l.h};paras.push(prev)}}
    for(const pa of paras){chars+=pa.text.length;
      const rpr=pa.big?`<w:rPr><w:b/><w:sz w:val="${Math.min(48,Math.round(pa.h*2))}"/></w:rPr>`:'';
      body+=`<w:p>${pa.big?'<w:pPr><w:spacing w:before="200" w:after="120"/></w:pPr>':''}<w:r>${rpr}<w:t xml:space="preserve">${xesc(pa.text)}</w:t></w:r></w:p>`}
    if(p<pdf.numPages)body+='<w:p><w:r><w:br w:type="page"/></w:r></w:p>'}
  if(!chars)throw new Error('No text found. This looks like a scanned PDF: use Image to Text (OCR) instead.');
  const z=new JSZip();
  z.file('[Content_Types].xml','<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>');
  z.file('_rels/.rels','<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>');
  z.file('word/document.xml','<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'+body+'<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr></w:body></w:document>');
  addOut(await z.generateAsync({type:'blob',mimeType:'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}),base(f.name)+'.docx');
};

/* page init */
cur=document.body.dataset.tool;
(function(){const t=TOOLS[cur];const fin=$('#fin');fin.accept=t.accept;fin.multiple=t.multi;
 $('#d-main').textContent=t.multi?'Choose files':'Choose a file';$('#d-sub').textContent='or drag and drop '+(t.multi?'them':'it')+' here';const fm=$('#d-fmt');if(fm)fm.textContent='Supported: '+t.fmt+(t.multi?' · several files at once':'');
 $('#go').textContent=t.go;renderOpts();render();
 const P=window.PRESET||{};for(const [sel,v] of Object.entries(P)){const e=$(sel);if(!e)continue;if(e.type==='checkbox')e.checked=!!v;else e.value=v;e.dispatchEvent(new Event('input'));e.dispatchEvent(new Event('change'))}})();
