# Staff notes for every wine, keyed by Cellar Book id (w001-w075), written from the October 2026 research.
# The four files below hold the text; this file only merges them.
# Prices are never typed: {g:id} = glass price, {b:id} = bottle price, {vint:id} = vintage, {age:id} = age in years.
from wines_sparkling import W as _S
from wines_white import W as _W
from wines_red import W as _R
from wines_rose_sweet import W as _RS

W = {}
for part in (_S, _W, _R, _RS):
    for k in part:
        assert k not in W, k
    W.update(part)
