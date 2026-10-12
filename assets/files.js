/* Tools for World file tools: everything runs in the browser, files never leave the device. */
const $=s=>document.querySelector(s);
const I={pdf:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6"/></svg>'};
const TOOLS={
 compress:{accept:'image/*',multi:true,go:'Compress'},
 resize:{accept:'image/*',multi:true,go:'Resize'},
 convert:{accept:'image/*',multi:true,go:'Convert'},
 passport:{accept:'image/*',multi:false,go:'Make sheet'},
 img2pdf:{accept:'image/jpeg,image/png,image/webp',multi:true,go:'Create PDF'},
 merge:{accept:'application/pdf',multi:true,go:'Merge PDFs'},
 split:{accept:'application/pdf',multi:false,go:'Split PDF'},
 pdf2jpg:{accept:'application/pdf',multi:false,go:'Convert to JPG'},
 word2pdf:{accept:'application/vnd.openxmlformats-officedocument.wordprocessingml.document,.docx',multi:false,go:'Convert to PDF'},
 png2jpg:{accept:'image/png',multi:true,go:'Convert to JPG',fmt:'image/jpeg'},
 jpg2png:{accept:'image/jpeg',multi:true,go:'Convert to PNG',fmt:'image/png'},
 webp2jpg:{accept:'image/webp',multi:true,go:'Convert to JPG',fmt:'image/jpeg'},
 heic2jpg:{accept:'image/heic,image/heif,.heic,.heif',multi:true,go:'Convert to JPG'},
 pdfcompress:{accept:'application/pdf',multi:false,go:'Compress PDF'},
 ocr:{accept:'image/*',multi:false,go:'Extract text'},
 bgremove:{accept:'image/*',multi:false,go:'Remove background'},
 mp4mp3:{accept:'video/*,audio/*,.mp4,.m4a,.mov,.webm,.mkv',multi:false,go:'Convert to MP3'},
 pdf2word:{accept:'application/pdf',multi:false,go:'Convert to Word'}
};
let cur=null, files=[], outs=[];
const kb=n=>n<1048576?(n/1024).toFixed(0)+' KB':(n/1048576).toFixed(2)+' MB';
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const base=n=>n.replace(/\.[^.]+$/,'');
function status(t,err){const s=$('#status');s.textContent=t||'';s.className='note'+(err?' err':'')}



function addFiles(list){
  const t=TOOLS[cur];let added=[...list].filter(f=>t.accept.split(',').some(a=>a.startsWith('.')?f.name.toLowerCase().endsWith(a):a.endsWith('/*')?f.type.startsWith(a.slice(0,-1)):f.type===a));
  if(!added.length){status('That file type is not supported here.',true);return}
  files=t.multi?files.concat(added):[added[0]];
  status('');render();if(cur==='passport')ppLoad();
}
$('#fin').addEventListener('change',e=>{addFiles(e.target.files);e.target.value=''});
const drop=$('#drop');
['dragenter','dragover'].forEach(ev=>drop.addEventListener(ev,e=>{e.preventDefault();drop.classList.add('over')}));
['dragleave','drop'].forEach(ev=>drop.addEventListener(ev,e=>{e.preventDefault();drop.classList.remove('over')}));
drop.addEventListener('drop',e=>addFiles(e.dataTransfer.files));
drop.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();$('#fin').click()}});
$('#clear').onclick=()=>{files=[];$('#out').innerHTML='';status('');render()};

function render(){
  $('#panel').hidden=!files.length;
  const L=$('#list');L.innerHTML='';
  const reorder=['img2pdf','merge'].includes(cur);
  files.forEach((f,i)=>{
    const d=document.createElement('div');d.className='file';
    const th=f.type.startsWith('image/')?`<img alt="" src="${URL.createObjectURL(f)}">`:`<span class="ic" style="color:var(--accent)">${I.pdf}</span>`;
    d.innerHTML=`${th}<span class="nm">${esc(f.name)}</span><span class="sz">${kb(f.size)}</span>`+
      (reorder?`<button class="mv" aria-label="Move up" data-u="${i}">▲</button><button class="mv" aria-label="Move down" data-d="${i}">▼</button>`:'')+
      `<button class="x" aria-label="Remove" data-x="${i}">×</button>`;
    L.appendChild(d);
  });
  L.querySelectorAll('[data-x]').forEach(b=>b.onclick=()=>{files.splice(+b.dataset.x,1);render()});
  L.querySelectorAll('[data-u]').forEach(b=>b.onclick=()=>{const i=+b.dataset.u;if(i>0){[files[i-1],files[i]]=[files[i],files[i-1]];render()}});
  L.querySelectorAll('[data-d]').forEach(b=>b.onclick=()=>{const i=+b.dataset.d;if(i<files.length-1){[files[i+1],files[i]]=[files[i],files[i+1]];render()}});
  $('#go').disabled=!files.length||(cur==='merge'&&files.length<2);
  if(cur==='merge'&&files.length===1)status('Add at least one more PDF to merge.');
}

function renderOpts(){
  const o=$('#opts');
  const fmt=(id,def)=>`<label>Format <select id="${id}"><option value="image/jpeg"${def==='jpg'?' selected':''}>JPG</option><option value="image/png"${def==='png'?' selected':''}>PNG</option><option value="image/webp"${def==='webp'?' selected':''}>WebP</option></select></label>`;
  o.innerHTML={
   compress:`<div class="row"><label>Quality <input type="range" id="q" min="10" max="95" value="70"> <span id="qv" class="sz">70%</span></label><label>Max width <input type="number" id="mw" placeholder="Original" min="50"> px</label><label>Output <select id="cf"><option value="image/jpeg">JPG</option><option value="image/webp">WebP</option></select></label></div>`,
   resize:`<div class="row"><label><select id="rm"><option value="px">Pixels</option><option value="pc">Percent</option></select></label><label>Width <input type="number" id="rw" min="1"></label><label>Height <input type="number" id="rh" min="1"></label><label><input type="checkbox" id="rk" checked> Keep ratio</label><label>Percent <input type="number" id="rp" value="50" min="1" max="500"> %</label></div><p class="note">With "Keep ratio", fill only width or height and the other is calculated for each image.</p>`,
   convert:`<div class="row">${fmt('tf','png')}<label>Quality <input type="range" id="tq" min="10" max="100" value="92"></label></div>`,
   passport:`<div class="pp"><canvas id="ppc" width="350" height="450" aria-label="Passport photo preview"></canvas><div class="panel" style="margin:0">
     <label>Size <select id="ps"><option value="35x45">35 × 45 mm – Pakistan, Australia, UK, EU, India</option><option value="51x51">2 × 2 in – USA</option><option value="40x50">40 × 50 mm</option><option value="30x40">30 × 40 mm</option></select></label>
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
  const u=URL.createObjectURL(blob);outs.push(u);
  const d=document.createElement('div');d.className='file';
  const th=blob.type.startsWith('image/')?`<img alt="" src="${u}">`:`<span class="ic" style="color:var(--accent)">${I.pdf}</span>`;
  d.innerHTML=`${th}<span class="nm">${esc(name)}</span><span class="sz">${kb(blob.size)}</span><a class="save" href="${u}" download="${esc(name)}">Download</a>`;
  $('#out').appendChild(d);
}
const loadImg=f=>new Promise((res,rej)=>{const i=new Image();i.onload=()=>res(i);i.onerror=()=>rej(new Error('Could not read '+f.name));i.src=URL.createObjectURL(f)});
const toBlob=(c,type,q)=>new Promise(r=>c.toBlob(r,type,q));
function draw(img,w,h,type){const c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');if(type==='image/jpeg'){x.fillStyle='#fff';x.fillRect(0,0,w,h)}x.drawImage(img,0,0,w,h);return c}
const ext={'image/jpeg':'jpg','image/png':'png','image/webp':'webp'};

$('#go').onclick=async()=>{
  $('#go').disabled=true;$('#out').innerHTML='';status('Working…');
  try{await RUN[cur]();status('Done. Your files are ready below.')}
  catch(e){console.error(e);status(e.message||'Something went wrong. Try another file.',true)}
  $('#go').disabled=false;
};
const RUN={
 async compress(){
  const q=$('#q').value/100,mw=+$('#mw').value||0,type=$('#cf').value;
  for(const f of files){const i=await loadImg(f);let w=i.naturalWidth,h=i.naturalHeight;if(mw&&w>mw){h=Math.round(h*mw/w);w=mw}
   const b=await toBlob(draw(i,w,h,type),type,q);addOut(b,base(f.name)+'-compressed.'+ext[type]);
   status(`${f.name}: ${kb(f.size)} → ${kb(b.size)}`)}
 },
 async resize(){
  const m=$('#rm').value,W=+$('#rw').value,H=+$('#rh').value,k=$('#rk').checked,p=+$('#rp').value/100;
  if(m==='px'&&!W&&!H)throw new Error('Enter a width or a height.');
  for(const f of files){const i=await loadImg(f),r=i.naturalWidth/i.naturalHeight;let w,h;
   if(m==='pc'){w=i.naturalWidth*p;h=i.naturalHeight*p}
   else if(k){w=W||H*r;h=W?W/r:H}else{w=W||i.naturalWidth;h=H||i.naturalHeight}
   w=Math.max(1,Math.round(w));h=Math.max(1,Math.round(h));
   const type=f.type==='image/png'?'image/png':f.type==='image/webp'?'image/webp':'image/jpeg';
   addOut(await toBlob(draw(i,w,h,type),type,.92),`${base(f.name)}-${w}x${h}.${ext[type]}`)}
 },
 async convert(){
  const type=$('#tf').value,q=$('#tq').value/100;
  for(const f of files){const i=await loadImg(f);addOut(await toBlob(draw(i,i.naturalWidth,i.naturalHeight,type),type,q),base(f.name)+'.'+ext[type])}
 },
 async passport(){
  const one=ppCanvas(600);const n=+$('#pn').value;
  const S=document.createElement('canvas');S.width=1800;S.height=1200;const x=S.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,1800,1200);
  const [mw,mh]=ppSize(),dpi=300,pw=Math.round(mw/25.4*dpi),ph=Math.round(mh/25.4*dpi);
  const cols=n===4?2:n===6?3:4,rows=2,gx=(1800-cols*pw)/(cols+1),gy=(1200-rows*ph)/(rows+1);
  for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){const X=gx+c*(gx+pw),Y=gy+r*(gy+ph);x.drawImage(one,X,Y,pw,ph);x.strokeStyle='#bbb';x.lineWidth=1;x.strokeRect(X,Y,pw,ph)}
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
  pdfjsLib.GlobalWorkerOptions.workerSrc='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
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
async function ppLoad(){ppImg=await loadImg(files[0]);ppDraw()}
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


/* Word (.docx) to PDF: mammoth turns the document into HTML, html2pdf draws it on A4 pages. */
RUN.word2pdf=async function(){
  const f=files[0];
  if(!/\.docx$/i.test(f.name))throw new Error('Please choose a .docx file (older .doc files: open in Word and "Save as" .docx first).');
  let res;
  try{res=await mammoth.convertToHtml({arrayBuffer:await f.arrayBuffer()})}catch(e){throw new Error('Could not read this Word file. It may be damaged or password-protected.')}
  const pv=$('#doc-preview');pv.hidden=false;pv.innerHTML=res.value||'<p>(empty document)</p>';
  status('Making PDF…');
  const blob=await html2pdf().set({margin:[12,12,14,12],image:{type:'jpeg',quality:.95},html2canvas:{scale:2,useCORS:true,backgroundColor:'#ffffff'},
    jsPDF:{unit:'mm',format:$('#wp').value,orientation:$('#wo').value},pagebreak:{mode:['css','legacy']}}).from(pv).outputPdf('blob');
  addOut(blob,base(f.name)+'.pdf');
  $('#printbtn').hidden=false;
};

/* ------------------------------------------------------------------ more tools */
const OPTX={
 png2jpg:`<div class="row"><label>Quality <input type="range" id="tq" min="10" max="100" value="92"></label><span class="note">Transparent areas become white.</span></div>`,
 jpg2png:'',
 webp2jpg:`<div class="row"><label>Quality <input type="range" id="tq" min="10" max="100" value="92"></label></div>`,
 heic2jpg:`<div class="row"><label>Quality <input type="range" id="tq" min="10" max="100" value="92"></label><span class="note">iPhone photos (.heic). Conversion can take a few seconds per photo.</span></div>`,
 pdfcompress:`<div class="row"><label>Level <select id="pc"><option value="150|0.75">Recommended (150 dpi)</option><option value="110|0.6" selected>Strong (110 dpi)</option><option value="200|0.85">Light (200 dpi)</option><option value="80|0.5">Extreme (80 dpi)</option></select></label></div><p class="note">Best for scanned PDFs and PDFs full of photos. Pages are re-saved as images, so text can no longer be selected or searched.</p>`,
 ocr:`<div class="row"><label>Language <select id="ol"><option value="eng">English</option><option value="urd">Urdu</option><option value="eng+urd">English + Urdu</option><option value="ara">Arabic</option><option value="hin">Hindi</option></select></label></div><p class="note">The first run downloads the language data (about 10–20 MB). Clear, straight photos give the best results.</p><textarea id="ocrout" rows="10" style="width:100%;font:inherit;padding:10px;border-radius:10px;border:1px solid var(--line);background:var(--sunk);color:var(--fg)" placeholder="Text will appear here" hidden></textarea><p><button class="btn ghost" id="ocrcopy" type="button" hidden>Copy text</button></p>`,
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
  if(typeof heic2any!=='function')throw new Error('The HEIC converter could not load. Check your internet connection and try again.');
  const q=$('#tq').value/100;
  for(const f of files){status('Converting '+f.name+'…');
    let out;try{out=await heic2any({blob:f,toType:'image/jpeg',quality:q})}catch(e){throw new Error(f.name+' could not be read as a HEIC photo.')}
    (Array.isArray(out)?out:[out]).forEach((b,i,a)=>addOut(b,base(f.name)+(a.length>1?'-'+(i+1):'')+'.jpg'))}
};

RUN.pdfcompress=async function(){
  pdfjsLib.GlobalWorkerOptions.workerSrc='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
  const f=files[0],[dpi,q]=$('#pc').value.split('|').map(Number);
  let pdf;try{pdf=await pdfjsLib.getDocument({data:await f.arrayBuffer()}).promise}catch(e){throw new Error('This PDF is password-protected or damaged.')}
  const {PDFDocument}=PDFLib,doc=await PDFDocument.create();
  for(let p=1;p<=pdf.numPages;p++){status(`Page ${p} of ${pdf.numPages}…`);
    const pg=await pdf.getPage(p),v1=pg.getViewport({scale:1}),vp=pg.getViewport({scale:dpi/72});
    const c=document.createElement('canvas');c.width=Math.ceil(vp.width);c.height=Math.ceil(vp.height);const x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,c.width,c.height);
    await pg.render({canvasContext:x,viewport:vp}).promise;
    const jpg=await doc.embedJpg(await (await toBlob(c,'image/jpeg',q)).arrayBuffer());
    doc.addPage([v1.width,v1.height]).drawImage(jpg,{x:0,y:0,width:v1.width,height:v1.height});c.width=c.height=0}
  const out=new Blob([await doc.save()],{type:'application/pdf'});
  if(out.size>=f.size){addOut(f,f.name);throw new Error(`This PDF is already well compressed (new size ${kb(out.size)} would not be smaller). Try a stronger level.`)}
  addOut(out,base(f.name)+'-compressed.pdf');
  setTimeout(()=>status(`${kb(f.size)} → ${kb(out.size)} (${Math.round((1-out.size/f.size)*100)}% smaller)`),0);
};

RUN.ocr=async function(){
  if(typeof Tesseract==='undefined')throw new Error('The text reader could not load. Check your internet connection and try again.');
  const lang=$('#ol').value,box=$('#ocrout');
  const r=await Tesseract.recognize(files[0],lang,{logger:m=>{if(m.status)status(m.status.replace(/^./,c=>c.toUpperCase())+(m.progress?' '+Math.round(m.progress*100)+'%':''))}});
  const t=(r.data.text||'').trim();
  box.hidden=false;box.value=t||'(No text found. Try a clearer photo.)';box.dir=/urd|ara/.test(lang)?'rtl':'ltr';
  $('#ocrcopy').hidden=false;$('#ocrcopy').onclick=()=>{navigator.clipboard.writeText(box.value).then(()=>status('Copied.'),()=>{box.select();status('Press Ctrl+C to copy.')})};
  addOut(new Blob([t],{type:'text/plain'}),base(files[0].name)+'.txt');
};

RUN.bgremove=async function(){
  status('Loading the AI model (first time only)…');
  let mod;try{mod=await import('https://cdn.jsdelivr.net/npm/@imgly/background-removal@1.4.5/+esm')}catch(e){throw new Error('The background remover could not load. Check your internet connection and try again.')}
  const blob=await mod.removeBackground(files[0],{progress:(k,c,t)=>status((k.includes('fetch')?'Downloading model ':'Working ')+(t?Math.round(c/t*100)+'%':''))});
  addOut(blob,base(files[0].name)+'-no-background.png');
};

function floatTo16(f){const o=new Int16Array(f.length);for(let i=0;i<f.length;i++){const s=Math.max(-1,Math.min(1,f[i]));o[i]=s<0?s*0x8000:s*0x7FFF}return o}
RUN.mp4mp3=async function(){
  if(typeof lamejs==='undefined')throw new Error('The MP3 encoder could not load. Check your internet connection and try again.');
  const f=files[0];status('Reading audio…');
  const AC=window.AudioContext||window.webkitAudioContext,ac=new AC();
  let buf;try{buf=await ac.decodeAudioData(await f.arrayBuffer())}catch(e){throw new Error('This file has no audio track your browser can read. Try another video.')}
  const ch=Math.min(2,buf.numberOfChannels),sr=buf.sampleRate,enc=new lamejs.Mp3Encoder(ch,sr,+$('#mb').value),parts=[],L=floatTo16(buf.getChannelData(0)),R=ch>1?floatTo16(buf.getChannelData(1)):null,step=1152;
  for(let i=0;i<L.length;i+=step){const d=ch>1?enc.encodeBuffer(L.subarray(i,i+step),R.subarray(i,i+step)):enc.encodeBuffer(L.subarray(i,i+step));if(d.length)parts.push(new Uint8Array(d));
    if(i%(step*400)===0){status('Encoding '+Math.round(i/L.length*100)+'%');await new Promise(r=>setTimeout(r))}}
  const e=enc.flush();if(e.length)parts.push(new Uint8Array(e));ac.close&&ac.close();
  addOut(new Blob(parts,{type:'audio/mpeg'}),base(f.name)+'.mp3');
};

const xesc=s=>s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g,'');
RUN.pdf2word=async function(){
  if(typeof JSZip==='undefined')throw new Error('The Word writer could not load. Check your internet connection and try again.');
  pdfjsLib.GlobalWorkerOptions.workerSrc='https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
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
 $('#d-main').textContent=t.multi?'Choose files':'Choose a file';$('#d-sub').textContent='or drag and drop '+(t.multi?'them':'it')+' here';
 $('#go').textContent=t.go;renderOpts();render();})();
