/* Tools for World: tool search, recently used tools. Small and dependency-free. */
(function () {
  var K = 'tfw_recent';
  function get() { try { return JSON.parse(localStorage.getItem(K) || '[]') || []; } catch (e) { return []; } }
  function set(v) { try { localStorage.setItem(K, JSON.stringify(v)); } catch (e) {} }
  window.TFW = { used: function () {} };
  var b = document.body, h1 = document.querySelector('h1');
  // remember tool pages the visitor opens (kept only in this browser)
  if ((b.dataset.tool || b.dataset.calc) && h1 && !document.getElementById('q')) {
    var slug = location.pathname.replace(/\/(index\.html)?$/, '').split('/').pop();
    if (slug) { var r = get().filter(function (x) { return x.s !== slug; }); r.unshift({ s: slug, n: h1.textContent.trim().slice(0, 60) }); set(r.slice(0, 6)); }
  }
  var q = document.getElementById('q');
  if (!q) return;                                   // the rest is for the home page
  var rec = get(), rc = document.getElementById('rchips');
  if (rec.length && rc) {
    rec.forEach(function (x) { if (!/^[a-z0-9-]+$/.test(x.s)) return; var a = document.createElement('a'); a.href = x.s + '/'; a.textContent = x.n; rc.appendChild(a); });
    if (rc.children.length) document.getElementById('recent').hidden = false;
  }
  // search index from the tool cards and preset chips already on the page
  var seen = {}, idx = [];
  document.querySelectorAll('#browse a.tile, #browse .xall a').forEach(function (a) {
    var href = a.getAttribute('href'); if (seen[href] || a.closest('#recent')) return; seen[href] = 1;
    var n = a.querySelector('.tn'), p = a.querySelector('.td'), row = a.closest('.xrow');
    var parent = row ? document.querySelector('#tgrid a.tile[href="' + row.querySelector('.xp').getAttribute('href') + '"]') : null;
    var name = n ? n.textContent.trim() : (a.getAttribute('title') || a.textContent).trim();
    idx.push({ href: href, name: name, desc: p ? p.textContent.trim() : '', k: (name + ' ' + (p ? p.textContent : '') + ' ' + (a.dataset.k || '') + ' ' + href.replace(/[-\/]/g, ' ')).toLowerCase(),
      main: !!n, tileEl: n ? a : null, parent: parent });
  });
  var res = document.getElementById('results'), grid = document.getElementById('rgrid'), none = document.getElementById('rnone'), browse = document.getElementById('browse');
  function norm(s) { return s.toLowerCase().replace(/[×x]/g, 'x').replace(/\s+/g, ' ').trim(); }
  function run() {
    var v = norm(q.value);
    if (!v) { res.hidden = true; browse.hidden = false; return; }
    var words = v.split(' ');
    var hits = idx.map(function (t) {
      var k = t.k.replace(/×/g, 'x'), sc = 0;
      for (var i = 0; i < words.length; i++) { if (k.indexOf(words[i]) < 0) return null; sc += t.name.toLowerCase().indexOf(words[i]) >= 0 ? 2 : 1; }
      return { t: t, sc: sc + (t.main ? 1 : 0) };
    }).filter(Boolean).sort(function (a, b) { return b.sc - a.sc; }).slice(0, 24);
    grid.innerHTML = '';
    hits.forEach(function (h) {
      var a;
      if (h.t.tileEl) { a = h.t.tileEl.cloneNode(true); a.hidden = false; }
      else {
        a = document.createElement('a'); a.className = 'tile'; a.href = h.t.href;
        var ic = h.t.parent ? h.t.parent.querySelector('.tic').cloneNode(true) : document.createElement('span');
        var n = document.createElement('span'), d = document.createElement('span');
        n.className = 'tn'; d.className = 'td'; n.textContent = h.t.name;
        d.textContent = h.t.parent ? h.t.parent.querySelector('.tn').textContent + ' preset' : 'Free, private, works in your browser.';
        a.appendChild(ic); a.appendChild(n); a.appendChild(d);
      }
      grid.appendChild(a);
    });
    none.hidden = hits.length > 0; res.hidden = false; browse.hidden = true;
  }
  q.addEventListener('input', run);
  q.addEventListener('keydown', function (e) { if (e.key === 'Enter') { var f = grid.querySelector('a'); if (f) location.href = f.href; } });
  document.addEventListener('keydown', function (e) { if (e.key === '/' && document.activeElement !== q && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { e.preventDefault(); q.focus(); } });
  // category filter: show one group of tools or all
  var fl = [].slice.call(document.querySelectorAll('.flt')), tiles = [].slice.call(document.querySelectorAll('#tgrid .tile'));
  function filt(f) {
    fl.forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.f === f); });
    tiles.forEach(function (t) { t.hidden = f !== 'all' && t.dataset.g !== f; });
  }
  fl.forEach(function (b) { b.addEventListener('click', function () { filt(b.dataset.f); }); });
  function fromHash() {
    var h = location.hash.replace('#', '');
    if (fl.some(function (b) { return b.dataset.f === h; })) { filt(h); document.getElementById('all').scrollIntoView(); }
  }
  fromHash(); window.addEventListener('hashchange', fromHash);
  var m = /[?&]q=([^&]*)/.exec(location.search);
  if (m) { try { q.value = decodeURIComponent(m[1].replace(/\+/g, ' ')); } catch (e) {} run(); }
})();
