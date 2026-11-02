#!/usr/bin/env python3
"""Turn the researchers' JSON (one file per group) into tools/content_bible.json for the app.

Staff-facing text is cleaned: source citations in brackets, and sentences that only say what could
not be found, are taken out (they stay in the research files and in the report for Simon).
Per-wine overrides in OVERRIDES replace any field after cleaning.

  python3 tools/curate_research.py <research-dir>
"""
import json, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

# words that mark a bracket as a citation rather than content
CITE = re.compile(r"\s*\((?:[^()]*?(?:Wine Anorak|Lea & Sandeman|L&S|Kermit Lynch|World of Fine Wine|Stelzer|Suckling|Wine Advocate|Vinous|"
                  r"Justerini|technical sheet|tech sheet|Frederick Wildman|Gault|York Wines|SommSelect|Les Caves|Hedonism|Fine \+ Rare|House of Malt|"
                  r"Enotria|Burghound|Caviste|Liberty|Wine Society|Decanter|Dunnuck|Skurnik|Tanners|Vinmonopolet|Systembolaget|Primal Wine|Berry Bros|"
                  r"Millésime|winedering|Winedering|IWC|M\. Touton|WineAlign|Callmewine|Cambridge Wine|Flaschenpost|Partridges|iDealwine|Vino Fino|"
                  r"Grand Cru Wijnen|Alliance|Lebendige|Superiore|Businessonline|Wine Spectator|Wine Access|Hay Wines|Singular|Reserve Wines|NP Wines|"
                  r"Godel|Godello|Vente à la|Lay & Wheeler|Fareham|Gerrard Seel|Grape to Glass|LCBO|Vinoscout|Garrafeira|Falstaff|TWCI|Wine Cellar Insider|"
                  r"Wikipedia|Kissack|Fréchette|importer|merchant|retailer|producer page|producer sheet|estate sheet|Vila Viniteca|Vintus|Wine Republic|"
                  r"Bourgogne Aujourd|Burgundy Report|Uncorked|Vine Arts|Opimian|ADUV|Rue des Vignerons|Hachette|K&L|evino|Flint|Highbury|winewithseth|"
                  r"Gismondi|vino\.com|wine\.com|Bottle of Italy|ICE|Italy's Finest|gamberorosso|Canadian|US |UK |general|generic|appellation rule|"
                  r"DOC regulations|category|Atkin|Robinson|Jancis|Parker|Galloni|Kelley|Perrotti|Krebiehl|Martin|Larner|O'Keefe|Rason|Norris|Luczy|"
                  r"Speller|Czerwinski|Walls|Lyons|Atkins|Beckett|Goode|Herzog)[^()]*)\)", re.I)
UNSURE = re.compile(r"\b(not published|not found|not confirmed|unconfirmed|could not|couldn't|no source|not stated|not documented|"
                    r"sources disagree|sources conflict|conflicts? with|not given|not described|not mentioned|no figure|is not known|unknown|"
                    r"not checked|no producer|no tech|no technical)\b", re.I)


def clean(t):
    if not t:
        return ''
    t = CITE.sub('', str(t))
    t = re.sub(r'\s+([,.;:])', r'\1', t)
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z‘“"\'])', t.strip())
    keep = [p for p in parts if not UNSURE.search(p)]
    out = ' '.join(keep).strip()
    out = re.sub(r'\s{2,}', ' ', out).replace(' ,', ',')
    return out


def curate(research_dir):
    from content_overrides import OVERRIDES
    bible, report = {}, []
    for f in sorted(glob.glob(os.path.join(research_dir, '*_out.json'))):
        for r in json.load(open(f)):
            wid = r['id']
            st = r.get('style') or {}
            food = [re.sub(r'\s*\([^)]*\)', '', clean(x)).strip() for x in (r.get('food') or [])]
            b = dict(
                food=[x for x in food if x][:4],
                abv=(re.match(r'\s*(\d+(?:\.\d+)?%)', str(r.get('abv') or '')) or [None, None])[1] or '',
                style={k: st.get(k) for k in ('profile', 'body', 'sweetness', 'acidity', 'tannin', 'oak') if st.get(k)},
                sources=[u for u in (r.get('sources') or []) if str(u).startswith('http')])
            o = OVERRIDES.get(wid, {})
            for k, v in o.items():
                if k == 'style':
                    b['style'].update(v)
                else:
                    b[k] = v
            bible[wid] = {k: v for k, v in b.items() if v not in ('', None, [], {})}
            report.append(dict(id=wid, confidence=r.get('confidence'), thin=r.get('thin', ''), corrections=r.get('corrections', [])))
    json.dump(bible, open(os.path.join(ROOT, 'tools', 'content_bible.json'), 'w'), ensure_ascii=False, indent=1)
    json.dump(report, open(os.path.join(research_dir, 'report.json'), 'w'), ensure_ascii=False, indent=1)
    print(f'curated {len(bible)} wines -> tools/content_bible.json')


if __name__ == '__main__':
    curate(sys.argv[1])
