/* Bar Finch staff wine app. Plain JavaScript, no build step, works offline.
   Two halves: INFO (the wine bible: look things up) and TRAINING (courses, quizzes, flashcards).
   All wine data comes from js/data.js, generated from the Cellar Book. */
(function () {
  'use strict';
  var D = window.FINCH;
  var main = document.getElementById('main');
  var byId = {};
  D.wines.forEach(function (w, i) { w.idx = i; w.style = w.style || {}; w.food = w.food || []; byId[w.id] = w; });
  var SEC = {}; D.sections.forEach(function (s) { SEC[s.key] = s.label; });
  var BTG = D.wines.filter(function (w) { return w.glass; });
  var PROF = {}; D.profiles.forEach(function (p) { PROF[p.key] = p; });

  /* ---------- helpers ---------- */
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function gbp(n) { return n == null ? '' : '£' + n; }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
  function pick(a) { return a[Math.floor(Math.random() * a.length)]; }
  function uniq(a) { var s = {}, o = []; a.forEach(function (x) { if (!s[x]) { s[x] = 1; o.push(x); } }); return o; }
  function norm(s) { return String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[’']/g, "'"); }
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem('finch.' + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem('finch.' + k, JSON.stringify(v)); } catch (e) { /* private mode: progress is just not kept */ } }
  };
  function badge(w) {
    if (w.pour === 'COR') return '<span class="badge cor">◆ Coravin</span>';
    if (w.pour === 'Y') return '<span class="badge btg">By the glass</span>';
    return '';
  }
  function rowClass(w) { return w.pour === 'COR' ? ' is-cor' : (w.pour === 'Y' ? ' is-btg' : ''); }
  function howServed(w) { return w.pour === 'COR' ? 'By the glass, on the Coravin' : (w.pour === 'Y' ? 'By the glass' : 'Bottle only'); }
  function bottleLabel(w) { return w.size ? w.size.replace(/ \(.*\)/, '') : 'Bottle'; }
  function wineHref(id) { return '#/info/wine/' + id; }
  function toast(msg, action, fn) {
    var t = document.getElementById('toast');
    t.innerHTML = '<span>' + esc(msg) + '</span>' + (action ? '<button type="button">' + esc(action) + '</button>' : '');
    t.hidden = false;
    if (action) t.querySelector('button').onclick = fn;
    clearTimeout(toast.tm); if (!action) toast.tm = setTimeout(function () { t.hidden = true; }, 2600);
  }
  var ICON_SEARCH = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>';
  var ICONS = {
    wines: '<path d="M8 2h8M9 2v5c0 1-3 3-3 7v7a1 1 0 0 0 1 1h10a1 1 0 0 0 1-1v-7c0-4-3-6-3-7V2"/><path d="M6 14h12"/>',
    glass: '<path d="M7 2h10l-1 7a4 4 0 0 1-8 0L7 2z"/><path d="M12 13v8M8 21h8"/>',
    guests: '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
    ref: '<path d="M4 4h6a2 2 0 0 1 2 2v14a2 2 0 0 0-2-2H4zM20 4h-6a2 2 0 0 0-2 2v14a2 2 0 0 1 2-2h6z"/>',
    courses: '<path d="M3 7l9-4 9 4-9 4-9-4z"/><path d="M7 9v5c0 1.5 2.2 3 5 3s5-1.5 5-3V9"/>',
    quiz: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17.5v.01"/>',
    cards: '<rect x="3" y="5" width="13" height="16" rx="2"/><path d="M8 3h11a2 2 0 0 1 2 2v14"/>'
  };
  var TABS = {
    info: [['#/info', 'wines', 'Wines'], ['#/info/glass', 'glass', 'By the glass'], ['#/info/guests', 'guests', 'Guests'], ['#/info/ref', 'ref', 'Reference']],
    train: [['#/train', 'courses', 'Courses'], ['#/train/quiz', 'quiz', 'Quizzes'], ['#/train/cards', 'cards', 'Flashcards']]
  };
  function drawChrome(mode, tab) {
    document.querySelectorAll('.modes a').forEach(function (a) {
      if (a.getAttribute('data-mode') === mode) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    var nav = document.getElementById('tabbar');
    nav.className = 'tabbar n' + TABS[mode].length;
    nav.innerHTML = TABS[mode].map(function (t) {
      return '<a href="' + t[0] + '"' + (t[1] === tab ? ' aria-current="page"' : '') + '><svg viewBox="0 0 24 24" aria-hidden="true">' + ICONS[t[1]] + '</svg><span>' + esc(t[2]) + '</span></a>';
    }).join('');
  }

  /* ---------- router ---------- */
  var LEGACY = { wines: '#/info', glass: '#/info/glass', guests: '#/info/guests', guide: '#/info/ref' };
  var after = null, keepScroll = false;
  function route() {
    var h = (location.hash || '#/info').replace(/^#\/?/, '');
    var p = h.split('/');
    if (LEGACY[p[0]]) { location.replace(p[0] === 'guide' && p[1] ? '#/info/ref/' + p[1] : LEGACY[p[0]]); return; }
    if (p[0] === 'wine') { location.replace(wineHref(p[1])); return; }
    var mode = p[0] === 'train' ? 'train' : 'info', tab, view;
    try {
      if (mode === 'info') {
        switch (p[1]) {
          case 'wine': tab = 'wines'; view = winePage(p[2]); break;
          case 'glass': tab = 'glass'; view = glassPage(); break;
          case 'guests': tab = 'guests'; view = guestsPage(); break;
          case 'ref': tab = 'ref'; view = refPage(p[2], p[3]); break;
          default: tab = 'wines'; view = winesPage();
        }
      } else {
        switch (p[1]) {
          case 'course': tab = 'courses'; view = coursePage(p[2]); break;
          case 'lesson': tab = 'courses'; view = lessonPage(p[2], p[3]); break;
          case 'test': tab = 'courses'; view = lessonQuizPage(p[2], p[3]); break;
          case 'quiz': tab = 'quiz'; view = p[2] ? quizPage(p[2]) : quizzesPage(); break;
          case 'cards': tab = 'cards'; view = p[2] ? cardsPage(p[2]) : decksPage(); break;
          default: tab = 'courses'; view = coursesPage();
        }
      }
    } catch (e) { console.error(e); view = '<p>Something went wrong showing this page.</p><p><a href="#/info">Back to the wines</a></p>'; }
    drawChrome(mode, tab);
    main.innerHTML = view;
    if (after) { var f = after; after = null; f(); }
    if (!keepScroll) window.scrollTo(0, 0);
    keepScroll = false;
  }
  window.addEventListener('hashchange', route);
  document.addEventListener('click', function (e) {
    var tr = e.target.closest('[data-href]');
    if (tr && !e.target.closest('a')) location.hash = tr.getAttribute('data-href');
  });

  /* ======================================================================
     INFO: the wine bible
     ====================================================================== */
  var listState = { q: '', f: 'all', p: '' };
  var FILTERS = [['all', 'All'], ['glass', 'By the glass'], ['cor', 'Coravin'], ['sparkling', 'Sparkling'], ['white', 'White'],
    ['rose', 'Rosé'], ['red', 'Red'], ['sweet', 'Dessert'], ['u100', 'Under £100']];
  function hay(w) {
    if (!w._hay) w._hay = norm([w.name, w.short, w.menuName, w.appellation, w.region, w.grape, w.grapes, w.vintage, SEC[w.section],
      w.style.profile, w.note, w.sell, w.flag, w.taste, w.story, w.site, w.making, w.fact, w.food.join(' ')].join(' '));
    return w._hay;
  }
  function matches(w) {
    var f = listState.f;
    if (f === 'glass' && !w.glass) return false;
    if (f === 'cor' && w.pour !== 'COR') return false;
    if (f === 'u100' && !(w.bottle < 100)) return false;
    if (SEC[f] && w.section !== f) return false;
    if (listState.p && w.style.profile !== listState.p) return false;
    if (!listState.q) return true;
    var h = hay(w);
    return norm(listState.q).split(/\s+/).every(function (t) { return h.indexOf(t) >= 0; });
  }
  function wineRow(w) {
    var pr = '<b>' + gbp(w.bottle) + '</b>' + (w.glass ? '<small>' + w.glassMl + 'ml ' + gbp(w.glass) + '</small>' : '') + (w.size ? '<small>' + esc(bottleLabel(w)) + '</small>' : '');
    return '<li><a class="wrow' + rowClass(w) + '" href="' + wineHref(w.id) + '"><span class="nm">' + esc(w.name) + '</span>' +
      '<span class="ap">' + esc(w.appellation) + ' · ' + esc(w.vintage) + '</span>' +
      '<span class="tags">' + badge(w) + (w.style.profile ? '<span class="badge soft">' + esc(w.style.profile) + '</span>' : '') + '</span>' +
      '<span class="pr">' + pr + '</span></a></li>';
  }
  function listHtml() {
    var ws = D.wines.filter(matches);
    if (!ws.length) return '<p class="empty">No wine matches that. Try a grape, a region, a food or a producer.</p>';
    var out = '<p class="count">' + ws.length + (ws.length === 1 ? ' wine' : ' wines') + (listState.q ? ' mention “' + esc(listState.q) + '”' : '') + '</p>';
    D.sections.forEach(function (s) {
      var sw = ws.filter(function (w) { return w.section === s.key; });
      if (!sw.length) return;
      var nb = sw.filter(function (w) { return w.glass; }).length;
      out += '<div class="sec-h"><h2>' + esc(s.label) + '</h2><span>' + sw.length + ' · ' + nb + ' by the glass</span></div>';
      var reg = null, open = false;
      sw.forEach(function (w) {
        if (w.region !== reg) { if (open) out += '</ul>'; reg = w.region; out += '<p class="reg-h">' + esc(reg) + '</p><ul class="wlist">'; open = true; }
        out += wineRow(w);
      });
      if (open) out += '</ul>';
    });
    return out;
  }
  function winesPage() {
    after = function () {
      var inp = document.getElementById('q'), sel = document.getElementById('prof');
      function redraw() { document.getElementById('wl').innerHTML = listHtml(); }
      inp.addEventListener('input', function () { listState.q = inp.value; redraw(); });
      sel.addEventListener('change', function () { listState.p = sel.value; redraw(); });
      document.querySelectorAll('.chips .chip').forEach(function (b) {
        b.addEventListener('click', function () {
          listState.f = b.getAttribute('data-f');
          document.querySelectorAll('.chips .chip').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
          redraw();
        });
      });
    };
    var profiles = D.profiles.filter(function (p) { return D.wines.some(function (w) { return w.style.profile === p.key; }); });
    return '<p class="eyebrow">Info · The wine bible</p><h1>Every wine we pour</h1>' +
      '<div class="search">' + ICON_SEARCH + '<input id="q" type="search" placeholder="Search a wine, grape, region or dish" autocomplete="off" value="' + esc(listState.q) + '" aria-label="Search the wine list"></div>' +
      '<div class="chips" role="group" aria-label="Filter">' + FILTERS.map(function (f) {
        return '<button type="button" class="chip" data-f="' + f[0] + '" aria-pressed="' + (listState.f === f[0]) + '">' + esc(f[1]) + '</button>';
      }).join('') + '</div>' +
      (profiles.length ? '<label class="selectrow"><span>Style</span><select id="prof"><option value="">Any style</option>' + profiles.map(function (p) {
        return '<option' + (listState.p === p.key ? ' selected' : '') + '>' + esc(p.key) + '</option>';
      }).join('') + '</select></label>' : '<select id="prof" hidden></select>') +
      '<div id="wl">' + listHtml() + '</div>';
  }

  function priceTiles(w) {
    var t = [];
    if (w.glass) t.push([w.glassMl + 'ml glass', w.glass]);
    if (w.g175) t.push(['175ml glass', w.g175]);
    if (w.carafe) t.push(['500ml carafe', w.carafe]);
    t.push([bottleLabel(w), w.bottle]);
    return '<div class="prices">' + t.map(function (x) { return '<div class="price"><div class="k">' + esc(x[0]) + '</div><div class="v">' + gbp(x[1]) + '</div></div>'; }).join('') + '</div>';
  }
  function facts(w) {
    var s = w.style, f = [];
    if (s.profile) f.push(['Style', s.profile]);
    if (s.body) f.push(['Body', s.body]);
    if (s.sweetness) f.push(['Sweetness', s.sweetness]);
    if (s.acidity) f.push(['Acidity', s.acidity]);
    if (s.tannin) f.push(['Tannin', s.tannin]);
    if (s.oak) f.push(['Oak', s.oak]);
    if (w.abv) f.push(['Alcohol', w.abv]);
    if (!f.length) return '';
    return '<dl class="facts">' + f.map(function (x) { return '<div><dt>' + esc(x[0]) + '</dt><dd>' + esc(x[1]) + '</dd></div>'; }).join('') + '</dl>';
  }
  function more(title, body, open) {
    if (!body) return '';
    return '<details class="more"' + (open ? ' open' : '') + '><summary>' + esc(title) + '</summary><div>' + body + '</div></details>';
  }
  function winePage(id) {
    var w = byId[id];
    if (!w) return '<a class="back" href="#/info">‹ All wines</a><p>That wine is no longer on the list.</p>';
    var prev = D.wines[w.idx - 1], next = D.wines[w.idx + 1];
    var menuLine = w.menuName && norm(w.menuName) !== norm(w.name.replace(/,/g, '')) ? '<div class="ap">On the menu as <b>' + esc(w.menuName) + '</b></div>' : '';
    return '<a class="back" href="#/info">‹ All wines</a>' +
      '<div class="wine-h' + rowClass(w) + '"><p class="eyebrow">' + esc(SEC[w.section]) + ' · ' + esc(w.region) + '</p>' + badge(w) +
      '<h1>' + esc(w.name) + '</h1><div class="ap">' + esc(w.appellation) + ' · ' + esc(w.vintage) + (w.size ? ' · ' + esc(w.size) : '') + '</div>' + menuLine +
      (w.menuNote ? '<div class="ap muted">' + esc(w.menuNote) + '</div>' : '') + priceTiles(w) + '</div>' +
      '<div class="sell"><div class="k">Sell it</div><p>' + esc(w.sell) + '</p></div>' +
      (w.flag ? '<div class="flag"><b>Good to know</b>' + esc(w.flag) + '</div>' : '') +
      facts(w) +
      '<div class="block"><div class="k">In short</div><p>' + esc(w.note) + '</p></div>' +
      (w.taste ? '<div class="block"><div class="k">What it tastes like</div><p>' + esc(w.taste) + '</p></div>' : '') +
      (w.food.length ? '<div class="block"><div class="k">Good with</div><ul class="food">' + w.food.map(function (f) { return '<li>' + esc(f) + '</li>'; }).join('') + '</ul></div>' : '') +
      '<div class="block"><div class="k">Serving</div><p>' + esc(howServed(w)) + (w.pour === 'COR' ? ', no carafe' : '') + '.' + (w.serve ? ' ' + esc(w.serve) : '') + '</p></div>' +
      more('A story to tell', w.fact ? '<p>' + esc(w.fact) + '</p>' : '', true) +
      more('Grapes', '<p>' + esc(w.grapes || w.grape) + '</p>') +
      more('The producer', w.story ? '<p>' + esc(w.story) + '</p>' : '') +
      more('The vineyard', w.site ? '<p>' + esc(w.site) + '</p>' : '') +
      more('How it is made', w.making ? '<p>' + esc(w.making) + '</p>' : '') +
      more('The vintage', w.vintageNote ? '<p>' + esc(w.vintageNote) + '</p>' : '') +
      more('On the display wall', w.shelf.length ? '<ul class="shelf">' + w.shelf.map(function (s) { return '<li>' + esc(s) + '</li>'; }).join('') + '</ul>' : '') +
      more('Sources', w.sources && w.sources.length ? '<ul class="src">' + w.sources.map(function (u) { return '<li><a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(u.replace(/^https?:\/\/(www\.)?/, '').slice(0, 70)) + '</a></li>'; }).join('') + '</ul>' : '') +
      '<div class="pager">' + (prev ? '<a href="' + wineHref(prev.id) + '"><span>‹ Previous</span>' + esc(prev.short) + '</a>' : '<i></i>') +
      (next ? '<a class="next" href="' + wineHref(next.id) + '"><span>Next ›</span>' + esc(next.short) + '</a>' : '<i></i>') + '</div>';
  }

  function glassPage() {
    var out = '<p class="eyebrow">Info · Quick reference</p><h1>The ' + BTG.length + ' wines by the glass</h1>' +
      '<p class="lede">Glasses are 125ml, 175ml on request. Dessert and fortified wines are poured in 75ml. ◆ Coravin wines never go in a carafe. No carafes of sparkling or dessert wine.</p>';
    D.sections.forEach(function (s) {
      var ws = BTG.filter(function (w) { return w.section === s.key; });
      if (!ws.length) return;
      ws.sort(function (a, b) { return (a.pour === 'COR') - (b.pour === 'COR') || a.glass - b.glass || a.bottle - b.bottle; });
      var sweet = s.key === 'sweet';
      out += '<h2>' + esc(s.label) + '</h2><table class="gtable"><thead><tr><th>Wine</th><th>' + (sweet ? '75ml' : '125ml') + '</th>' +
        (sweet ? '' : '<th>175ml</th><th>Carafe</th>') + '<th>Bottle</th></tr></thead><tbody>';
      var corShown = false;
      ws.forEach(function (w) {
        if (w.pour === 'COR' && !corShown) { corShown = true; out += '<tr class="sub"><td colspan="5">◆ From the Coravin</td></tr>'; }
        out += '<tr data-href="' + wineHref(w.id) + '"><td><a class="nm" href="' + wineHref(w.id) + '">' + esc(w.short) + '</a><span class="ap">' + esc(w.appellation) + ' · ' + esc(w.vintage) + (w.size ? ' · ' + esc(w.size) : '') + '</span></td>' +
          '<td>' + gbp(w.glass) + '</td>' + (sweet ? '' : '<td>' + (w.g175 ? gbp(w.g175) : '<span class="dash">–</span>') + '</td><td>' + (w.carafe ? gbp(w.carafe) : '<span class="dash">–</span>') + '</td>') +
          '<td>' + gbp(w.bottle) + '</td></tr>';
      });
      out += '</tbody></table>';
    });
    return out;
  }

  function pickChip(id, kind) {
    var w = byId[id];
    var cls = kind === 'g' ? (w.pour === 'COR' ? 'pick c' : 'pick g') : 'pick';
    var price = kind === 'g' ? gbp(w.glass) : gbp(w.bottle);
    return '<a class="' + cls + '" href="' + wineHref(id) + '">' + esc(w.short) + (kind === 'g' && w.pour === 'COR' ? ' ◆' : '') + ' <b>' + price + '</b></a>';
  }
  var guestQ = '';
  function steerHtml() {
    var rows = D.steer.filter(function (s) {
      if (!guestQ) return true;
      var h = norm(s.q + ' ' + s.tip + ' ' + s.glass.concat(s.bottle).map(function (id) { return byId[id].short; }).join(' '));
      return norm(guestQ).split(/\s+/).every(function (t) { return h.indexOf(t) >= 0; });
    });
    if (!rows.length) return '<p class="empty">Nothing matches. Try “light”, “Burgundy” or “sweet”.</p>';
    return '<ul class="steer">' + rows.map(function (s) {
      return '<li><p class="q">' + esc(s.q) + '</p>' +
        '<div class="lbl">By the glass</div><div class="picks">' + (s.glass.length ? s.glass.map(function (id) { return pickChip(id, 'g'); }).join('') : '<span class="muted small">Nothing by the glass</span>') + '</div>' +
        (s.bottle.length ? '<div class="lbl">Bottle only</div><div class="picks">' + s.bottle.map(function (id) { return pickChip(id, 'b'); }).join('') + '</div>' : '') +
        (s.tip ? '<p class="tip">' + esc(s.tip) + '</p>' : '') + '</li>';
    }).join('') + '</ul>';
  }
  function guestsPage() {
    after = function () {
      var inp = document.getElementById('gq');
      inp.addEventListener('input', function () { guestQ = inp.value; document.getElementById('sl').innerHTML = steerHtml(); });
    };
    return '<p class="eyebrow">Info · Steering</p><h1>When a guest says…</h1>' +
      '<p class="lede">Guests usually describe a style, or name a wine we don\'t list. Start with the glass, then trade up. Every glass wine is also sold by the bottle.</p>' +
      '<a class="callout" href="#/info/ref/sancerre"><b>When a guest asks for Sancerre</b><span>What we pour instead, and how to say it ›</span></a>' +
      '<div class="search">' + ICON_SEARCH + '<input id="gq" type="search" placeholder="Search: light, Burgundy, sweet…" autocomplete="off" value="' + esc(guestQ) + '" aria-label="Search guest requests"></div>' +
      '<div id="sl">' + steerHtml() + '</div>';
  }

  var REF = [
    ['list', 'How the list works', 'Measures, the Coravin, the house wines, natural wines'],
    ['service', 'Wine service at Finch', 'What the sommelier does, and how the floor supports it'],
    ['sancerre', 'When a guest asks for Sancerre', 'What we pour instead, and how to say it'],
    ['styles', 'Styles at a glance', 'Every wine grouped by what it tastes like'],
    ['grapes', 'Grapes on the list', 'Every grape, what it tastes like and where to find it'],
    ['glossary', 'Glossary', 'Short answers for the terms guests use'],
    ['about', 'About this app', 'Installing it, updates and your progress']
  ];
  function refPage(p) {
    var back = '<a class="back" href="#/info/ref">‹ Reference</a>';
    if (p === 'list') {
      return back + '<p class="eyebrow">Reference</p><h1>How the list works</h1>' +
        '<p class="lede">' + D.wines.length + ' wines, ' + BTG.length + ' of them by the glass. Learn the glass wines first: they cover most of the evening.</p>' +
        '<div class="cards">' + D.rules.map(function (r) { return '<div class="card"><h3>' + esc(r.t) + '</h3><p>' + esc(r.b) + '</p></div>'; }).join('') + '</div>' +
        '<h2>The value end</h2><p>' + valueEnd() + '</p>';
    }
    if (p === 'service') {
      var S = D.service;
      return back + '<p class="eyebrow">Reference</p><h1>Wine service at Finch</h1><p class="lede">' + esc(S.intro) + '</p>' +
        '<div class="somm">' + esc(S.somm) + '</div>' +
        '<h2>The principles</h2><ul class="points">' + S.principles.map(function (x) { return '<li><b>' + esc(x[0]) + '</b> ' + esc(x[1]) + '</li>'; }).join('') + '</ul>' +
        '<h2>Steps of service: a bottle</h2><ol class="steps">' + S.bottle.map(function (x) { return '<li><b>' + esc(x[0]) + '</b> ' + esc(x[1]) + '</li>'; }).join('') + '</ol>' +
        '<h2>Steps of service: by the glass</h2><ol class="steps">' + S.glass.map(function (x) { return '<li>' + esc(x[1]) + '</li>'; }).join('') + '</ol>' +
        '<h2>What the floor team can do</h2><ul class="points">' + S.floor.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>';
    }
    if (p === 'sancerre') {
      var C = D.sancerre;
      return back + '<p class="eyebrow">Reference · Steering</p><h1>When a guest asks for Sancerre</h1><p class="lede">' + esc(C.intro) + '</p>' +
        C.sections.map(function (s) {
          var h = '<h3>' + esc(s.h) + '</h3>', list = [];
          s.parts.forEach(function (x) {
            if (x.k === 'li') { list.push('<li>' + x.t + '</li>'); return; }
            if (list.length) { h += '<ul class="points">' + list.join('') + '</ul>'; list = []; }
            h += x.k === 'q' ? '<blockquote>' + esc(x.t) + '</blockquote>' : '<p>' + x.t + '</p>';
          });
          if (list.length) h += '<ul class="points">' + list.join('') + '</ul>';
          return h;
        }).join('') +
        '<div class="picks" style="margin-top:18px">' + pickChip('w013', 'g') + pickChip('w020', 'b') + '</div>';
    }
    if (p === 'styles') {
      return back + '<p class="eyebrow">Reference</p><h1>Styles at a glance</h1><p class="lede">Every wine on the list, grouped by what it tastes like. Glass wines show their glass price.</p>' +
        D.profiles.map(function (pf) {
          var ws = D.wines.filter(function (w) { return w.style.profile === pf.key; });
          if (!ws.length) return '';
          return '<h2>' + esc(pf.key) + '</h2><p class="small muted">' + esc(pf.blurb) + '</p><div class="picks">' +
            ws.map(function (w) { return pickChip(w.id, w.glass ? 'g' : 'b'); }).join('') + '</div>';
        }).join('');
    }
    if (p === 'grapes') {
      function gl(rows) { return '<ul class="grapes">' + rows.map(function (g) { return '<li><b>' + esc(g[0]) + '</b>' + esc(g[1]) + '<span class="on">On our list: ' + esc(g[2]) + '</span></li>'; }).join('') + '</ul>'; }
      return back + '<p class="eyebrow">Reference</p><h1>Grapes on the list</h1>' +
        '<p class="lede">A guest who knows one grape can usually be led to a wine they don\'t know yet. Blends appear under each of their main grapes.</p>' +
        '<h2>White grapes</h2>' + gl(D.grapes.white) + '<h2>Red grapes</h2>' + gl(D.grapes.red);
    }
    if (p === 'glossary') {
      return back + '<p class="eyebrow">Reference</p><h1>Glossary</h1><p class="lede">Short answers for the terms guests use, and the ones on the list.</p>' +
        '<dl class="gloss">' + D.gloss.map(function (g) { return '<div><dt>' + esc(g[0]) + '</dt><dd>' + esc(g[1]) + '</dd></div>'; }).join('') + '</dl>';
    }
    if (p === 'about') {
      after = function () { var b = document.getElementById('inst'); if (b && installEvt) { b.hidden = false; b.onclick = function () { installEvt.prompt(); }; } };
      return back + '<p class="eyebrow">Reference</p><h1>About this app</h1><div class="about">' +
        '<p><b>Info</b> is the wine bible: every wine, the glass list, what to offer guests and the house rules. <b>Training</b> is where you learn: short courses on tasting, styles, grapes and regions, then quizzes and flashcards.</p>' +
        '<p>Prices, vintages, what is poured by the glass and where each bottle sits on the wall come from the Cellar Book, taken on <b>' + esc(fmtDate(D.takenAt)) + '</b>. Vintages change as bins run out, so always read the label.</p>' +
        '<div class="install"><b>Put it on your phone</b><span><b>iPhone:</b> open this page in Safari, tap Share, then “Add to Home Screen”.</span><span><b>Android:</b> open it in Chrome, tap ⋮, then “Install app” or “Add to Home screen”.</span><button id="inst" class="btn primary" hidden>Install the app</button></div>' +
        '<p>Once it has been opened, the app works without a connection. When the list changes, the new version downloads the next time you open the app online, and a message offers to reload.</p>' +
        '<p>Your training progress is kept on this phone only. <button class="btn" id="reset" type="button" style="min-height:40px;margin-top:6px">Reset my progress</button></p>' +
        '<p class="muted small">Questions about the list: ask Simon.</p></div>';
    }
    return '<p class="eyebrow">Info</p><h1>Reference</h1><p class="lede">The house rules and the background to the list, to look up when you need it.</p>' +
      '<ul class="menu">' + REF.map(function (g) { return '<li><a href="#/info/ref/' + g[0] + '"><b>' + esc(g[1]) + '</b><span>' + esc(g[2]) + '</span></a></li>'; }).join('') + '</ul>' +
      '<a class="callout alt" href="#/train"><b>Learning the list?</b><span>Go to Training for courses, quizzes and flashcards ›</span></a>';
  }
  document.addEventListener('click', function (e) {
    if (e.target.id === 'reset' && confirm('Reset all your training progress on this phone?')) {
      ['boxes', 'misses', 'best', 'lessons'].forEach(function (k) { store.set(k, k === 'misses' ? [] : {}); });
      toast('Progress reset');
    }
  });
  function fmtDate(iso) { var d = new Date(iso + 'T12:00:00'); return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }); }
  function valueEnd() {
    var under = D.wines.filter(function (w) { return w.bottle < 100; }).sort(function (a, b) { return a.bottle - b.bottle; });
    var parts = D.sections.map(function (s) {
      var ws = under.filter(function (w) { return w.section === s.key; });
      return ws.length ? esc(s.label) + ': ' + ws.map(function (w) { return '<b>' + esc(w.short) + (w.size ? ' (' + esc(bottleLabel(w).toLowerCase()) + ')' : '') + ' ' + gbp(w.bottle) + '</b>'; }).join(', ') + '.' : '';
    }).filter(Boolean);
    var still = BTG.filter(function (w) { return w.section !== 'sweet' && w.section !== 'sparkling'; });
    var low = Math.min.apply(null, still.map(function (w) { return w.glass; }));
    var entry = still.filter(function (w) { return w.glass === low; }).map(function (w) { return w.short; });
    return under.length + ' bottles are under £100. ' + parts.join(' ') + ' The entry glasses are all ' + gbp(low) + ': ' + esc(entry.join(', ')) + '.';
  }

  /* ======================================================================
     TRAINING
     ====================================================================== */
  var COURSE = {}; D.courses.forEach(function (c) { COURSE[c.id] = c; });
  var PASS = 0.8;
  function lessonBest(cid, lid) { return store.get('lessons', {})[cid + '/' + lid]; }
  function lessonDone(cid, lid) { var b = lessonBest(cid, lid); return b != null && b >= PASS; }
  function courseDone(c) { return c.lessons.filter(function (l) { return lessonDone(c.id, l.id); }).length; }
  function lessonWines(l) {
    var ids = l.wines.slice();
    D.wines.forEach(function (w) { if (l.profiles.indexOf(w.style.profile) >= 0 && ids.indexOf(w.id) < 0) ids.push(w.id); });
    return ids.filter(function (id) { return byId[id]; });
  }
  function nextLesson() {
    for (var i = 0; i < D.courses.length; i++) for (var j = 0; j < D.courses[i].lessons.length; j++) {
      var c = D.courses[i], l = c.lessons[j];
      if (!lessonDone(c.id, l.id)) return { c: c, l: l };
    }
    return null;
  }
  function meter(n, of) { return '<div class="meter" aria-hidden="true"><i style="width:' + Math.round(100 * n / Math.max(1, of)) + '%"></i></div>'; }

  function coursesPage() {
    var total = 0, done = 0;
    D.courses.forEach(function (c) { total += c.lessons.length; done += courseDone(c); });
    var nx = nextLesson();
    return '<p class="eyebrow">Training</p><h1>Learn the list</h1>' +
      '<p class="lede">Short lessons on tasting, styles, grapes and regions, all built around the wines we pour. Each lesson ends with a short quiz; get ' + Math.round(PASS * 100) + '% to tick it off.</p>' +
      '<div class="overall"><div><b>' + done + ' of ' + total + '</b> lessons done</div>' + meter(done, total) + '</div>' +
      (nx ? '<a class="callout" href="#/train/lesson/' + nx.c.id + '/' + nx.l.id + '"><b>' + (done ? 'Carry on' : 'Start here') + ': ' + esc(nx.l.title) + '</b><span>' + esc(nx.c.title) + ' ›</span></a>' : '<p class="done-all">Every lesson done. Keep sharp with the quizzes.</p>') +
      '<div class="tgrid">' + D.courses.map(function (c) {
        var d = courseDone(c);
        return '<a class="tcard" href="#/train/course/' + c.id + '"><b>' + esc(c.title) + '</b><span>' + esc(c.blurb) + '</span>' + meter(d, c.lessons.length) + '<small>' + d + ' of ' + c.lessons.length + ' lessons done</small></a>';
      }).join('') + '</div>';
  }
  function coursePage(cid) {
    var c = COURSE[cid];
    if (!c) return '<a class="back" href="#/train">‹ Courses</a><p>That course does not exist.</p>';
    return '<a class="back" href="#/train">‹ Courses</a><p class="eyebrow">Course</p><h1>' + esc(c.title) + '</h1><p class="lede">' + esc(c.blurb) + '</p>' +
      '<ol class="lessons">' + c.lessons.map(function (l, i) {
        var b = lessonBest(c.id, l.id), ok = b != null && b >= PASS;
        return '<li><a href="#/train/lesson/' + c.id + '/' + l.id + '" class="' + (ok ? 'done' : '') + '"><span class="n">' + (ok ? '✓' : i + 1) + '</span><span class="t"><b>' + esc(l.title) + '</b><small>' +
          l.cards.length + ' short sections · ' + (l.quiz.length + (l.profiles.length ? 2 : 0)) + ' questions' + (b != null ? ' · best ' + Math.round(b * 100) + '%' : '') + '</small></span></a></li>';
      }).join('') + '</ol>';
  }
  function lessonPage(cid, lid) {
    var c = COURSE[cid], l = c && c.lessons.filter(function (x) { return x.id === lid; })[0];
    if (!l) return '<a class="back" href="#/train">‹ Courses</a><p>That lesson does not exist.</p>';
    var ws = lessonWines(l);
    var i = c.lessons.indexOf(l), nextL = c.lessons[i + 1];
    return '<a class="back" href="#/train/course/' + c.id + '">‹ ' + esc(c.title) + '</a><p class="eyebrow">Lesson ' + (i + 1) + ' of ' + c.lessons.length + '</p><h1>' + esc(l.title) + '</h1>' +
      '<div class="lesson">' + l.cards.map(function (k) { return '<section><h3>' + esc(k.h) + '</h3><p>' + k.b + '</p></section>'; }).join('') + '</div>' +
      (ws.length ? '<h2>On our list</h2><div class="picks">' + ws.map(function (id) { return pickChip(id, byId[id].glass ? 'g' : 'b'); }).join('') + '</div>' : '') +
      '<div class="stack" style="margin-top:22px"><a class="btn primary wide" href="#/train/test/' + c.id + '/' + l.id + '">Take the lesson quiz</a>' +
      (nextL ? '<a class="btn wide" href="#/train/lesson/' + c.id + '/' + nextL.id + '">Next lesson: ' + esc(nextL.title) + '</a>' : '') + '</div>';
  }

  /* profile lessons get two extra questions built from the list itself */
  function profileQuestions(l) {
    var out = [];
    l.profiles.forEach(function (pf) {
      var ins = D.wines.filter(function (w) { return w.style.profile === pf; });
      var group = PROF[pf] ? PROF[pf].group : null;
      var outs = D.wines.filter(function (w) { return w.style.profile && l.profiles.indexOf(w.style.profile) < 0 && (!PROF[w.style.profile] || PROF[w.style.profile].group !== group || group === 'sparkling' || group === 'sweet'); });
      if (ins.length && outs.length >= 3) {
        var w = pick(ins), o = shuffle(outs).slice(0, 3).map(function (x) { return x.short; });
        out.push({ q: 'Which of these is a ' + pf.toLowerCase() + '?', o: shuffle(o.concat([w.short])), a: w.short, why: w.short + ' is a ' + pf.toLowerCase() + '. ' + w.sell, w: w });
      }
    });
    return shuffle(out).slice(0, 2);
  }
  var lq = null;
  function lessonQuizPage(cid, lid) {
    var c = COURSE[cid], l = c && c.lessons.filter(function (x) { return x.id === lid; })[0];
    if (!l) return '<a class="back" href="#/train">‹ Courses</a><p>That lesson does not exist.</p>';
    var key = cid + '/' + lid;
    if (!lq || lq.key !== key) {
      var qs = l.quiz.map(function (q) { return { q: esc(q.q), o: shuffle(q.o), a: q.a, why: q.why, k: l.title }; }).concat(profileQuestions(l).map(function (q) { q.q = esc(q.q); q.k = l.title; return q; }));
      lq = { key: key, qs: shuffle(qs), i: 0, chosen: null, right: 0, missed: [] };
    }
    var back = '<a class="back" href="#/train/lesson/' + cid + '/' + lid + '">‹ ' + esc(l.title) + '</a>';
    if (lq.i >= lq.qs.length) {
      var pct = lq.right / lq.qs.length, all = store.get('lessons', {}), prev = all[key];
      if (prev == null || pct > prev) { all[key] = pct; store.set('lessons', all); }
      var passed = pct >= PASS, i = c.lessons.indexOf(l), nextL = c.lessons[i + 1], r = lq.right, n = lq.qs.length;
      lq = null;
      after = function () { document.getElementById('again').addEventListener('click', function () { lq = null; route(); }); };
      return back + '<div class="score"><p class="eyebrow">' + esc(l.title) + '</p><div class="big">' + r + ' / ' + n + '</div><p>' +
        (passed ? 'Lesson done. ✓' : 'You need ' + Math.ceil(PASS * n) + ' to tick this lesson off. Have another read and try again.') + '</p></div>' +
        '<div class="stack">' + (passed && nextL ? '<a class="btn primary wide" href="#/train/lesson/' + cid + '/' + nextL.id + '">Next lesson: ' + esc(nextL.title) + '</a>' : '') +
        (passed && !nextL ? '<a class="btn primary wide" href="#/train">Back to the courses</a>' : '') +
        '<button type="button" class="btn wide' + (passed ? '' : ' primary') + '" id="again">Try the quiz again</button>' +
        '<a class="btn wide" href="#/train/lesson/' + cid + '/' + lid + '">Read the lesson again</a></div>';
    }
    return back + quizBody(lq, l.title, function () { lessonQuizPage(cid, lid); });
  }

  /* shared question renderer for lesson quizzes and practice quizzes */
  function quizBody(st, title) {
    var q = st.qs[st.i];
    after = function () {
      document.querySelectorAll('.opt').forEach(function (b) {
        b.addEventListener('click', function () {
          if (st.chosen != null) return;
          st.chosen = b.getAttribute('data-o');
          if (st.chosen === q.a) st.right++;
          else if (q.w) {
            st.missed.push(q.w);
            var m = store.get('misses', []); if (m.indexOf(q.w.id) < 0) { m.push(q.w.id); store.set('misses', m); }
          }
          keepScroll = true; route();
        });
      });
      var nx = document.getElementById('next');
      if (nx) { nx.addEventListener('click', function () { st.i++; st.chosen = null; route(); }); nx.focus({ preventScroll: true }); }
    };
    var answered = st.chosen != null, ok = st.chosen === q.a;
    return '<div class="progress"><span>' + esc(title) + '</span><span>Question ' + (st.i + 1) + ' of ' + st.qs.length + ' · ' + st.right + ' right</span></div>' +
      '<div class="qbox"><div class="qk">' + esc(q.k) + '</div><p class="qt">' + q.q + '</p>' + (q.sub ? '<p class="muted small" style="margin:8px 0 0">' + esc(q.sub) + '</p>' : '') + '</div>' +
      '<div class="opts">' + q.o.map(function (o) {
        var cls = 'opt', mark = '';
        if (answered) { if (o === q.a) { cls += ' right'; mark = '✓'; } else if (o === st.chosen) { cls += ' wrong'; mark = '✗'; } }
        return '<button type="button" class="' + cls + '" data-o="' + esc(o) + '"' + (answered ? ' disabled' : '') + '><span>' + esc(o) + '</span><span class="mark">' + mark + '</span></button>';
      }).join('') + '</div>' +
      (answered ? '<div class="explain"><div class="v ' + (ok ? 'ok">Right.' : 'no">Not quite: it\'s ' + esc(q.a) + '.') + '</div>' + (q.html || esc(q.why || '')) +
        (q.w ? ' <a href="' + wineHref(q.w.id) + '">Open the wine ›</a>' : '') + '</div>' +
        '<button type="button" class="btn primary wide" id="next">' + (st.i + 1 < st.qs.length ? 'Next question' : 'See your score') + '</button>' : '');
  }

  /* ---------- practice quizzes ---------- */
  var QUIZ = {
    guest: { t: 'The guest says…', d: 'Pick the right glass for the request' },
    pour: { t: 'Glass or bottle?', d: 'By the glass, on the Coravin, or bottle only' },
    glassprice: { t: 'Price of a glass', d: 'What does a glass cost?' },
    grape: { t: 'Name the grape', d: 'The main grape in each wine' },
    style: { t: 'What style is it?', d: 'Light, rich, aromatic, savoury…' },
    region: { t: 'Where is it from?', d: 'Region by region' },
    sell: { t: 'Whose selling line?', d: 'Match the line to the wine' },
    bottleprice: { t: 'Bottle prices', d: 'Roughly what a bottle costs' },
    mixed: { t: 'Mixed round', d: 'A bit of everything' }
  };
  function opts(correct, pool, n) {
    var o = uniq(shuffle(pool.filter(function (x) { return x !== correct; }))).slice(0, (n || 4) - 1);
    return shuffle(o.concat([correct]));
  }
  function nearPrices(v, all) {
    var others = uniq(all.filter(function (x) { return x !== v; }));
    others.sort(function (a, b) { return Math.abs(a - v) - Math.abs(b - v); });
    return shuffle(others.slice(0, 3).concat([v]));
  }
  function explainWine(w, extra) {
    return '<b>' + esc(w.name) + '</b>, ' + esc(w.appellation) + ' ' + esc(w.vintage) + '. ' + esc(w.grape) + '. ' + esc(howServed(w)) +
      (w.glass ? ' at ' + gbp(w.glass) + ' (' + w.glassMl + 'ml)' : '') + ', ' + esc(bottleLabel(w).toLowerCase()) + ' ' + gbp(w.bottle) + '. <i>' + esc(extra || w.sell) + '</i>';
  }
  var MAKE = {
    grape: function () {
      var w = pick(D.wines), pool = uniq(D.wines.map(function (x) { return x.g; })).filter(function (g) { return w.grape.indexOf(g) < 0 && (w.grapes || '').indexOf(g) < 0; });
      return { k: 'Name the grape', q: 'What is the main grape in the <i>' + esc(w.name) + '</i>?', sub: w.appellation, a: w.g, o: opts(w.g, pool), w: w };
    },
    pour: function () {
      var w = Math.random() < 0.5 ? pick(BTG) : pick(D.wines);
      return { k: 'Glass or bottle?', q: 'How do we serve the <i>' + esc(w.name) + '</i>?', sub: w.appellation, a: howServed(w), o: ['By the glass', 'By the glass, on the Coravin', 'Bottle only'], w: w };
    },
    glassprice: function () {
      var w = pick(BTG);
      var all = BTG.filter(function (x) { return x.glassMl === w.glassMl; }).map(function (x) { return x.glass; }).concat([w.glass - 1, w.glass + 1, w.glass + 2, w.glass - 2]);
      return { k: 'Price of a glass', q: 'What does a ' + w.glassMl + 'ml glass of the <i>' + esc(w.short) + '</i> cost?', sub: w.name, a: gbp(w.glass), o: nearPrices(w.glass, all).map(gbp), w: w };
    },
    bottleprice: function () {
      var w = pick(D.wines), sorted = D.wines.slice().sort(function (a, b) { return a.bottle - b.bottle; });
      var i = sorted.indexOf(w), near = sorted.slice(Math.max(0, i - 4), i + 5).map(function (x) { return x.bottle; });
      return { k: 'Bottle prices', q: 'What is a ' + esc(bottleLabel(w).toLowerCase()) + ' of the <i>' + esc(w.short) + '</i>?', sub: w.name + ' · ' + w.vintage, a: gbp(w.bottle), o: nearPrices(w.bottle, near).map(gbp), w: w };
    },
    region: function () {
      var w = pick(D.wines), pool = uniq(D.wines.map(function (x) { return x.region; }));
      return { k: 'Where is it from?', q: 'Where is the <i>' + esc(w.name) + '</i> from?', sub: SEC[w.section] + ' · ' + w.vintage, a: w.region, o: opts(w.region, pool), w: w };
    },
    style: function () {
      var ws = D.wines.filter(function (x) { return x.style.profile; });
      if (!ws.length) return MAKE.region();
      var w = pick(ws), grp = PROF[w.style.profile] ? PROF[w.style.profile].group : '';
      var pool = D.profiles.filter(function (p) { return p.group === grp || (grp === 'rose' && p.group === 'white') || (grp === 'sweet' && p.group === 'white'); }).map(function (p) { return p.key; });
      if (pool.length < 4) pool = pool.concat(D.profiles.map(function (p) { return p.key; }));
      return { k: 'What style is it?', q: 'Which style best describes the <i>' + esc(w.name) + '</i>?', sub: w.appellation + ' · ' + w.grape, a: w.style.profile, o: opts(w.style.profile, pool), w: w };
    },
    sell: function () {
      var w = pick(D.wines), pool = D.wines.filter(function (x) { return x.section === w.section; }).map(function (x) { return x.short; });
      return { k: 'Whose selling line?', q: '“' + esc(w.sell) + '”', sub: 'Which wine is this?', a: w.short, o: opts(w.short, pool), w: w };
    },
    guest: function () {
      var s = pick(D.steer.filter(function (x) { return x.glass.length; }));
      var w = byId[pick(s.glass)];
      var pool = BTG.filter(function (x) { return s.glass.indexOf(x.id) < 0 && x.section !== w.section; }).map(function (x) { return x.short; });
      return { k: 'The guest says…', q: 'A guest asks for ' + esc(s.q) + '. Which glass do you offer?', sub: '', a: w.short, o: opts(w.short, pool), w: w, tip: s.tip };
    }
  };
  var qz = null;
  function newQuiz(mode) {
    var qs = [], seen = {}, tries = 0;
    while (qs.length < 10 && tries++ < 400) {
      var m = mode === 'mixed' ? pick(Object.keys(MAKE)) : mode;
      var q = MAKE[m]();
      var sig = m + q.w.id + q.q;
      if (seen[sig] || q.o.length < 3) continue;
      seen[sig] = 1; q.html = explainWine(q.w, q.tip); qs.push(q);
    }
    return { mode: mode, qs: qs, i: 0, chosen: null, right: 0, missed: [] };
  }
  function quizzesPage() {
    var best = store.get('best', {});
    return '<p class="eyebrow">Training · Practice</p><h1>Quizzes</h1><p class="lede">Ten questions at a time, built from the list as it is today. Wrong answers go into a flashcard deck so you can go over them.</p>' +
      '<div class="tgrid">' + Object.keys(QUIZ).map(function (k) {
        var q = QUIZ[k];
        return '<a class="tcard" href="#/train/quiz/' + k + '"><b>' + esc(q.t) + '</b><span>' + esc(q.d) + '</span><small>' + (best[k] != null ? 'Best: ' + best[k] + ' / 10' : '10 questions') + '</small></a>';
      }).join('') + '</div>';
  }
  function quizPage(mode) {
    var back = '<a class="back" href="#/train/quiz">‹ Quizzes</a>';
    if (!QUIZ[mode]) return back + '<p>That quiz does not exist.</p>';
    if (!qz || qz.mode !== mode) qz = newQuiz(mode);
    if (qz.i >= qz.qs.length) {
      var best = store.get('best', {}), r = qz.right, missed = qz.missed;
      var hadBest = best[mode] != null, isBest = !hadBest || r > best[mode];
      if (isBest) { best[mode] = r; store.set('best', best); }
      qz = null;
      after = function () { document.getElementById('again').addEventListener('click', function () { qz = null; route(); }); };
      return back + '<div class="score"><p class="eyebrow">' + esc(QUIZ[mode].t) + '</p><div class="big">' + r + ' / 10</div><p>' +
        (r === 10 ? 'Perfect round.' : r >= 8 ? 'Very good.' : r >= 5 ? 'Getting there.' : 'Keep at it: try the flashcards first.') + (hadBest && isBest ? ' A new best.' : '') + '</p></div>' +
        (missed.length ? '<h2>To look at again</h2><ul class="missed">' + missed.map(function (w) { return '<li><a href="' + wineHref(w.id) + '">' + esc(w.name) + '<span>' + esc(w.appellation) + '</span></a></li>'; }).join('') + '</ul>' : '') +
        '<div class="stack"><button type="button" class="btn primary wide" id="again">Play again</button>' +
        (missed.length ? '<a class="btn wide" href="#/train/cards/misses">Flashcards of your misses</a>' : '') + '<a class="btn wide" href="#/train/quiz">All quizzes</a></div>';
    }
    return back + quizBody(qz, QUIZ[mode].t);
  }

  /* ---------- flashcards (Leitner boxes: 0 new, 1 seen, 2+ known) ---------- */
  function wineCard(w) { return { key: 'w:' + w.id, kind: 'wine', w: w }; }
  function secCards(sec) { return D.wines.filter(function (w) { return w.section === sec; }).map(wineCard); }
  var DECKS = {
    glass: { t: 'By the glass', d: 'The ' + BTG.length + ' wines we pour by the glass', cards: function () { return BTG.map(wineCard); } },
    guests: { t: 'The guest says…', d: 'What to offer for the common requests', cards: function () { return D.steer.map(function (s, i) { return { key: 'st:' + i, kind: 'steer', s: s }; }); } },
    sparkling: { t: 'Champagne & sparkling', cards: function () { return secCards('sparkling'); } },
    white: { t: 'White', cards: function () { return secCards('white'); } },
    red: { t: 'Red', cards: function () { return secCards('red'); } },
    rosesweet: { t: 'Rosé & dessert', cards: function () { return secCards('rose').concat(secCards('sweet')); } },
    all: { t: 'The whole list', d: 'All ' + D.wines.length + ' wines', cards: function () { return D.wines.map(wineCard); } },
    grapes: { t: 'Grapes', d: 'What each grape tastes like', cards: function () { return D.grapes.white.concat(D.grapes.red).map(function (g) { return { key: 'gr:' + g[0], kind: 'grape', g: g }; }); } },
    gloss: { t: 'Glossary', d: 'Wine words, in plain English', cards: function () { return D.gloss.map(function (g) { return { key: 'gl:' + g[0], kind: 'gloss', g: g }; }); } },
    misses: { t: 'Review your misses', d: 'Wines you got wrong in a quiz', cards: function () { return store.get('misses', []).filter(function (id) { return byId[id]; }).map(function (id) { return wineCard(byId[id]); }); } }
  };
  ['sparkling', 'white', 'red', 'rosesweet'].forEach(function (k) { DECKS[k].d = DECKS[k].cards().length + ' wines'; });
  function known(cards) { var b = store.get('boxes', {}); return cards.filter(function (c) { return (b[c.key] || 0) >= 2; }).length; }
  function decksPage() {
    var deckTile = function (k) {
      var d = DECKS[k], cs = d.cards(), kn = known(cs);
      return '<a class="tcard' + (k === 'misses' ? ' review' : '') + '" href="#/train/cards/' + k + '"><b>' + esc(d.t) + '</b><span>' + esc(d.d) + '</span>' +
        (k === 'misses' ? '' : meter(kn, cs.length) + '<small>' + kn + ' of ' + cs.length + ' known</small>') + '</a>';
    };
    return '<p class="eyebrow">Training · Practice</p><h1>Flashcards</h1><p class="lede">Read the front, say the answer to yourself, then turn it over. Cards you know come back less often.</p>' +
      '<div class="tgrid">' + (DECKS.misses.cards().length ? deckTile('misses') : '') +
      ['glass', 'guests', 'sparkling', 'white', 'red', 'rosesweet', 'all', 'grapes', 'gloss'].map(deckTile).join('') + '</div>';
  }
  var fc = null;
  function cardsPage(deck) {
    var d = DECKS[deck], back = '<a class="back" href="#/train/cards">‹ Flashcards</a>';
    if (!d) return back + '<p>That deck does not exist.</p>';
    if (!fc || fc.deck !== deck) {
      var boxes = store.get('boxes', {});
      var cs = shuffle(d.cards()).sort(function (a, b) { return (boxes[a.key] || 0) - (boxes[b.key] || 0); }).slice(0, 15);
      fc = { deck: deck, cards: cs, i: 0, flipped: false, right: 0 };
    }
    if (!fc.cards.length) { fc = null; return back + '<h1>' + esc(d.t) + '</h1><p class="lede">Nothing to review here. Nice work.</p>'; }
    if (fc.i >= fc.cards.length) {
      var r = fc.right, n = fc.cards.length; fc = null;
      return back + '<div class="score"><p class="eyebrow">' + esc(d.t) + '</p><div class="big">' + r + ' / ' + n + '</div><p>cards you knew this time</p></div>' +
        '<div class="stack"><a class="btn primary wide" href="#/train/cards/' + deck + '">Another round</a><a class="btn wide" href="#/train/cards">All decks</a></div>';
    }
    var c = fc.cards[fc.i];
    after = function () {
      document.getElementById('face').addEventListener('click', function () { fc.flipped = !fc.flipped; keepScroll = true; route(); });
      var turn = document.getElementById('turn'); if (turn) turn.addEventListener('click', function () { fc.flipped = true; keepScroll = true; route(); });
      document.querySelectorAll('[data-ans]').forEach(function (b) {
        b.addEventListener('click', function () {
          var ok = b.getAttribute('data-ans') === '1', boxes = store.get('boxes', {});
          boxes[c.key] = ok ? Math.min(4, (boxes[c.key] || 0) + 1) : 0;
          store.set('boxes', boxes);
          if (ok) { fc.right++; if (c.kind === 'wine') { var m = store.get('misses', []); store.set('misses', m.filter(function (x) { return x !== c.w.id; })); } }
          fc.i++; fc.flipped = false; keepScroll = true; route();
        });
      });
    };
    return back + '<div class="progress"><span>' + esc(d.t) + '</span><span>' + (fc.i + 1) + ' / ' + fc.cards.length + '</span></div>' +
      '<div class="flash"><button type="button" id="face" class="face' + (fc.flipped ? ' back flip-in' : '') + '" aria-label="' + (fc.flipped ? 'Show the front' : 'Turn the card over') + '">' +
      (fc.flipped ? cardBack(c) : cardFront(c)) + '</button></div>' +
      (fc.flipped ? '<div class="actions"><button type="button" class="btn again" data-ans="0">Not yet</button><button type="button" class="btn primary" data-ans="1">I knew it</button></div>'
        : '<button type="button" class="btn wide" id="turn">Turn over</button>');
  }
  function cardFront(c) {
    if (c.kind === 'wine') {
      var w = c.w;
      return '<span class="eyebrow">' + esc(SEC[w.section]) + '</span><span class="front-t">' + esc(w.name) + '</span><span class="muted">' + esc(w.appellation) + ' · ' + esc(w.vintage) + '</span>' +
        '<span class="hint">Grape, style, how we serve it, the price and the selling line? Tap to check.</span>';
    }
    if (c.kind === 'steer') return '<span class="eyebrow">The guest says</span><span class="front-t">' + esc(c.s.q) + '</span><span class="hint">What do you offer? Tap to check.</span>';
    if (c.kind === 'grape') return '<span class="eyebrow">Grape</span><span class="front-t">' + esc(c.g[0]) + '</span><span class="hint">What does it taste like, and which of our wines is it in?</span>';
    return '<span class="eyebrow">Glossary</span><span class="front-t">' + esc(c.g[0]) + '</span><span class="hint">What does it mean?</span>';
  }
  function cardBack(c) {
    if (c.kind === 'wine') {
      var w = c.w, pr = [];
      if (w.glass) pr.push(w.glassMl + 'ml ' + gbp(w.glass));
      if (w.carafe) pr.push('carafe ' + gbp(w.carafe));
      pr.push(bottleLabel(w).toLowerCase() + ' ' + gbp(w.bottle));
      return '<span class="eyebrow">' + esc(w.short) + '</span>' +
        '<span class="row"><b>Grape</b>' + esc(w.grape) + '</span>' +
        (w.style.profile ? '<span class="row"><b>Style</b>' + esc(w.style.profile) + '</span>' : '') +
        '<span class="row"><b>Served</b>' + esc(howServed(w)) + ' · ' + esc(pr.join(' · ')) + '</span>' +
        '<span class="row sellrow"><b>Sell it</b><p>' + esc(w.sell) + '</p></span>' +
        (w.flag ? '<span class="row"><b>Good to know</b>' + esc(w.flag) + '</span>' : '');
    }
    if (c.kind === 'steer') {
      var s = c.s;
      return '<span class="eyebrow">' + esc(s.q) + '</span>' +
        '<span class="row"><b>By the glass</b>' + (s.glass.length ? esc(s.glass.map(function (id) { return byId[id].short + ' ' + gbp(byId[id].glass); }).join(' · ')) : 'Nothing by the glass') + '</span>' +
        (s.bottle.length ? '<span class="row"><b>Bottle only</b>' + esc(s.bottle.map(function (id) { return byId[id].short + ' ' + gbp(byId[id].bottle); }).join(' · ')) + '</span>' : '') +
        (s.tip ? '<span class="row sellrow"><b>Tip</b><p>' + esc(s.tip) + '</p></span>' : '');
    }
    if (c.kind === 'grape') return '<span class="eyebrow">' + esc(c.g[0]) + '</span><span class="row"><b>Tastes like</b>' + esc(c.g[1]) + '</span><span class="row"><b>On our list</b>' + esc(c.g[2]) + '</span>';
    return '<span class="eyebrow">' + esc(c.g[0]) + '</span><span class="row">' + esc(c.g[1]) + '</span>';
  }

  /* ---------- install & offline ---------- */
  var installEvt = null;
  window.addEventListener('beforeinstallprompt', function (e) { e.preventDefault(); installEvt = e; });
  if ('serviceWorker' in navigator && location.protocol !== 'file:') {
    navigator.serviceWorker.register('sw.js').then(function (reg) {
      function offer(sw) { toast('The wine list has been updated.', 'Reload', function () { sw.postMessage('skipWaiting'); }); }
      if (reg.waiting && navigator.serviceWorker.controller) offer(reg.waiting);
      reg.addEventListener('updatefound', function () {
        var sw = reg.installing;
        sw.addEventListener('statechange', function () { if (sw.state === 'installed' && navigator.serviceWorker.controller) offer(sw); });
      });
    }).catch(function () { /* offline use just won't be available */ });
    var reloading = false;
    navigator.serviceWorker.addEventListener('controllerchange', function () { if (!reloading) { reloading = true; location.reload(); } });
  }

  route();
})();
