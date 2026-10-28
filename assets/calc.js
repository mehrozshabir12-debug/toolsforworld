/* Tools for World utility tools. Each page sets <body data-calc="...">. Everything runs in the browser. */
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const num = id => { const v = parseFloat(($('#' + id) || {}).value); return isFinite(v) ? v : 0; };
const fx = (n, d = 2) => (+n).toLocaleString('en-US', { maximumFractionDigits: d });
function live(fn) { $$('.calc input, .calc select, .calc textarea').forEach(e => { e.addEventListener('input', fn); e.addEventListener('change', fn); }); fn(); }
function copyText(text, btn) {
  const done = () => { const t = btn.textContent; btn.textContent = 'Copied'; setTimeout(() => btn.textContent = t, 1200); };
  if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, () => { prompt('Copy:', text); });
}
const CALC = {};

/* ---------------- Word counter ---------------- */
CALC.words = () => {
  const run = () => {
    const t = $('#wt').value;
    const words = (t.match(/[\p{L}\p{N}][\p{L}\p{N}'’\-]*/gu) || []).length;
    const chars = [...t].length, noSpace = [...t.replace(/\s/g, '')].length;
    const sentences = (t.match(/[^.!?؟।]+[.!?؟।]+/g) || []).length || (t.trim() ? 1 : 0);
    const paras = t.split(/\n\s*\n/).filter(p => p.trim()).length;
    const mins = w => w <= 0 ? '0 min' : w < 1 ? '< 1 min' : (w < 60 ? Math.max(1, Math.round(w)) + ' min' : Math.floor(w / 60) + ' h ' + Math.round(w % 60) + ' min');
    $('#out-kv').innerHTML = [['Words', fx(words, 0)], ['Characters', fx(chars, 0)], ['Characters (no spaces)', fx(noSpace, 0)],
      ['Sentences', fx(sentences, 0)], ['Paragraphs', fx(paras, 0)], ['Reading time', mins(words / 238)], ['Speaking time', mins(words / 140)]]
      .map(([k, v]) => `<div><b>${v}</b><span>${k}</span></div>`).join('');
    const freq = {};
    (t.toLowerCase().match(/[\p{L}][\p{L}'’]{3,}/gu) || []).forEach(w => freq[w] = (freq[w] || 0) + 1);
    const top = Object.entries(freq).sort((a, b) => b[1] - a[1]).slice(0, 8);
    $('#out-top').innerHTML = top.length ? top.map(([w, n]) => `<tr><td>${w.replace(/[<>&]/g, '')}</td><td class="n">${n}</td><td class="n">${fx(n / Math.max(1, words) * 100, 1)}%</td></tr>`).join('') : '<tr><td colspan="3" class="note">Start typing to see your most used words.</td></tr>';
  };
  $('#wclear').onclick = () => { $('#wt').value = ''; run(); $('#wt').focus(); };
  live(run);
};

/* ---------------- Age calculator ---------------- */
CALC.age = () => {
  const today = new Date(); const iso = d => d.toISOString().slice(0, 10);
  if (!$('#ato').value) $('#ato').value = iso(today);
  const run = () => {
    const a = new Date($('#adob').value + 'T00:00:00'), b = new Date($('#ato').value + 'T00:00:00');
    if (isNaN(a) || isNaN(b)) { $('#out-total').innerHTML = '—<small>Enter a date of birth</small>'; $('#out-kv').innerHTML = ''; return; }
    if (b < a) { $('#out-total').innerHTML = '—<small>The second date is before the date of birth</small>'; $('#out-kv').innerHTML = ''; return; }
    let y = b.getFullYear() - a.getFullYear(), m = b.getMonth() - a.getMonth(), d = b.getDate() - a.getDate();
    if (d < 0) { m--; d += new Date(b.getFullYear(), b.getMonth(), 0).getDate(); }
    if (m < 0) { y--; m += 12; }
    const days = Math.round((b - a) / 864e5);
    let next = new Date(b.getFullYear(), a.getMonth(), a.getDate());
    if (next < b) next = new Date(b.getFullYear() + 1, a.getMonth(), a.getDate());
    const toNext = Math.round((next - b) / 864e5);
    const wd = a.toLocaleDateString('en-US', { weekday: 'long' });
    $('#out-total').innerHTML = `${y} years, ${m} months, ${d} days<small>Born on a ${wd}</small>`;
    $('#out-kv').innerHTML = [['Total months', fx(y * 12 + m, 0)], ['Total weeks', fx(Math.floor(days / 7), 0)], ['Total days', fx(days, 0)],
      ['Total hours', fx(days * 24, 0)], ['Next birthday', toNext === 0 ? 'Today! 🎂' : 'in ' + toNext + ' days'], ['Turning', y + (toNext === 0 ? 0 : 1)]]
      .map(([k, v]) => `<div><b>${v}</b><span>${k}</span></div>`).join('');
  };
  live(run);
};

/* ---------------- Percentage calculator ---------------- */
CALC.pct = () => {
  const run = () => {
    const show = (id, v, suf = '') => $('#' + id).textContent = isFinite(v) ? fx(v, 4) + suf : '—';
    show('r1', num('p1a') / 100 * num('p1b'));
    show('r2', num('p2a') / num('p2b') * 100, '%');
    const from = num('p3a'), to = num('p3b'), ch = (to - from) / Math.abs(from) * 100;
    $('#r3').textContent = isFinite(ch) ? (ch > 0 ? '+' : '') + fx(ch, 4) + '% ' + (ch > 0 ? 'increase' : ch < 0 ? 'decrease' : '') : '—';
    show('r4', num('p4b') * (1 + num('p4a') / 100));
    show('r5', num('p5b') * (1 - num('p5a') / 100));
  };
  live(run);
};

/* ---------------- Password generator ---------------- */
const SETS = { upper: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', lower: 'abcdefghijklmnopqrstuvwxyz', digits: '0123456789', symbols: '!@#$%^&*()-_=+[]{};:,.?/~' };
function rnd(n) { const a = new Uint32Array(1), lim = Math.floor(2 ** 32 / n) * n; do crypto.getRandomValues(a); while (a[0] >= lim); return a[0] % n; }
CALC.pass = () => {
  const run = () => {
    $('#plv').textContent = $('#pl').value;
    let pools = Object.keys(SETS).filter(k => $('#p_' + k).checked).map(k => SETS[k]);
    if ($('#p_sim').checked) pools = pools.map(p => p.replace(/[O0Il1|]/g, ''));
    if (!pools.length) { $('#out-list').innerHTML = '<p class="note err">Choose at least one character type.</p>'; return; }
    const all = pools.join(''), len = +$('#pl').value;
    const make = () => {
      const c = pools.map(p => p[rnd(p.length)]);                 // at least one from each chosen type
      while (c.length < len) c.push(all[rnd(all.length)]);
      for (let i = c.length - 1; i > 0; i--) { const j = rnd(i + 1); [c[i], c[j]] = [c[j], c[i]]; }
      return c.slice(0, len).join('');
    };
    const bits = Math.round(len * Math.log2(all.length));
    const lvl = bits < 40 ? ['Weak', 'var(--warn)'] : bits < 60 ? ['Fair', 'var(--warn)'] : bits < 80 ? ['Strong', 'var(--accent)'] : ['Very strong', 'var(--accent)'];
    $('#out-strength').innerHTML = `<b style="color:${lvl[1]}">${lvl[0]}</b> · about ${bits} bits of entropy`;
    $('#out-list').innerHTML = Array.from({ length: 5 }, make).map((p, i) =>
      `<div class="file"><code class="nm" style="font:500 1rem var(--mono)">${p.replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]))}</code><button class="btn ghost" data-i="${i}" type="button">Copy</button></div>`).join('');
    $$('#out-list button').forEach(b => b.onclick = () => copyText(b.previousElementSibling.textContent, b));
  };
  $('#pgen').onclick = () => run();
  live(run);
};

/* ---------------- QR code generator ---------------- */
CALC.qr = () => {
  const cv = $('#qrc');
  const run = () => {
    const text = $('#qt').value;
    if (typeof qrcode !== 'function') { $('#qerr').textContent = 'The QR library could not load. Check your internet connection.'; $('#qerr').hidden = false; return; }
    $('#qerr').hidden = true;
    if (!text) { cv.getContext('2d').clearRect(0, 0, cv.width, cv.height); return; }
    if (qrcode.stringToBytesFuncs && qrcode.stringToBytesFuncs['UTF-8']) qrcode.stringToBytes = qrcode.stringToBytesFuncs['UTF-8'];
    let q;
    try { q = qrcode(0, $('#qe').value); q.addData(text, 'Byte'); q.make(); }
    catch (e) { $('#qerr').textContent = 'This text is too long for one QR code. Shorten it or use a link.'; $('#qerr').hidden = false; return; }
    const n = q.getModuleCount(), size = +$('#qs').value, quiet = 4, cell = Math.floor(size / (n + quiet * 2)), dim = cell * (n + quiet * 2);
    cv.width = cv.height = dim;
    const x = cv.getContext('2d'); x.fillStyle = $('#qbg').value; x.fillRect(0, 0, dim, dim); x.fillStyle = $('#qfg').value;
    for (let r = 0; r < n; r++) for (let c = 0; c < n; c++) if (q.isDark(r, c)) x.fillRect((c + quiet) * cell, (r + quiet) * cell, cell, cell);
    $('#qinfo').textContent = `${dim} × ${dim} px`;
  };
  $('#qdl').onclick = () => cv.toBlob(b => { const a = document.createElement('a'); a.href = URL.createObjectURL(b); a.download = 'qr-code.png'; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 4000); }, 'image/png');
  $$('[data-qt]').forEach(b => b.onclick = () => { $('#qt').value = b.dataset.qt; run(); });
  live(run);
};

/* ---------------- Date calculator ---------------- */
CALC.date = () => {
  const D = v => { const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v || ''); return m ? Date.UTC(+m[1], +m[2] - 1, +m[3]) : NaN; };
  const iso = t => new Date(t).toISOString().slice(0, 10);
  const long = t => new Date(t).toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });
  const DAY = 864e5, wd = t => new Date(t).getUTCDay();
  const now = new Date(), today = Date.UTC(now.getFullYear(), now.getMonth(), now.getDate());
  if (!$('#ds').value) $('#ds').value = iso(today);
  if (!$('#de').value) $('#de').value = iso(Date.UTC(now.getFullYear(), 11, 31));
  if (!$('#da').value) $('#da').value = iso(today);
  const ymd = (a, b) => {   // full years, then months, then days (a <= b)
    const A = new Date(a), B = new Date(b);
    let y = B.getUTCFullYear() - A.getUTCFullYear(), m = B.getUTCMonth() - A.getUTCMonth(), d = B.getUTCDate() - A.getUTCDate();
    if (d < 0) { m--; d += new Date(Date.UTC(B.getUTCFullYear(), B.getUTCMonth(), 0)).getUTCDate(); }
    if (m < 0) { y--; m += 12; }
    return [y, m, d];
  };
  const workdays = (a, b) => { let n = 0; for (let t = a; t < b; t += DAY) { const w = wd(t); if (w && w < 6) n++; } return n; };
  const addMonths = (t, k) => { const x = new Date(t), y = x.getUTCFullYear(), m = x.getUTCMonth() + k, d = x.getUTCDate();
    const last = new Date(Date.UTC(y, m + 1, 0)).getUTCDate(); return Date.UTC(y, m, Math.min(d, last)); };
  const run = () => {
    let a = D($('#ds').value), b = D($('#de').value);
    if (isNaN(a) || isNaN(b)) { $('#out-total').innerHTML = '—<small>Pick both dates</small>'; $('#out-kv').innerHTML = ''; }
    else {
      const back = b < a; if (back) [a, b] = [b, a];
      const inc = $('#dinc').checked, end = inc ? b + DAY : b, days = Math.round((end - a) / DAY);
      const [y, m, d] = ymd(a, end), wk = Math.floor(days / 7), rest = days % 7;
      const parts = [y && `${y} year${y > 1 ? 's' : ''}`, m && `${m} month${m > 1 ? 's' : ''}`, (d || (!y && !m)) && `${d} day${d === 1 ? '' : 's'}`].filter(Boolean).join(', ');
      $('#out-total').innerHTML = `${fx(days, 0)} day${days === 1 ? '' : 's'}<small>${back ? 'The end date is before the start date, so the dates were swapped. ' : ''}${parts}${inc ? ' (end date included)' : ''}</small>`;
      $('#out-kv').innerHTML = [['Weeks and days', `${fx(wk, 0)} wk ${rest} d`], ['Weekdays (Mon–Fri)', fx(workdays(a, end), 0)], ['Weekend days', fx(days - workdays(a, end), 0)],
        ['Months (approx.)', fx(days / 30.4369, 1)], ['Hours', fx(days * 24, 0)], ['Minutes', fx(days * 1440, 0)]]
        .map(([k, v]) => `<div><b>${v}</b><span>${k}</span></div>`).join('');
    }
    const s = D($('#da').value), n = Math.trunc(num('dn')) * ($('#dop').value === '-' ? -1 : 1), u = $('#du').value;
    if (isNaN(s)) { $('#r-add').innerHTML = '—'; return; }
    let r;
    if (u === 'd') r = s + n * DAY; else if (u === 'w') r = s + n * 7 * DAY;
    else if (u === 'm') r = addMonths(s, n); else if (u === 'y') r = addMonths(s, n * 12);
    else { r = s; let left = Math.abs(n); const step = n < 0 ? -DAY : DAY; while (left > 0) { r += step; const w = wd(r); if (w && w < 6) left--; } }
    $('#r-add').innerHTML = isFinite(r) && Math.abs(r) < 8.64e15 ? `${long(r)}<small>${iso(r)}</small>` : '—';
  };
  $$('[data-dq]').forEach(b => b.onclick = () => { const [op, k, u] = b.dataset.dq.split(' '); $('#dop').value = op; $('#dn').value = k; $('#du').value = u; run(); });
  live(run);
};

const which = document.body.dataset.calc;
for (const [sel, v] of Object.entries(window.PRESET || {})) { const e = $(sel); if (e) e.value = v; }
if (CALC[which]) CALC[which]();
