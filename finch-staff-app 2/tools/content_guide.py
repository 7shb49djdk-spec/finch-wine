# Guide content for the staff app: steering, how the list works, service, Sancerre, grapes, glossary.
# Wines are referred to by Cellar Book id; {g:id} / {b:id} become live glass / bottle prices at build time.

# ---------- When a guest says… ----------
# (what the guest says, glass picks, bottle-only picks, tip)
STEER = [
    ("“A Sancerre” or “a Sauvignon Blanc”", ["w013"], ["w002", "w020"],
     "Lead with the Pabiot: Sancerre's neighbour, by the glass. See “When a guest asks for Sancerre”."),
    ("“Pinot Grigio” or “light and crisp”", ["w001", "w012"], ["w003", "w008", "w011"],
     "We have no Pinot Grigio. Muscadet is the lightest and the cheapest; Finch Bianco is the house white."),
    ("“Chablis” or “unoaked Chardonnay”", ["w007"], ["w016"],
     "Chablis sells itself. The Premier Cru Beauroy is the step up."),
    ("“White Burgundy”", ["w025", "w007"], ["w015", "w018", "w021", "w022"],
     "Vinya del Coll: a different grape, a similar profile, a little softer and rounder."),
    ("“A rich, full-bodied white”", ["w010", "w017"], ["w019", "w023", "w024"],
     "Cervaro is the famous name. Châteauneuf Blanc is very intense, best with food."),
    ("“Aromatic”, “fruity” or “not too dry”", ["w006"], ["w004", "w005", "w019"],
     "The Riesling is old-school, with a touch of sweetness. Offer a taste of the AWM first. For properly sweet, see the dessert wines."),
    ("“Something different” or “natural wine”", ["w006", "w052"], ["w033", "w009", "w014", "w018", "w062"],
     "AWM and Areore are funky. Offer a taste of the AWM first."),
    ("“Prosecco”", ["w055", "w056"], [],
     "Franciacorta: made like Champagne, finer and drier. Vouvray for more fruit."),
    ("“Champagne”", ["w058", "w061", "w060"], ["w062"],
     "Start with the house Billecart. Pol Roger is rounder; Bonnet-Gilmert is grower Champagne. The Taillet, all Meunier, is by the bottle."),
    ("“Something to celebrate”", ["w060"], ["w063", "w064", "w065", "w066", "w067"],
     "Churchill is cheaper here than on any other Mayfair list we checked."),
    ("“Something English”", [], ["w005", "w057", "w059"],
     "Nothing English by the glass."),
    ("“A pale, dry rosé”", ["w051"], ["w054"],
     "Ott is the name people know."),
    ("“A rosé with more flavour”", ["w052"], ["w053"],
     "Tavel drinks like a light red. Karambolage is natural: offer a taste."),
    ("“Pinot Noir”, “a light red” or “red with fish”", ["w031", "w036", "w026"], ["w028", "w044", "w048", "w049"],
     "Etna Rosso and Morgon are the adventurous alternatives to Burgundy. Novaia and Juliénas take a chill."),
    ("“Big and bold” (Malbec, Shiraz)", ["w032", "w042"], ["w029", "w027", "w041", "w039", "w046", "w047"],
     "Turley and Amarone are the ripest. Côte-Rôtie is the most savoury."),
    ("“Bordeaux”, “claret” or “Merlot”", ["w032", "w050"], ["w035", "w037", "w040"],
     "Pavillon Rouge by the glass is a First Growth experience."),
    ("“Rioja” or “Tempranillo”", ["w038"], ["w029"],
     "The Rioja is {age:w038} years old: soft, mellow and traditional."),
    ("“Italian red”, “Chianti” or “Barolo”", ["w034", "w042"], ["w030", "w043", "w045", "w039"],
     "Finch Rosso, Rosso, Brunello: Sangiovese. Barolo, Barbaresco: Nebbiolo."),
    ("“Something sweet” or “a dessert wine”", ["w071", "w075"], ["w073", "w072"],
     "Sauternes is the classic. Pierre Bise is fresher; Climens is the grand one."),
    ("“Port”, or “with cheese” or “chocolate”", ["w070", "w069", "w074"], ["w068"],
     "LBV with cheese, Mas Amiel with chocolate. White Port, chilled, also works as an aperitif."),
]

# ---------- How the list works ----------
# Cards; {coravin} becomes the live list of Coravin wines, {house_glass} the house glass price.
RULES = [
    ("Measures", "Glasses are 125ml; a 175ml pour is available on request. Dessert and fortified wines are poured in 75ml. A carafe is 500ml, two-thirds of a bottle. Glass and carafe prices are in proportion to the bottle, so a bottle carries no discount and a carafe never costs more than four small glasses."),
    ("◆ Coravin wines: no carafe", "{coravin}. These are drawn through the cork with the Coravin, so the bottle is never opened and they are never offered as a carafe. Never pull the cork on these for a glass."),
    ("Sparkling and dessert: glass or bottle", "No carafes of sparkling wine, because it goes flat before it is finished, and none of dessert wine. None of the Champagnes is on the Coravin."),
    ("House wines and chilled red", "Our house wines are Finch Bianco and Finch Rosso, both {g:w012} a glass. Finch Bianco is Tenuta di Montefoscoli's Vermentino ('Fontemaggiore') and Finch Rosso their Sangiovese ('Santandrea'), from an organic family estate in the hills near Pisa. The Novaia Valpolicella is served chilled and listed that way on the menu; the Juliénas also works with a light chill."),
    ("A glass of Sancerre", "We don't pour Sancerre by the glass. We pour the Pabiot Pouilly-Fumé instead ({g:w013}): the same grape on the same soils, just across the river. The Riffault Sancerre ({b:w020}) is bottle only. See “When a guest asks for Sancerre”."),
    ("Natural wines: offer a taste", "The two Austrian Wine Mafia wines (Dolce und die Japaner and Karambolage) are natural and funky. Offer a taste before pouring a glass. They are unfiltered, so a little haze or a slight spritz on opening is normal, not a fault. The Scarbolo Areore has some funk too."),
    ("Know the characters", "The Rolly Gassmann is an old-school Riesling, not the modern dry style. The Châteauneuf Blanc is very intense, so steer it towards food. The Saperavi is very tannic. The Rioja is {age:w038} years old and delicate."),
    ("Check the bottle", "Vintages change as bins run out. Read the label before describing a wine's age, and point out the vintage when you present the bottle."),
]

# ---------- Wine service at Finch ----------
SERVICE = dict(
    intro="The sommelier looks after wine service. This is so the whole floor team knows what is being done and why, and can support it.",
    somm="The sommelier is part of the floor team. They are on the floor to support the whole service: clearing tables when they can, and keeping an eye on wine and water so the rest of the team can focus on everything else. But the sommelier is only one person and can't see every table at once, so they will always be grateful to be told about anything drink-related, anywhere in the room.",
    principles=[
        ("No empty glasses, water or wine.", "A guest should never sit in front of an empty glass."),
        ("We pour, the guest doesn't.", "The bottle is kept out of the guests' reach as far as possible. Sometimes it has to go on the table, but either way we keep the glasses topped up throughout the meal."),
        ("Glass guests get the same care.", "As a glass runs low, offer a top-up, so it feels as if they also have a bottle somewhere."),
        ("Short time at the table.", "As a rule, bottles are presented at the table and opened away from it. It's a small room, and standing at a table for long makes it hard for everyone else to move. Many of our bottles also have wax tops, which crumble when opened and need cleaning up. But it is a judgement call: depending on the bottle and on what is happening in the room, opening at the table is sometimes the better choice."),
    ],
    bottle=[
        ("Present.", "Show the bottle to the host at the table: producer, wine and vintage."),
        ("Open, usually away from the table.", "Most bottles go back to the station to be opened. Some are opened at the table, depending on the bottle and how busy the room is."),
        ("Clean wax tops.", "Many of our bottles are sealed with wax. Once opened, clean the wax from the rim before pouring, and clear away any crumbs."),
        ("Taste and pour.", "Pour a taste for the host, then pour for the table."),
        ("Bottle away.", "Place the bottle out of the guests' reach, as far as the space allows."),
        ("Keep topping up", "throughout the meal. When the bottle is nearly finished, ask whether the table would like another."),
    ],
    glass=[
        ("", "Pour the glass and bring it to the guest."),
        ("", "As the glass runs low, offer a top-up of the same wine, or suggest the next one."),
    ],
    floor=[
        "Tell the sommelier about anything drink-related you notice, anywhere in the room: a low or empty glass, a guest looking for the list, a table ready for another bottle.",
        "Keep an eye on every glass as you pass, and top up water yourself.",
        "Keep walkways clear around the station while bottles are being opened.",
        "If a guest reaches for a bottle or asks for more wine, let the sommelier know straight away.",
    ],
)

# ---------- When a guest asks for Sancerre ----------
SANCERRE = dict(
    intro="We don't pour Sancerre by the glass. What we pour instead is the Pabiot Pouilly-Fumé, and the aim is to present it as the insider's choice, never as the cheaper one. The guest should feel let in on something, not steered down.",
    sections=[
        ("Lead with what we pour, not with what we don't", [
            ("p", "“We don't have Sancerre by the glass” starts the conversation with a no. Start with the Pabiot instead:"),
            ("q", "“Our Loire Sauvignon by the glass is a Pouilly-Fumé. It's the same grape, grown on the same soils, just across the river from Sancerre, and it's the top wine from a brilliant young biodynamic grower. Can I bring you a taste?”"),
            ("p", "If the room is busy:"),
            ("q", "“By the glass we pour Sancerre's neighbour across the river, a Pouilly-Fumé from Pabiot. Would you like to try it?”"),
        ]),
        ("If they ask why not Sancerre", [
            ("q", "“We picked this one because it's the better glass. It's Pabiot's flagship wine, so there's more depth and texture than most Sancerre you'll find by the glass. There's a lovely smoky, flinty edge too; that's the ‘Fumé’.”"),
        ]),
        ("If they still want Sancerre", [
            ("q", "“Of course. We have Claude Riffault's single-vineyard Sancerre by the bottle.”"),
            ("p", "Then present it with the same warmth."),
        ]),
        ("Other lines that work", [
            ("li", "“Do you know Pouilly-Fumé? It's the same grape, from just across the river from Sancerre. It's what I'd drink.”"),
            ("li", "“If you like Sancerre, you'll love this. Same Sauvignon, but from a biodynamic grower, with a smokier, more textured edge.”"),
        ]),
        ("What makes the case", [
            ("li", "<b>Same grape, same soils, the other bank.</b> Pouilly-Fumé is Sauvignon Blanc from the opposite bank of the Loire, on the same limestone, marl and flint. A guest asking for “a glass of Sancerre” usually means a crisp Loire Sauvignon, and that is exactly what they get."),
            ("li", "<b>The “Fumé”.</b> The name is usually linked to the smoky, flinty note that flint soils give, and Léon is grown partly on flint."),
            ("li", "<b>Pabiot is a serious grower, not a stand-in.</b> Biodynamic, very densely planted vines, wild-yeast fermentation, partly in concrete and amphora. More texture and length than most wines at its price."),
            ("li", "<b>The taste does the selling.</b> It is poured by the glass, so the guest can try it first. Once they have, most won't ask again."),
            ("li", "<b>If they are interested:</b> Pouilly-Fumé is a smaller appellation than Sancerre, so there is less of it about."),
        ]),
        ("Words to use, words to avoid", [
            ("p", "<b>Say</b> “instead”, “our Loire Sauvignon”, “Sancerre's neighbour”.<br><b>Never say</b> “we don't have”, “alternative”, “similar” or “cheaper”. They all make the Pabiot sound second best."),
        ]),
        ("What to avoid", [
            ("li", "Don't knock the Sancerre. The Riffault is a great single-vineyard wine and stays on the list for guests who want it."),
            ("li", "Don't give price as the reason. A guest who hears “it's cheaper” starts wondering what they're missing."),
            ("li", "Don't argue. If the guest insists, pour the Riffault with the same enthusiasm."),
        ]),
    ],
)

# ---------- Grapes ----------
GRAPES_W = [
    ("Chardonnay", "The great white grape. Unoaked it is crisp, green apple and chalk (Chablis); oaked it is richer, nutty and creamy (Côte de Beaune).",
     "Chablis, Chablis Beauroy, Saint-Romain, Chassagne, Corton-Charlemagne, Liquid Farm, Cervaro (with Grechetto), Areore (in the blend); Blanc de Blancs Champagne, Franciacorta"),
    ("Sauvignon Blanc", "Crisp and aromatic: citrus, green herbs, gooseberry. In the Loire it can be flinty or smoky.",
     "Pabiot Pouilly-Fumé, Riffault Sancerre, Toblino; in blends in both white Bordeaux, the Areore and the Sauternes"),
    ("Sémillon", "Waxy, lemony and round. It gives body to the Bordeaux blend, and takes noble rot well, which makes it the great sweet-wine grape of Bordeaux.",
     "Lamothe Bouscaut Blanc, Blanc de Lynch-Bages; sweet: Rabaud-Promis Sauternes, Climens Barsac (100%)"),
    ("Chenin Blanc", "The Loire's great grape: apple, quince, honey and high acidity. Made dry, sweet or sparkling.", "Savennières, Breton Vouvray; sweet: Pierre Bise Coteaux du Layon"),
    ("Riesling", "Aromatic, with high acidity: lime, peach, sometimes honey. Can be bone dry or off-dry.", "Rolly Gassmann (old-school, touch of sweetness)"),
    ("Melon de Bourgogne", "Light and neutral, salty and fresh; ageing on the lees adds texture.", "Muscadet"),
    ("Grüner Veltliner", "Austria's grape: green apple, citrus and a white-pepper note.", "AWM Dolce und die Japaner (with Müller-Thurgau); Karambolage rosé"),
    ("Albariño", "Galicia's grape: peach, citrus, blossom and a salty finish.", "Terras Gauda O Rosal (with Loureiro and Caíño)"),
    ("Garganega", "The Soave grape: almond, lemon and a soft, textured palate.", "Battistelle Soave"),
    ("Vermentino", "Coastal Italy: citrus, herbs and almond.", "Finch Bianco (house white, Montefoscoli Fontemaggiore)"),
    ("Carricante", "Etna's white grape: lemon, high acidity, very mineral.", "Caciorgna Etna Bianco"),
    ("Xarel·lo", "Catalonia's grape, the backbone of Cava: textured, herbal and saline.", "Vinya del Coll"),
    ("Viognier", "Perfumed and rich: apricot, peach and blossom, with gentle acidity.", "Condrieu"),
    ("Southern Rhône whites", "Grenache Blanc, Clairette, Roussanne and Bourboulenc: full-bodied, with orchard fruit and flowers.", "Châteauneuf-du-Pape Blanc"),
    ("Friulano", "Friuli's grape: pear, almond and a slightly bitter finish.", "Scarbolo Areore (with Sauvignon and Chardonnay)"),
    ("English aromatics", "Bacchus, Ortega and other cool-climate grapes: elderflower, hedgerow and citrus.", "Davenport Horsmonden"),
    ("Douro whites", "Rabigato, Viosinho, Gouveio, Códega do Larinho and Arinto: the white grapes of White Port. Nutty and honeyed with age.", "Niepoort White Port, Niepoort Colheita White Port"),
    ("Malvasia, Trebbiano, Grechetto", "Central Italy's white grapes. Dried for months, they make Vin Santo: dried apricot, fig and nuts.", "Caterina Dei Vin Santo"),
]
GRAPES_R = [
    ("Pinot Noir", "Light to medium body, low tannin: red cherry, raspberry, earth. Also one of the three Champagne grapes.",
     "Magnien, Volnay, Ambonnay Rouge; most Champagnes, both English sparkling wines, Franciacorta"),
    ("Pinot Meunier", "The fruity Champagne grape, usually hidden in blends.", "Taillet Blanc de Noirs (100%), Billecart, Pol Roger, Herbert Hall"),
    ("Gamay", "Beaujolais: juicy red fruit, low tannin, good lightly chilled.", "Juliénas, Morgon Côte du Py"),
    ("Merlot", "Soft and round: plum and dark cherry.", "Saint-Émilion, Pomerol, Pessac-Léognan, Margaux blends"),
    ("Cabernet Sauvignon", "Blackcurrant and cedar, with firm tannin. The backbone of the Médoc.", "Pavillon Rouge, Brio, Pessac-Léognan"),
    ("Cabernet Franc", "Fragrant and leafy: raspberry and violets.", "Pomerol, Saint-Émilion, Pessac-Léognan"),
    ("Syrah", "Dark fruit, pepper, black olive and smoked meat.", "Côte-Rôtie; in Rasteau, Châteauneuf and Tavel"),
    ("Grenache", "Ripe red fruit, spice and warmth. The southern Rhône's main grape.", "Rasteau, Châteauneuf-du-Pape, Tavel; Provence rosés; Mas Amiel Maury (sweet)"),
    ("Nebbiolo", "Pale in colour but powerful: roses, tar and cherry, with high tannin and acidity.", "Barolo, Barbaresco"),
    ("Sangiovese", "Tuscany's grape, and Chianti's: sour cherry, herbs and bright acidity.", "Finch Rosso (house red, Montefoscoli Santandrea), Rosso di Montalcino, Brunello"),
    ("Corvina", "Valpolicella's grape: fresh cherry, light. Dried before fermenting for Amarone.", "Novaia Valpolicella, Novaia Amarone"),
    ("Tempranillo", "Spain's grape: strawberry, plum, leather; takes well to long oak ageing.", "Urbina Rioja, Dehesa Gago (as Tinta de Toro)"),
    ("Nerello Mascalese", "Etna's red: pale, red-fruited and mineral. Often compared to Pinot Noir.", "Caciorgna N'Anticchia"),
    ("Saperavi", "Georgia's grape, red-fleshed: inky, dark, very tannic.", "The Qvevri Wine Cellar Saperavi"),
    ("Zinfandel", "California: ripe blackberry, spice, generous alcohol.", "Turley Old Vines"),
    ("Zweigelt", "Austria's red: cherry and a peppery edge.", "AWM Karambolage rosé"),
    ("Douro reds", "Touriga Nacional, Touriga Franca, Tinta Roriz (Tempranillo) and Tinta Barroca: the Port grapes. Dark fruit, floral, firm.", "Niepoort LBV Port"),
]

# ---------- Glossary ----------
GLOSS = [
    ("Appellation", "The legally defined place a wine comes from, and the rules for making it (Chablis, Rioja, Barolo)."),
    ("Grand Cru / Premier Cru (1er Cru)", "In Burgundy and Champagne, the top and second-tier classified vineyards or villages."),
    ("Blanc de Blancs / Blanc de Noirs", "White sparkling wine from white grapes only (Chardonnay) / from black grapes only (Pinot Noir or Meunier)."),
    ("Brut / Extra Brut", "Sweetness levels for sparkling wine. Brut is dry; Extra Brut has even less added sugar."),
    ("NV / Vintage", "Non-vintage blends several years for a consistent house style. Vintage is from one good year only."),
    ("Traditional method", "Second fermentation in the bottle that makes the bubbles, as in Champagne. Prosecco is made in a tank."),
    ("On the lees (sur lie)", "Wine left resting on its spent yeast, which adds texture and a bready or creamy note."),
    ("Grower Champagne", "Made by the family that grows the grapes, rather than a big house buying them in."),
    ("Second wine", "A château's second label, made from younger vines or lots not used in the main wine (Pavillon Rouge, Brio, Promesse)."),
    ("Cru Beaujolais", "The ten top villages of Beaujolais (Juliénas, Morgon…). Serious Gamay, nothing like Nouveau."),
    ("Super Tuscan", "Tuscan red made outside the traditional rules, often Sangiovese blended with Bordeaux grapes."),
    ("Appassimento", "Drying grapes for months before fermenting, as for Amarone. It gives rich, concentrated, high-alcohol wine."),
    ("Qvevri", "Large clay jars buried in the ground, used to make wine in Georgia for thousands of years."),
    ("Organic / Biodynamic", "No synthetic chemicals in the vineyard. Biodynamic adds a holistic calendar and natural preparations."),
    ("Natural wine", "Wild yeasts, little or no added sulphur, nothing added or taken away. Styles vary a lot."),
    ("Coravin", "A needle through the cork draws wine out under argon, so the bottle is never opened and keeps for weeks."),
    ("Noble rot", "A mould (botrytis) that shrivels ripe grapes in misty autumns, concentrating sugar and adding honey and apricot. Behind Sauternes, Barsac and Coteaux du Layon."),
    ("Fortified wine", "Wine with grape spirit added. Added during fermentation, it stops the yeast and keeps the wine sweet, as in Port and Maury."),
    ("Vin Doux Naturel", "The French name for a sweet wine fortified during fermentation, like the Mas Amiel Maury."),
    ("LBV (Late Bottled Vintage)", "Port from a single year, bottled after four to six years in wood. Ready to drink, unlike young Vintage Port."),
    ("Colheita", "Port from a single year, aged many years in cask before bottling. Portuguese for harvest."),
    ("Vin Santo", "Tuscany's 'holy wine': sweet wine from grapes dried for months, then aged for years in small barrels."),
    ("Tannin", "The drying, grippy feel in red wine, from skins and oak. Nebbiolo and Cabernet are high; Gamay and Pinot are low."),
]
