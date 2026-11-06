#!/usr/bin/env python3
"""Build js/data.js for the Bar Finch staff app.

Two steps:
  1. snapshot  - read a Cellar Book export (wines/*.json, config/*.json) plus the prices the
                 Cellar Book pricing engine produced, and write data/cellar-book-snapshot.json.
                 Trade costs and suppliers are dropped here, so they never reach the public app.
  2. build     - merge the snapshot with the staff notes (content_wines.py, content_guide.py),
                 fill in every {g:id} / {b:id} price token, run the consistency checks and
                 write js/data.js.

  python3 tools/build_data.py snapshot <cellar-book-export-dir> <prices.json>
  python3 tools/build_data.py build
"""
import json, os, re, sys, datetime, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
SNAP = os.path.join(ROOT, 'data', 'cellar-book-snapshot.json')

SECTION_ORDER = ['sparkling', 'white', 'rose', 'red', 'sweet']
SECTION_LABEL = {'sparkling': 'Champagne & Sparkling', 'white': 'White', 'rose': 'Rosé', 'red': 'Red',
                 'sweet': 'Dessert & Fortified'}
PROFILES = [  # style profiles: (name, group, one line for staff)
    ('Fresh & citrus fizz', 'sparkling', 'Zesty, lemon and green apple, lighter on its feet.'),
    ('Rich & toasty fizz', 'sparkling', 'Brioche, toast and nuts; rounder and fuller.'),
    ('Rosé fizz', 'sparkling', 'Pink sparkling: red berries and citrus.'),
    ('Crisp & mineral white', 'white', 'High acidity, little or no oak, citrus and a salty or stony finish.'),
    ('Aromatic white', 'white', 'Perfumed: flowers, peach, apricot, elderflower.'),
    ('Textured & savoury white', 'white', 'The feel matters as much as the fruit: waxy, grippy, nutty, sometimes funky.'),
    ('Rich & oaked white', 'white', 'Full-bodied, often barrel-aged: stone fruit, honey, toast, cream.'),
    ('Pale & dry rosé', 'rose', 'Provence style: very pale, crisp, delicate.'),
    ('Fuller rosé', 'rose', 'More colour, fruit and body; a rosé for food.'),
    ('Light & fresh red', 'red', 'Soft tannin, bright acidity, red fruit; several take a chill.'),
    ('Medium & savoury red', 'red', 'Structure plus herbs, earth, leather and spice beyond the fruit.'),
    ('Rich & powerful red', 'red', 'Full body, dark ripe fruit, firm tannin, often high alcohol.'),
    ('Sweet wine', 'sweet', 'Made sweet by noble rot or dried grapes: honey, apricot, dried fruit.'),
    ('Fortified wine', 'sweet', 'Grape spirit added to keep it sweet and strong: Port and Maury.'),
]
PROFILE_KEYS = [p[0] for p in PROFILES]
SHELF_NAME = {'T': 'top shelf', 'R1': 'row 1', 'R2': 'row 2', 'R3': 'row 3', 'R4': 'row 4',
              'L': 'lower shelf', 'B': 'bottom shelf'}


def load(p):
    d = json.load(open(p))
    return d.get('data', d) if isinstance(d, dict) else d


# ---------------------------------------------------------------- snapshot
def snapshot(export_dir, prices_path):
    prices = json.load(open(prices_path))
    wines = []
    for f in sorted(os.listdir(os.path.join(export_dir, 'wines'))):
        w = load(os.path.join(export_dir, 'wines', f))
        if w.get('status') != 'list':
            continue
        p = prices[w['id']]
        m = w.get('menu') or {}
        wines.append(dict(
            id=w['id'], section=w['section'], style=w.get('style') or '', vintage=str(w.get('vintage') or ''),
            ml=w.get('ml') or 750, pour=w.get('btg') or '',
            producer=m.get('producer') or '', cuvee=m.get('cuvee') or '', appellation=m.get('appellation') or '',
            region=m.get('region') or '', menuNote=m.get('note') or '',
            bottle=p['bottle'], glass=p.get('glass'), g175=p.get('g175'), carafe=p.get('carafe')))
    shelves = load(os.path.join(export_dir, 'config', 'shelves.json'))
    menu = load(os.path.join(export_dir, 'config', 'menu.json'))
    out = dict(source='Bar Finch Cellar Book', takenAt=datetime.date.today().isoformat(),
               shelvesAt=shelves.get('at'), regionOrder=menu.get('regionOrder', []),
               shelves=dict(bays=shelves['bays'], names=shelves.get('names', {}), zones=shelves.get('zones', {})),
               wines=wines)
    os.makedirs(os.path.dirname(SNAP), exist_ok=True)
    json.dump(out, open(SNAP, 'w'), ensure_ascii=False, indent=1)
    print(f'snapshot: {len(wines)} wines on the list -> {SNAP}')


# ---------------------------------------------------------------- build
def shelf_spots(shelves):
    """wine id -> 'Bay 2 · top shelf, lanes 3–4 · 8 bottles' (one string per place it sits)."""
    spots = {}
    for bay, shelfs in shelves['bays'].items():
        for key in ['T', 'R1', 'R2', 'R3', 'R4', 'L', 'B']:
            lane = 1
            for lanes, ids in shelfs.get(key, []):
                if lanes == 0:   # a middle row of 8, split between its wines
                    n = len(ids)
                    for i, wid in enumerate(ids):
                        half = '' if n == 1 else (' (left half)' if i == 0 else ' (right half)')
                        spots.setdefault(wid, []).append(f'Bay {bay} · {SHELF_NAME[key]}{half} · {8 // n} bottles')
                else:
                    for wid in ids:
                        ln = f'lane {lane}' if lanes == 1 else f'lanes {lane}–{lane + lanes - 1}'
                        spots.setdefault(wid, []).append(f'Bay {bay} · {SHELF_NAME[key]}, {ln} · {lanes * 4} bottles')
                    lane += lanes
    return spots


def build():
    from content_wines import W
    from content_guide import STEER, RULES, SERVICE, SANCERRE, GRAPES_W, GRAPES_R, GLOSS
    from content_training import COURSES
    bible_path = os.path.join(ROOT, 'tools', 'content_bible.json')
    BIBLE = json.load(open(bible_path)) if os.path.exists(bible_path) else {}
    snap = json.load(open(SNAP))
    year = datetime.date.today().year
    P = {w['id']: w for w in snap['wines']}
    problems = []

    def need(cond, msg):
        if not cond:
            problems.append(msg)

    need(set(P) == set(W), f'notes and list differ: no notes for {sorted(set(P) - set(W))}, notes for wines not on the list {sorted(set(W) - set(P))}')
    if problems:
        sys.exit('\n'.join(problems))

    def btg(wid):
        return P[wid]['pour'] in ('Y', 'COR', 'GLASS')

    def fill(t, where):
        def rep(m):
            kind, wid = m.group(1), m.group(2)
            w = P.get(wid)
            if not w:
                problems.append(f'{where}: unknown wine {wid}')
                return '?'
            if kind == 'g':
                need(w['glass'], f'{where}: {wid} has no glass price')
                return f"£{w['glass']}"
            if kind == 'b':
                return f"£{w['bottle']}"
            if kind == 'vint':
                return w['vintage']
            if kind == 'age':
                need(w['vintage'].isdigit(), f'{where}: {wid} has no vintage year')
                return str(year - int(w['vintage']))
        return re.sub(r'\{(g|b|vint|age):(w\d{3})\}', rep, t)

    spots = shelf_spots(snap['shelves'])
    wines = []
    for wid, w in P.items():
        n = W[wid]
        name = n.get('name') or (w['producer'] + (f", {w['cuvee']}" if w['cuvee'] else ''))
        size = {375: 'Half bottle (37.5cl)', 500: '50cl bottle'}.get(w['ml'], '')
        sell, note, flag = (fill(n.get(k, ''), f'{wid}.{k}') for k in ('sell', 'note', 'flag'))
        txt = (sell + ' ' + flag).lower()
        # the words staff read must match how the wine is actually poured
        if 'coravin' in txt:
            need(w['pour'] == 'COR', f'{wid} text mentions the Coravin but it is poured "{w["pour"] or "bottle only"}"')
        if 'by the glass' in txt:
            need(btg(wid), f'{wid} text says "by the glass" but it is bottle only')
        loc = spots.get(wid) or (['Bay 1 · sparkling and sweet, arranged by Simon'] if w['section'] in ('sparkling', 'sweet') else [])
        wines.append(dict(
            id=wid, section=w['section'], region=w['region'] or 'Other', name=name, short=n['short'],
            appellation=w['appellation'] or w['style'], vintage=w['vintage'], size=size, ml=w['ml'],
            pour=('COR' if w['pour'] == 'COR' else ('Y' if btg(wid) else '')),
            glassMl=75 if w['section'] == 'sweet' else 125,
            glass=w['glass'] if btg(wid) else None, g175=w['g175'] if btg(wid) else None,
            carafe=w['carafe'] if w['pour'] == 'Y' else None, bottle=w['bottle'],
            menuNote=w['menuNote'], grape=n['grape'], g=n['g'], note=note, sell=sell, flag=flag, shelf=loc,
            menuName=(w['producer'] + (' ' + w['cuvee'] if w['cuvee'] else '')).strip()))
        b = BIBLE.get(wid, {})
        for k in ('story', 'site', 'making', 'taste', 'serve', 'fact'):   # hand-written, from the research
            if n.get(k):
                wines[-1][k] = fill(n[k], f'{wid}.{k}')
        for k in ('abv', 'vintageNote'):                                     # straight from the research
            if b.get(k):
                wines[-1][k] = b[k]
        need(n.get('taste'), f'{wid}: no tasting note')
        wines[-1]['food'] = b.get('food', [])
        wines[-1]['sources'] = b.get('sources', [])
        wines[-1]['style'] = b.get('style', {})
        st = wines[-1]['style']
        if BIBLE:
            need(st.get('profile') in PROFILE_KEYS, f'{wid}: style profile "{st.get("profile")}" is not one of the known profiles')

    # menu order: section, then region (menu order), then bottle price per 75cl
    ro = {r: i for i, r in enumerate(snap['regionOrder'])}
    wines.sort(key=lambda x: (SECTION_ORDER.index(x['section']), ro.get(x['region'], 99), x['bottle'] * 750 / x['ml']))

    # ---- facts the written guidance relies on
    still = [x for x in wines if x['glass'] and x['section'] in ('white', 'red', 'rose')]
    spk = [x for x in wines if x['glass'] and x['section'] == 'sparkling']
    need(P['w055']['glass'] == min(x['glass'] for x in spk), 'Franciacorta is no longer the cheapest glass of fizz')
    need(P['w061']['glass'] > P['w076']['glass'], 'Pol Roger is no longer a step up from the house Devaux by the glass')
    need(P['w051']['glass'] == min(x['glass'] for x in still), 'Ollières is no longer the entry glass')
    need(P['w012']['glass'] == P['w034']['glass'], 'house white and house red are no longer the same glass price')
    need(btg('w013'), 'the Pabiot is no longer by the glass: rewrite the Sancerre guidance')
    need(not btg('w020'), 'the Riffault Sancerre is now by the glass: rewrite the Sancerre guidance')

    steer = []
    for q, gl, bo, tip in STEER:
        for x in gl:
            need(x in P and btg(x), f'steering "{q}": {x} is listed under by the glass but is bottle only')
        for x in bo:
            need(x in P and not btg(x), f'steering "{q}": {x} is listed under by the bottle but is poured by the glass')
        steer.append(dict(q=q, glass=gl, bottle=bo, tip=fill(tip, 'steer')))

    cor = [x['short'] for x in wines if x['pour'] == 'COR']
    rules = [dict(t=t, b=fill(b.replace('{coravin}', ', '.join(cor)), 'rules')) for t, b in RULES]
    sanc = dict(intro=SANCERRE['intro'], sections=[dict(h=h, parts=[dict(k=k, t=fill(t, 'sancerre')) for k, t in parts])
                                                  for h, parts in SANCERRE['sections']])

    # ---- training courses: resolve {w:id}, check every wine they name is on the list
    def wlink(t, where, plain=False):
        def rep(m):
            wid = m.group(1)
            if wid not in P:
                problems.append(f'{where}: names {wid}, which is not on the list')
                return '?'
            nm = W[wid]['short']
            return nm if plain else f'<a class="wl" href="#info-wine-{wid}">{html.escape(nm)}</a>'
        return re.sub(r'\{w:(w\d{3})\}', rep, t)
    courses = []
    for c in COURSES:
        lessons = []
        for l in c['lessons']:
            where = f"course {c['id']}/{l['id']}"
            for x in l.get('wines', []):
                need(x in P, f'{where}: lists {x}, which is not on the list')
            for pf in l.get('profiles', []):
                need(pf in PROFILE_KEYS, f'{where}: unknown profile {pf}')
                if BIBLE:
                    need(any(BIBLE.get(x, {}).get('style', {}).get('profile') == pf for x in P), f'{where}: no wine on the list has the profile {pf}')
            quiz = []
            for q, opts, a, why in l['quiz']:
                o = [wlink(x, where, True) for x in opts]
                need(len(set(o)) == len(o), f'{where}: duplicate options in "{q}"')
                quiz.append(dict(q=wlink(q, where, True), o=o, a=o[a], why=wlink(why, where, True)))
            lessons.append(dict(id=l['id'], title=l['title'], wines=l.get('wines', []), profiles=l.get('profiles', []),
                                cards=[dict(h=h, b=fill(wlink(b, where), where)) for h, b in l['cards']], quiz=quiz))
        courses.append(dict(id=c['id'], title=c['title'], blurb=c['blurb'], lessons=lessons))

    if problems:
        sys.exit('NOT BUILT, fix these first:\n- ' + '\n- '.join(problems))

    data = dict(
        builtAt=datetime.date.today().isoformat(), takenAt=snap['takenAt'],
        sections=[dict(key=k, label=SECTION_LABEL[k]) for k in SECTION_ORDER],
        wines=wines, steer=steer, rules=rules, service=SERVICE, sancerre=sanc,
        grapes=dict(white=GRAPES_W, red=GRAPES_R), gloss=GLOSS, courses=courses,
        profiles=[dict(key=k, group=g, blurb=b) for k, g, b in PROFILES])
    js = '/* Generated by tools/build_data.py from the Bar Finch Cellar Book. Do not edit by hand. */\n'
    js += 'window.FINCH = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n'
    open(os.path.join(ROOT, 'js', 'data.js'), 'w').write(js)
    # new cache version for the service worker, so installed phones pick up the change
    import hashlib
    h = hashlib.sha1()
    for f in ('index.html', 'css/app.css', 'js/app.js', 'js/data.js', 'manifest.webmanifest'):
        h.update(open(os.path.join(ROOT, f), 'rb').read())
    swp = os.path.join(ROOT, 'sw.js')
    sw = re.sub(r"var VERSION = '[^']*';", f"var VERSION = 'finch-{data['builtAt']}-{h.hexdigest()[:8]}';", open(swp).read())
    open(swp, 'w').write(sw)
    n_btg = sum(1 for x in wines if x['glass'])
    print(f'built js/data.js: {len(wines)} wines, {n_btg} by the glass, {len(cor)} on the Coravin, '
          f'{len(steer)} steering rows')


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1] == 'snapshot':
        snapshot(sys.argv[2], sys.argv[3])
    elif len(sys.argv) >= 2 and sys.argv[1] == 'build':
        build()
    else:
        print(__doc__)
