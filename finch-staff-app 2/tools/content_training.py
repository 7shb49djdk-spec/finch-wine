# Training courses for the staff app. Only what is relevant to the Bar Finch list.
# {w:w007} in a card becomes a link to that wine (its short name); in a quiz it becomes the plain name.
# A lesson can name its wines with `wines=[...]`, or take every wine of a style with `profile=...`
# (the profile comes from each wine's research notes, so the list keeps itself up to date).
# quiz entries: (question, [options], index of the right option, why)

COURSES = [
  dict(id='basics', title='Tasting basics', blurb='What you are tasting, where it comes from, and how to talk about it.', lessons=[
    dict(id='five', title='The five things you taste', cards=[
      ('Five things to notice', 'Almost every description of a wine comes down to five things: <b>sweetness</b>, <b>acidity</b>, <b>tannin</b>, <b>alcohol</b> and <b>body</b>. Then come the flavours: fruit, flowers, spice, earth, oak. Learn to notice the five first; they tell you what a wine is like to drink and what it goes with.'),
      ('Sweetness', 'Most of our list is <b>dry</b>: no sugar you can taste. A few wines have a touch of sweetness (<b>off-dry</b>), like the {w:w004}. The dessert and fortified wines are properly sweet. On sparkling labels, <b>Brut</b> means dry and <b>Extra Brut</b> drier still, like the {w:w062}.'),
      ('Acidity', 'Acidity is what makes your mouth water. It makes a wine taste fresh and is why wine works with food. High-acid wines on our list include the {w:w001}, the {w:w007}, the {w:w009} and every Champagne. Lower-acid, softer whites include the {w:w019}.'),
      ('Tannin', 'Tannin is the drying, grippy feeling on your gums and tongue, like strong black tea. It comes from grape skins, seeds and stems, and from oak, so it is mostly found in reds. Very tannic: the {w:w033}, the {w:w042} and the {w:w043}. Soft, low tannin: the {w:w028}, the {w:w026}, and the {w:w038}, whose tannins have softened with age.'),
      ('Alcohol and body', 'Body is the weight of the wine in your mouth: think skimmed milk against whole milk against cream. Alcohol adds weight and a warming feel. Light-bodied: the {w:w001} and the {w:w026}. Full-bodied: the {w:w039}, made from dried grapes, the {w:w041} and the {w:w017}.'),
    ], quiz=[
      ('What does tannin feel like?', ['A drying grip on the gums', 'A mouth-watering freshness', 'Sweetness on the tip of the tongue', 'A tingle of bubbles'], 0, 'Tannin dries the mouth, like strong tea. Acidity is the mouth-watering one.'),
      ('Which of these reds has the firmest tannin?', ['{w:w043}', '{w:w028}', '{w:w026}', '{w:w038}'], 0, 'A young Barbaresco Riserva, from Nebbiolo, is very tannic. Gamay and Corvina are soft, and the old Rioja has softened with age.'),
      ('What does “Brut” mean on a Champagne label?', ['Dry', 'Sweet', 'Vintage', 'Rosé'], 0, 'Brut is dry. Extra Brut has even less added sugar.'),
      ('Which white is known for its high acidity?', ['{w:w001}', '{w:w019}', '{w:w023}', '{w:w017}'], 0, 'Muscadet is light and very fresh. The others are rich, rounder whites.'),
      ('“Body” describes…', ['The weight of the wine in the mouth', 'The colour of the wine', 'How old the wine is', 'How sweet the wine is'], 0, 'Light, medium or full: like skimmed milk, whole milk or cream.'),
    ]),
    dict(id='where', title='Where flavour comes from', cards=[
      ('The grape', 'Each grape has its own range of flavours. Sauvignon Blanc tastes of citrus and green herbs, Viognier of apricot, Pinot Noir of red cherry, Syrah of black pepper and dark fruit. If a guest knows the grape they like, you can find it on our list in the Grapes course or the grape reference.'),
      ('The place: cool or warm', 'Cool places (Chablis, the Loire, Champagne, England) give wines with more acidity, lighter body and citrus or green-apple fruit. Warm places (the southern Rhône, California, Toro in Spain) give riper fruit, more alcohol and fuller body. Compare the {w:w007}, from cool northern Burgundy (lean, citrus, chalky), with the {w:w023}, from warmer Umbria and fermented in barrel (broader and riper).'),
      ('Oak', 'Barrels add vanilla, toast and spice and give a rounder texture; new oak gives more of this than old. The {w:w007} and the {w:w001} see no oak. The {w:w025} and the {w:w023} are fermented in barrel. Big old casks, like the ones used for the {w:w042}, add little flavour: they let the wine breathe and soften.'),
      ('Lees', 'Lees are the spent yeast left after fermentation. Leaving a wine on them adds texture and a bready, creamy note. Muscadet “sur lie” is aged this way ({w:w001}), and Champagne spends years on its lees in the bottle, which is where the brioche and biscuit flavours come from.'),
      ('Time', 'With age, fresh fruit turns to dried fruit, and notes of leather, tobacco and earth appear in reds: the {w:w038} (2004) and the {w:w050} (2008). Sweet and fortified whites turn nutty and honeyed: the {w:w072} and the {w:w074}.'),
    ], quiz=[
      ('A wine from a cool place usually has…', ['More acidity and lighter body', 'More alcohol and riper fruit', 'More tannin', 'More sweetness'], 0, 'Cool climates keep acidity high and alcohol lower.'),
      ('Which of these whites sees no oak at all?', ['{w:w007}', '{w:w025}', '{w:w023}', '{w:w010}'], 0, 'Village Chablis here is unoaked: that is the point of it.'),
      ('Where do the brioche and biscuit notes in Champagne come from?', ['Ageing on the lees', 'New oak barrels', 'Adding sugar', 'Very ripe grapes'], 0, 'Years on the spent yeast in the bottle give the bready, toasty notes.'),
      ('What happens to red wine as it ages?', ['Fresh fruit turns to dried fruit, leather and tobacco', 'It gets more tannic', 'It gets sweeter', 'It gets darker in colour'], 0, 'Tannins soften and fruit turns from fresh to dried. Colour actually fades towards brick.'),
    ]),
    dict(id='talk', title='Talking to guests about wine', cards=[
      ('Ask before you suggest', 'Three questions do most of the work. <b>What do you usually enjoy?</b> <b>Something lighter or something fuller?</b> <b>What are you eating?</b> Then offer one or two wines, not five.'),
      ('Words that work', 'Plain words describe wine best: <b>crisp</b>, <b>fresh</b>, <b>juicy</b>, <b>round</b>, <b>rich</b>, <b>smooth</b>, <b>savoury</b>, <b>dry</b>. Use the technical words (malolactic, appellation) only if the guest does.'),
      ('Hear what they mean', 'Guests use words loosely. “Dry” about a red often means “not too fruity” or “not too soft”. “Smooth” usually means low tannin. “Something light” can mean low alcohol or pale colour. Ask a follow-up question if you are not sure. The Guests tab in Info has the common requests and what to offer.'),
      ('Offer a taste', 'Anything by the glass can be tasted first. Always offer a taste of the natural wines, the {w:w006} and the {w:w052}: they are funky, and a taste avoids a surprise.'),
      ('If you are unsure', 'Tell the guest the sommelier will be right with them, and let them know. That is always better than guessing.'),
    ], quiz=[
      ('A guest asks for a “smooth” red. What do they most likely mean?', ['Soft, low tannin', 'Very sweet', 'Very old', 'Full of bubbles'], 0, 'Smooth usually means low tannin: the Juliénas or the Pinot Noir by the glass, not the Barolo.'),
      ('Which wines should you always offer a taste of first?', ['The two Austrian Wine Mafia natural wines', 'The Champagnes', 'The house wines', 'The dessert wines'], 0, 'The AWM Grüner and the Karambolage are natural and funky.'),
      ('How many wines should you usually suggest?', ['One or two', 'Five or six', 'Every wine in the style', 'None: let them read the list'], 0, 'One or two clear suggestions are easier for a guest than a long list.'),
      ('If you are not sure what to recommend, you should…', ['Bring in the sommelier', 'Pick the most expensive', 'Guess', 'Suggest the house wine every time'], 0, 'The sommelier is there to help; always better than guessing.'),
    ]),
  ]),

  dict(id='styles', title='Styles on our list', blurb='Every wine on the list grouped by what it tastes like, with what to say and what it goes with.', lessons=[
    dict(id='fizz', title='Champagne and sparkling', profiles=['Fresh & citrus fizz', 'Rich & toasty fizz', 'Rosé fizz'], cards=[
      ('How the bubbles get there', 'All our sparkling wines are made by the <b>traditional method</b>: a still wine is bottled with a little yeast and sugar, ferments again in the bottle, and the gas stays trapped as bubbles. This is how Champagne, Franciacorta, Vouvray Brut and English sparkling are made. Prosecco is different: its second fermentation happens in a big tank, which keeps it simpler and fruitier.'),
      ('Fresh and citrus', 'Lighter, zesty, lemon and green apple: the {w:w055}, the {w:w057}, the {w:w058}. A good start to the evening and with oysters or raw fish.'),
      ('Rich and toasty', 'More time on the lees or more Pinot Noir gives brioche, toast, nuts and a rounder feel: the {w:w061}, the vintage Pol Roger and the {w:w066}. Good with richer starters and as a celebration bottle.'),
      ('Words on the label', '<b>NV</b> (non-vintage) blends several years for a consistent house style. <b>Vintage</b> is one good year only. <b>Blanc de Blancs</b> is white grapes only, Chardonnay ({w:w060}). <b>Blanc de Noirs</b> is black grapes only ({w:w062}, all Meunier). <b>Grower</b> Champagne is made by the family that grows the grapes.'),
      ('No carafes, no Coravin', 'Sparkling is sold by the glass or the bottle only: it goes flat in a carafe. None of the Champagnes is on the Coravin.'),
    ], quiz=[
      ('How do the bubbles get into Champagne?', ['A second fermentation in the bottle', 'Gas is added before bottling', 'A second fermentation in a big tank', 'The grapes are picked early'], 0, 'That is the traditional method. Prosecco does its second fermentation in a tank.'),
      ('“Blanc de Blancs” means…', ['Made from white grapes only', 'Made from black grapes only', 'Made in one year only', 'Very dry'], 0, 'White grapes only, which in Champagne means Chardonnay.'),
      ('Which of our Champagnes is made only from Pinot Meunier?', ['{w:w062}', '{w:w058}', '{w:w060}', '{w:w067}'], 0, 'Taillet Exclusivi’T is a Blanc de Noirs from Meunier alone.'),
      ('Why is there no carafe of sparkling wine?', ['It would go flat', 'It is too expensive', 'The Coravin is used instead', 'It must be served in the bottle by law'], 0, 'A carafe lets the bubbles escape.'),
    ]),
    dict(id='crisp', title='Crisp and mineral whites', profiles=['Crisp & mineral white'], cards=[
      ('What they taste like', 'Light to medium body, high acidity, no or little oak. Citrus, green apple, pear, and often a salty or stony edge that people call “mineral”. They are refreshing and very good with food.'),
      ('What to say', '“Crisp and fresh, with a salty finish.” “Unoaked, lots of citrus.” These are the wines for a guest who asks for Pinot Grigio, Sauvignon Blanc or “something light and dry”.'),
      ('With food', 'Oysters and shellfish, raw and cured fish, salads, goat\'s cheese, anything with lemon. The {w:w001} with oysters is a classic.'),
    ], quiz=[
      ('A crisp and mineral white is usually…', ['High in acidity with little or no oak', 'Rich and buttery', 'Slightly sweet', 'Full-bodied and high in alcohol'], 0, 'Freshness first, oak rarely.'),
      ('A classic match for these wines is…', ['Oysters', 'Chocolate', 'Braised beef', 'Blue cheese'], 0, 'Shellfish and raw fish love high acidity.'),
    ]),
    dict(id='aromatic', title='Aromatic whites', profiles=['Aromatic white'], cards=[
      ('What they taste like', 'Very expressive on the nose: flowers, peach, apricot, elderflower, lime. Some are bone dry, some have a touch of sweetness. The grapes do the talking here, usually without much oak.'),
      ('What to say', '“Very perfumed and fruity.” For a guest who says they want something fruity or “not too dry”. The {w:w004} is old-school and rounder, with a touch of sweetness: say so before they order.'),
      ('With food', 'Spiced and aromatic dishes, Asian flavours, pork, mild curries, fresh cheeses.'),
    ], quiz=[
      ('Which word best describes an aromatic white?', ['Perfumed', 'Tannic', 'Toasty', 'Oaky'], 0, 'The aroma is the point: flowers and ripe fruit.'),
      ('What should you tell a guest about the Rolly Gassmann Riesling?', ['It is old-school, with a touch of sweetness', 'It is bone dry and very sharp', 'It is a sparkling wine', 'It is oaked like Burgundy'], 0, 'A guest expecting a modern dry Riesling would be surprised.'),
    ]),
    dict(id='textured', title='Textured and savoury whites', profiles=['Textured & savoury white'], cards=[
      ('What they taste like', 'Medium to full body with a feel in the mouth that matters as much as the fruit: waxy, grippy, nutty, sometimes a little funky. Some of these are natural wines or have spent time on their skins or lees.'),
      ('What to say', '“A white with real texture.” “Something a bit different.” For a guest who finds most whites thin, or who asks for natural wine. Warn about the funky ones before they order.'),
      ('With food', 'Roast chicken, pork, mushrooms, hard cheeses, richer fish dishes.'),
    ], quiz=[
      ('These whites are chosen as much for…', ['Their texture in the mouth', 'Their sweetness', 'Their bubbles', 'Their low price'], 0, 'Texture: waxy, grippy, nutty.'),
      ('What should you do before a guest orders one of the funky natural whites?', ['Mention the style and offer a taste', 'Decant it', 'Serve it very warm', 'Nothing'], 0, 'A taste avoids a surprise.'),
    ]),
    dict(id='rich', title='Rich and oaked whites', profiles=['Rich & oaked white'], cards=[
      ('What they taste like', 'Full body, often fermented or aged in oak barrels: ripe stone fruit, honey, toasted nuts, vanilla, a creamy texture. White Burgundy is the model; the Rhône and Bordeaux whites here are in this group too.'),
      ('What to say', '“Rich and round, with some oak.” For a guest who asks for white Burgundy, Chardonnay or “a full-bodied white”. The {w:w018} is the softer, rounder alternative for a white Burgundy drinker.'),
      ('With food', 'Lobster and crab, scallops, chicken with cream or butter sauces, veal, truffle.'),
    ], quiz=[
      ('Where do the vanilla and toast notes in a rich white usually come from?', ['Oak barrels', 'High acidity', 'Cold fermentation', 'Bubbles'], 0, 'Barrel fermentation and ageing.'),
      ('Which food suits a rich and oaked white best?', ['Lobster with butter', 'Oysters', 'Chocolate', 'A green salad'], 0, 'Rich food for a rich wine.'),
    ]),
    dict(id='rose', title='Rosé', profiles=['Pale & dry rosé', 'Fuller rosé'], cards=[
      ('How rosé is made', 'Rosé is made from red grapes whose juice spends only a short time with the skins, a few hours for a pale Provence rosé, a day or more for a darker Tavel. The longer the contact, the deeper the colour and flavour.'),
      ('Pale and dry', 'Provence style: very pale, crisp, delicate red berries and citrus: the {w:w051} and the {w:w054}. Good on its own or with light food.'),
      ('Fuller', 'More colour, more fruit, more body: the {w:w053} drinks almost like a light red, and the {w:w052} is natural and funky (offer a taste). Good with food: lamb, shellfish, spicy dishes.'),
    ], quiz=[
      ('What makes a rosé darker in colour?', ['More time with the grape skins', 'Adding red wine', 'Oak ageing', 'Riper white grapes'], 0, 'Longer skin contact. (Rosé Champagne is the exception: a little red wine is often blended in.)'),
      ('Which of our rosés drinks almost like a light red?', ['{w:w053}', '{w:w051}', '{w:w054}', 'None of them'], 0, 'Tavel has more skin contact, colour and body.'),
    ]),
    dict(id='lightred', title='Light and fresh reds', profiles=['Light & fresh red'], cards=[
      ('What they taste like', 'Light body, soft tannins and bright acidity: cherry, raspberry, redcurrant. Easy to drink, and several of them are good slightly chilled.'),
      ('What to say', '“Light and juicy.” For a guest who wants “a red but not heavy”, Pinot Noir, or a red with fish. The {w:w026} is served chilled.'),
      ('With food', 'Charcuterie, roast chicken, salmon and tuna, mushrooms, lighter pasta.'),
    ], quiz=[
      ('Light and fresh reds usually have…', ['Soft tannins and bright acidity', 'Heavy tannins and high alcohol', 'Lots of sweetness', 'Strong new oak'], 0, 'Low tannin is why they work chilled and with fish.'),
      ('Which red is served chilled?', ['{w:w026}', '{w:w042}', '{w:w039}', '{w:w041}'], 0, 'The Novaia Valpolicella is listed as also served chilled.'),
    ]),
    dict(id='medred', title='Medium and savoury reds', profiles=['Medium & savoury red'], cards=[
      ('What they taste like', 'Medium body, real structure, and flavours beyond fruit: herbs, earth, leather, spice, cedar. Most of our Bordeaux, Rhône and Italian reds sit here.'),
      ('What to say', '“Savoury, with some structure.” For a guest who wants a classic red with dinner: claret, Rioja, Chianti-style Sangiovese.'),
      ('With food', 'Lamb, steak, duck, game birds, aged cheeses, tomato-based dishes for the Italians.'),
    ], quiz=[
      ('Which flavours mark a savoury red?', ['Herbs, earth and leather', 'Lemon and green apple', 'Honey and apricot', 'Bubblegum and banana'], 0, 'Savoury means beyond fruit.'),
      ('Which dish suits a medium, savoury red best?', ['Roast lamb', 'Oysters', 'Lemon tart', 'Green salad'], 0, 'Structure needs protein.'),
    ]),
    dict(id='bigred', title='Rich and powerful reds', profiles=['Rich & powerful red'], cards=[
      ('What they taste like', 'Full body, ripe or concentrated dark fruit, often high alcohol and firm tannin: blackberry, plum, chocolate, pepper, spice.'),
      ('What to say', '“Big and generous.” For a guest who asks for Malbec, Shiraz or “something bold”. Warn about tannin where it matters: the {w:w033} grips hard.'),
      ('With food', 'Red meat, braises, game, hard cheeses. The {w:w039} also works after dinner with cheese.'),
    ], quiz=[
      ('A guest asks for “a Malbec or a Shiraz”. Which style do you look at?', ['Rich and powerful reds', 'Light and fresh reds', 'Pale rosé', 'Aromatic whites'], 0, 'Bold, full, dark fruit.'),
      ('Amarone is rich because…', ['The grapes are dried before fermenting', 'It is aged for 20 years', 'Sugar is added', 'It is blended with Port'], 0, 'Drying concentrates sugar and flavour (appassimento).'),
    ]),
    dict(id='sweet', title='Sweet and fortified', profiles=['Sweet wine', 'Fortified wine'], cards=[
      ('Two ways to make a sweet wine', '<b>Concentrate the grape:</b> noble rot (Sauternes, Barsac, Coteaux du Layon) or drying the grapes (Vin Santo). <b>Stop the fermentation:</b> add grape spirit while it still has sugar. That is fortification: Port and Maury.'),
      ('Noble rot', 'Botrytis is a mould that, in misty autumn mornings and dry afternoons, shrivels ripe grapes and concentrates their sugar and acidity. It gives honey, apricot, marmalade and saffron notes. Our three: the {w:w071}, the {w:w072} and the {w:w073}.'),
      ('Port and Maury', 'Fortified wines are stronger: around 16% for Maury, around 19–20% for Port. The {w:w070} and the {w:w068} are red and rich; the {w:w069} and the {w:w074} are white Ports, nutty and honeyed. White Port is served chilled.'),
      ('Serving', 'Dessert and fortified wines are poured in 75ml glasses. Some come in half bottles (37.5cl) or 50cl bottles, which suit two people.'),
      ('With food', 'The rule: the wine should be at least as sweet as the dessert. Sauternes with blue cheese or fruit tarts; LBV with cheese; Maury with chocolate; Vin Santo with cantucci.'),
    ], quiz=[
      ('How is Port made sweet?', ['Grape spirit is added during fermentation', 'Sugar is added at bottling', 'The grapes are frozen', 'Noble rot'], 0, 'Fortification stops the yeast, so natural sugar stays in the wine.'),
      ('Which of our dessert wines is made with noble rot?', ['{w:w071}', '{w:w070}', '{w:w068}', '{w:w069}'], 0, 'Sauternes is the classic noble rot wine.'),
      ('What size is a dessert wine glass at Finch?', ['75ml', '125ml', '175ml', '50ml'], 0, 'Dessert and fortified wines are poured in 75ml.'),
      ('Which dessert wine goes best with chocolate?', ['{w:w068}', '{w:w071}', '{w:w073}', '{w:w069}'], 0, 'Red, fortified Grenache handles chocolate, which beats most wines.'),
    ]),
  ]),

  dict(id='grapes', title='Grapes on our list', blurb='The grapes behind the list: what each tastes like and where to find it.', lessons=[
    dict(id='chardonnay', title='Chardonnay', wines=['w007', 'w016', 'w015', 'w022', 'w025', 'w021', 'w023', 'w060', 'w055'], cards=[
      ('The great all-rounder', 'Chardonnay takes on the character of where it grows and how it is made. On its own it is fairly neutral: apple, pear, citrus. The place and the cellar add the rest.'),
      ('Unoaked', 'In Chablis, in cool Burgundy, it is crisp and stony: green apple, lemon, a salty finish ({w:w007}). The Premier Cru ({w:w016}) has more depth.'),
      ('Oaked', 'In the Côte de Beaune it is richer, with hazelnut, butter and toast from barrels: {w:w015}, {w:w022}, {w:w025}. The Italian {w:w023} and the Californian {w:w021} are in the same family.'),
      ('Sparkling', 'Chardonnay is one of the three Champagne grapes. A Blanc de Blancs is all Chardonnay ({w:w060}). It is also most of the {w:w055}.'),
    ], quiz=[
      ('Which of these is unoaked Chardonnay?', ['{w:w007}', '{w:w025}', '{w:w023}', '{w:w022}'], 0, 'Village Chablis here is unoaked.'),
      ('A Blanc de Blancs Champagne is made from…', ['Chardonnay', 'Pinot Noir', 'Pinot Meunier', 'Sauvignon Blanc'], 0, 'White grapes only.'),
      ('Which of these is NOT made from Chardonnay?', ['{w:w019}', '{w:w021}', '{w:w015}', '{w:w016}'], 0, 'Condrieu is Viognier.'),
    ]),
    dict(id='loire', title='Sauvignon Blanc and Chenin Blanc', wines=['w013', 'w020', 'w002', 'w010', 'w024', 'w009', 'w056', 'w073'], cards=[
      ('Sauvignon Blanc', 'Zesty and aromatic: lime, grapefruit, gooseberry, green herbs, cut grass. In the Loire it can be flinty or smoky: {w:w013} and {w:w020}. The {w:w002} is from the Alps in northern Italy.'),
      ('Sauvignon in Bordeaux', 'In Bordeaux, Sauvignon Blanc is blended with Sémillon, often in oak, for a rounder, waxier white: {w:w010} and {w:w024}. The same pair makes Sauternes.'),
      ('Chenin Blanc', 'The Loire\'s other great white grape: apple, quince, honey and very high acidity. It is made in every style: dry ({w:w009}), sparkling ({w:w056}) and sweet with noble rot ({w:w073}).'),
    ], quiz=[
      ('Sancerre and Pouilly-Fumé are both made from…', ['Sauvignon Blanc', 'Chardonnay', 'Chenin Blanc', 'Melon de Bourgogne'], 0, 'Same grape, opposite banks of the Loire.'),
      ('In white Bordeaux, Sauvignon Blanc is usually blended with…', ['Sémillon', 'Chardonnay', 'Riesling', 'Viognier'], 0, 'Sémillon adds body and a waxy texture.'),
      ('Which grape makes dry, sparkling and sweet wines on our list?', ['Chenin Blanc', 'Sauvignon Blanc', 'Vermentino', 'Albariño'], 0, 'Savennières, Vouvray La Dilettante and Coteaux du Layon.'),
    ]),
    dict(id='aromawhites', title='Aromatic and coastal whites', wines=['w004', 'w006', 'w019', 'w003', 'w012', 'w001', 'w005'], cards=[
      ('Riesling', 'Very high acidity with lime, peach and sometimes honey. Can be bone dry or sweet. The {w:w004} is the old-school, rounder style.'),
      ('Grüner Veltliner', 'Austria\'s grape: green apple, citrus and a white-pepper note. Ours is a natural, funky take ({w:w006}).'),
      ('Viognier', 'Perfumed and rich: apricot, peach, blossom, gentle acidity. Condrieu is its home ({w:w019}).'),
      ('By the sea', '<b>Albariño</b> (Galicia): peach, citrus and a salty finish ({w:w003}). <b>Vermentino</b> (coastal Italy): citrus, herbs and almond, our house white {w:w012}. <b>Melon de Bourgogne</b> (Muscadet): light, neutral, salty-fresh ({w:w001}).'),
      ('English aromatics', 'Bacchus and other cool-climate grapes: elderflower, hedgerow, citrus ({w:w005}).'),
    ], quiz=[
      ('Which grape is our house white, Finch Bianco?', ['Vermentino', 'Chardonnay', 'Pinot Grigio', 'Sauvignon Blanc'], 0, 'Finch Bianco is Montefoscoli\'s Tuscan Vermentino.'),
      ('Condrieu is made from…', ['Viognier', 'Riesling', 'Chardonnay', 'Chenin Blanc'], 0, 'Apricot and blossom.'),
      ('Which grape often has a white-pepper note?', ['Grüner Veltliner', 'Viognier', 'Albariño', 'Melon de Bourgogne'], 0, 'Pepper is Grüner\'s calling card.'),
    ]),
    dict(id='otherwhites', title='Italian, Spanish and Rhône whites', wines=['w011', 'w008', 'w014', 'w018', 'w017'], cards=[
      ('Italy', '<b>Garganega</b> is the Soave grape: almond, lemon, soft texture ({w:w011}). <b>Carricante</b> is Etna\'s white: lemon and very mineral ({w:w008}). <b>Friulano</b> brings pear and almond, in the {w:w014} with Sauvignon and Chardonnay.'),
      ('Spain', '<b>Xarel·lo</b> is Catalonia\'s grape, the backbone of Cava. Made still, as in the {w:w018}, it is textured, herbal and saline, close to white Burgundy.'),
      ('The southern Rhône', 'White Châteauneuf-du-Pape blends Grenache Blanc, Clairette, Roussanne and Bourboulenc: full-bodied, orchard fruit and flowers ({w:w017}).'),
    ], quiz=[
      ('Soave is made from…', ['Garganega', 'Vermentino', 'Carricante', 'Friulano'], 0, 'Garganega, from the hills east of Verona.'),
      ('Xarel·lo is best known as a grape for…', ['Cava', 'Champagne', 'Port', 'Rioja'], 0, 'The Vinya del Coll shows what it does as a still wine.'),
      ('Which white on our list grows on a volcano?', ['{w:w008}', '{w:w011}', '{w:w014}', '{w:w018}'], 0, 'Etna. (The Soave is from old volcanic hills too, but Etna is an active volcano.)'),
    ]),
    dict(id='pinot', title='Pinot Noir and Gamay', wines=['w031', 'w049', 'w048', 'w028', 'w036', 'w061', 'w058', 'w062'], cards=[
      ('Pinot Noir', 'Light to medium body, low tannin, high acidity: red cherry, raspberry, earth, mushroom with age. Burgundy is its home: {w:w031} and {w:w049}. From Champagne, as a still red, it is a real rarity: {w:w048}.'),
      ('Pinot in Champagne', 'Pinot Noir and Pinot Meunier are the two black Champagne grapes. They give body and red fruit; Meunier is the fruitier one ({w:w062} is all Meunier).'),
      ('Gamay', 'The Beaujolais grape: juicy red fruit, very low tannin, often good lightly chilled. The cru villages make the serious ones: {w:w028} is fresh and light, {w:w036} is the deepest and firmest.'),
    ], quiz=[
      ('Red Burgundy is made from…', ['Pinot Noir', 'Gamay', 'Merlot', 'Syrah'], 0, 'Pinot Noir. Beaujolais, just south, is Gamay.'),
      ('Which grape makes Beaujolais?', ['Gamay', 'Pinot Noir', 'Grenache', 'Cabernet Franc'], 0, 'Juicy, low tannin.'),
      ('Which is the deepest, firmest of our Beaujolais?', ['{w:w036}', '{w:w028}', 'Both are the same', 'Neither: they are both rosé'], 0, 'Morgon Côte du Py is the most structured Beaujolais.'),
    ]),
    dict(id='bordeaux', title='The Bordeaux grapes', wines=['w050', 'w040', 'w035', 'w032', 'w037'], cards=[
      ('Cabernet Sauvignon', 'Blackcurrant, cedar, firm tannin. It leads on the Left Bank of Bordeaux, in the Médoc and Graves: {w:w050}, {w:w040}.'),
      ('Merlot', 'Plum and dark cherry, rounder and softer. It leads on the Right Bank, in Saint-Émilion and Pomerol: {w:w032}, {w:w037}.'),
      ('Cabernet Franc', 'Raspberry, violets, a leafy freshness. A blending partner on both banks.'),
      ('Blends', 'Bordeaux is almost always a blend. The {w:w035} from Pessac-Léognan uses Merlot and both Cabernets.'),
    ], quiz=[
      ('Which grape leads in Saint-Émilion and Pomerol?', ['Merlot', 'Cabernet Sauvignon', 'Syrah', 'Pinot Noir'], 0, 'The Right Bank is Merlot country.'),
      ('Blackcurrant and cedar are classic notes of…', ['Cabernet Sauvignon', 'Gamay', 'Grenache', 'Pinot Noir'], 0, 'Left Bank Bordeaux.'),
      ('Pavillon Rouge is led by…', ['Cabernet Sauvignon', 'Merlot', 'Cabernet Franc', 'Malbec'], 0, 'Margaux is on the Left Bank.'),
    ]),
    dict(id='rhonereds', title='Syrah and Grenache', wines=['w046', 'w047', 'w027', 'w053', 'w051', 'w068'], cards=[
      ('Syrah', 'Dark fruit, black pepper, black olive, smoked meat, violets. The northern Rhône is its home: {w:w046}. (Called Shiraz in Australia.)'),
      ('Grenache', 'Ripe red fruit, spice, warmth and generous alcohol. It leads in the southern Rhône: {w:w047}, {w:w027}, and in the rosés {w:w053} and {w:w051}. It also makes the sweet red {w:w068}.'),
    ], quiz=[
      ('A guest asks for Shiraz. Which grape is the same?', ['Syrah', 'Grenache', 'Merlot', 'Zinfandel'], 0, 'Shiraz and Syrah are the same grape.'),
      ('Which grape leads Châteauneuf-du-Pape?', ['Grenache', 'Syrah', 'Pinot Noir', 'Cabernet Sauvignon'], 0, 'The southern Rhône is Grenache-led.'),
    ]),
    dict(id='italianreds', title='Italian reds', wines=['w042', 'w043', 'w034', 'w030', 'w045', 'w026', 'w039', 'w044'], cards=[
      ('Nebbiolo', 'Pale in the glass but powerful: roses, tar, cherry, with high tannin and acidity. Piedmont\'s great grape: {w:w042} and {w:w043}.'),
      ('Sangiovese', 'Tuscany\'s grape, and Chianti\'s: sour cherry, herbs, tea leaf, bright acidity. Our house red {w:w034}, {w:w030} and {w:w045}.'),
      ('Corvina', 'The Valpolicella grape: fresh cherry and light ({w:w026}). Dried for months before fermenting, it makes Amarone ({w:w039}).'),
      ('Nerello Mascalese', 'Etna\'s red: pale, red-fruited, mineral, often compared to Pinot Noir ({w:w044}).'),
    ], quiz=[
      ('Barolo and Barbaresco are made from…', ['Nebbiolo', 'Sangiovese', 'Corvina', 'Barbera'], 0, 'Both are Nebbiolo from Piedmont.'),
      ('Our house red, Finch Rosso, is made from…', ['Sangiovese', 'Nebbiolo', 'Merlot', 'Corvina'], 0, 'Montefoscoli\'s Tuscan Sangiovese.'),
      ('Amarone and Valpolicella share the same grape. What makes Amarone different?', ['The grapes are dried first', 'It is from Sicily', 'It is aged in new oak only', 'It is fortified'], 0, 'Appassimento: drying concentrates everything.'),
    ]),
    dict(id='worldreds', title='Tempranillo, Zinfandel and Saperavi', wines=['w038', 'w029', 'w041', 'w033', 'w070'], cards=[
      ('Tempranillo', 'Spain\'s great grape: strawberry, plum, leather, and it takes well to long oak ageing. In Rioja ({w:w038}) and, as Tinta de Toro, in Toro ({w:w029}). In Portugal it is called Tinta Roriz and goes into Port ({w:w070}).'),
      ('Zinfandel', 'California\'s own: ripe blackberry, spice, generous alcohol ({w:w041}).'),
      ('Saperavi', 'Georgia\'s grape, red-fleshed as well as red-skinned: inky, dark and very tannic ({w:w033}).'),
    ], quiz=[
      ('Rioja is mainly made from…', ['Tempranillo', 'Grenache', 'Saperavi', 'Zinfandel'], 0, 'Usually with a little Mazuelo and Graciano.'),
      ('What is unusual about Saperavi?', ['Its flesh is red, not just its skin', 'It is a white grape', 'It is always sweet', 'It only grows in California'], 0, 'Most red grapes have clear juice.'),
    ]),
  ]),

  dict(id='regions', title='Regions on our list', blurb='Where our wines come from, and what each place is known for.', lessons=[
    dict(id='champagne', title='Champagne', wines=['w058', 'w061', 'w060', 'w062', 'w063', 'w064', 'w065', 'w066', 'w067', 'w048'], cards=[
      ('Where it is', 'The northernmost of France\'s great regions, east of Paris around Reims and Épernay. Cold, with chalk soils that keep vines fed with water and give the wines their fine, chalky finish.'),
      ('The grapes', 'Three main grapes: Chardonnay, Pinot Noir and Pinot Meunier. Most Champagnes blend all three.'),
      ('Houses and growers', 'The big houses buy grapes from many growers and blend for a consistent style: Billecart-Salmon ({w:w058}), Pol Roger ({w:w061}), Roederer ({w:w067}). Growers make wine only from their own vines: {w:w060}, {w:w062}.'),
      ('Prestige cuvées', 'Each house\'s top wine, made only in great years: {w:w066} and {w:w067}.'),
      ('Still wine too', 'Champagne also makes a little still wine, Coteaux Champenois, like the red {w:w048}.'),
    ], quiz=[
      ('What are the three main Champagne grapes?', ['Chardonnay, Pinot Noir, Pinot Meunier', 'Chardonnay, Sauvignon Blanc, Pinot Noir', 'Pinot Noir, Gamay, Chardonnay', 'Chardonnay, Chenin Blanc, Riesling'], 0, 'Most Champagnes blend all three.'),
      ('Which of these is a grower Champagne?', ['{w:w060}', '{w:w058}', '{w:w061}', '{w:w067}'], 0, 'Bonnet-Gilmert makes wine from its own vines.'),
      ('Champagne\'s soil is famous for being…', ['Chalk', 'Volcanic', 'Granite', 'Sand'], 0, 'Chalk.'),
    ]),
    dict(id='burgundy', title='Burgundy and Beaujolais', wines=['w007', 'w016', 'w015', 'w022', 'w025', 'w031', 'w049', 'w028', 'w036'], cards=[
      ('Two grapes', 'Burgundy is Chardonnay for whites and Pinot Noir for reds. Simple grapes, very complicated map.'),
      ('Chablis', 'The cool northern outpost: unoaked, crisp Chardonnay on Kimmeridgian limestone full of fossil oyster shells. {w:w007} and the Premier Cru {w:w016}.'),
      ('The Côte d\'Or', 'The heart of Burgundy, a narrow slope. In the south, the Côte de Beaune, are the great whites: {w:w015}, {w:w022}, {w:w025}, and Volnay\'s elegant reds ({w:w049}).'),
      ('The ladder', 'From the bottom up: regional (Bourgogne, Coteaux Bourguignons: {w:w031}), village (Chablis), Premier Cru (a named top vineyard), Grand Cru (the very best vineyards, like Corton-Charlemagne).'),
      ('Beaujolais', 'Just south of Burgundy, on granite, with Gamay. Ten “cru” villages make the serious wines, including Juliénas ({w:w028}) and Morgon ({w:w036}). Nothing like Beaujolais Nouveau.'),
    ], quiz=[
      ('What is the top level of a Burgundy vineyard?', ['Grand Cru', 'Premier Cru', 'Village', 'Regional'], 0, 'Grand Cru, then Premier Cru, then village, then regional.'),
      ('Which grape makes Burgundy\'s white wines?', ['Chardonnay', 'Sauvignon Blanc', 'Aligoté only', 'Pinot Blanc'], 0, 'Chardonnay (a little Aligoté too, but not on our list).'),
      ('Morgon and Juliénas are…', ['Beaujolais crus', 'Burgundy Grand Crus', 'Rhône villages', 'Champagne villages'], 0, 'Two of the ten Beaujolais crus.'),
    ]),
    dict(id='loirereg', title='The Loire', wines=['w001', 'w009', 'w013', 'w020', 'w056', 'w073'], cards=[
      ('France\'s longest river', 'The Loire runs west to the Atlantic, and its vineyards are mostly cool and fresh. It is white wine country above all.'),
      ('By the sea: Muscadet', 'Near Nantes, from Melon de Bourgogne, aged on its lees: light, salty, made for oysters ({w:w001}).'),
      ('Anjou and Touraine: Chenin Blanc', 'In the middle, Chenin Blanc in every style: dry Savennières ({w:w009}), sweet Coteaux du Layon ({w:w073}), sparkling Vouvray ({w:w056}).'),
      ('The east: Sauvignon Blanc', 'Upstream, Sancerre and Pouilly-Fumé face each other across the river: crisp, flinty Sauvignon Blanc ({w:w020} and {w:w013}).'),
    ], quiz=[
      ('Sancerre and Pouilly-Fumé are on…', ['Opposite banks of the Loire', 'The Atlantic coast', 'Either side of Chablis', 'The Rhône'], 0, 'They face each other across the river.'),
      ('Muscadet is made near…', ['Nantes and the Atlantic', 'Sancerre', 'Lyon', 'Bordeaux'], 0, 'The western end of the Loire.'),
      ('Which Loire grape is used for dry, sweet and sparkling wine?', ['Chenin Blanc', 'Melon de Bourgogne', 'Sauvignon Blanc', 'Chardonnay'], 0, 'Chenin Blanc.'),
    ]),
    dict(id='bordeauxreg', title='Bordeaux', wines=['w050', 'w040', 'w035', 'w010', 'w024', 'w032', 'w037', 'w071', 'w072'], cards=[
      ('Two banks', 'The Gironde estuary splits Bordeaux. The <b>Left Bank</b> (Médoc, Margaux, Pauillac, Pessac-Léognan) has gravel soils and Cabernet Sauvignon-led reds. The <b>Right Bank</b> (Saint-Émilion, Pomerol) has clay and limestone and Merlot-led reds.'),
      ('Classed growths and second wines', 'In 1855 the top Médoc châteaux were ranked into five growths; Château Margaux is a First Growth. Many châteaux also make a <b>second wine</b> from younger vines or lots not used in the main wine: {w:w050}, {w:w040}.'),
      ('Dry whites', 'Sauvignon Blanc and Sémillon, often barrel-fermented, mostly from Pessac-Léognan and around: {w:w010}, {w:w024}.'),
      ('Sauternes and Barsac', 'South of the city, mists from the Ciron river bring noble rot, which makes some of the world\'s great sweet wines: {w:w071}, {w:w072}.'),
    ], quiz=[
      ('Which bank of Bordeaux is Merlot country?', ['The Right Bank', 'The Left Bank', 'Both equally', 'Neither'], 0, 'Saint-Émilion and Pomerol.'),
      ('What is a “second wine”?', ['A château\'s second label, from younger vines or other lots', 'A wine made from leftover grapes of another region', 'A sweet wine', 'The second bottle a table orders'], 0, 'Pavillon Rouge is Château Margaux\'s.'),
      ('What makes Sauternes sweet?', ['Noble rot', 'Added sugar', 'Fortification', 'Frozen grapes'], 0, 'Mists from the Ciron river.'),
    ]),
    dict(id='rhone', title='The Rhône', wines=['w046', 'w019', 'w047', 'w017', 'w027', 'w053'], cards=[
      ('North and south', 'The <b>northern Rhône</b> is steep, narrow and cooler, mostly one grape per wine: Syrah for reds (Côte-Rôtie, {w:w046}) and Viognier for Condrieu ({w:w019}).'),
      ('The south', 'The <b>southern Rhône</b> is wide, warm and windy (the Mistral), and its wines are blends led by Grenache: Châteauneuf-du-Pape ({w:w047}), Rasteau ({w:w027}).'),
      ('White Châteauneuf and Tavel', 'Only a small share of Châteauneuf-du-Pape is white ({w:w017}). Tavel, across the river, was France\'s first rosé appellation and makes only rosé ({w:w053}).'),
    ], quiz=[
      ('Côte-Rôtie is made mainly from…', ['Syrah', 'Grenache', 'Viognier only', 'Merlot'], 0, 'Northern Rhône reds are Syrah.'),
      ('Which wind blows through the southern Rhône?', ['The Mistral', 'The Sirocco', 'The Föhn', 'The Bora'], 0, 'The Mistral keeps vines dry and healthy.'),
      ('Tavel makes only…', ['Rosé', 'Sparkling wine', 'Sweet wine', 'White wine'], 0, 'France\'s first rosé appellation.'),
    ]),
    dict(id='frmore', title='Alsace, Provence and Roussillon', wines=['w004', 'w051', 'w054', 'w068'], cards=[
      ('Alsace', 'On the German border, sheltered by the Vosges mountains, one of the driest parts of France. Whites named by grape: Riesling, Gewurztraminer, Pinot Gris ({w:w004}).'),
      ('Provence', 'The south coast, home of pale, dry rosé, mostly Grenache and Cinsault: {w:w054}, and from the cooler, higher Coteaux Varois, {w:w051}.'),
      ('Roussillon', 'France\'s far south, on the Spanish border. Known for Vins Doux Naturels, sweet wines fortified during fermentation, like Maury ({w:w068}).'),
    ], quiz=[
      ('Alsace wines are usually named after…', ['The grape', 'The château', 'The village only', 'The vintage'], 0, 'Unusually for France, the grape goes on the label.'),
      ('Provence is best known for…', ['Pale, dry rosé', 'Sweet wine', 'Sparkling wine', 'Big tannic reds'], 0, 'Pale and dry.'),
    ]),
    dict(id='italy', title='Italy', wines=['w042', 'w043', 'w026', 'w039', 'w011', 'w002', 'w014', 'w012', 'w034', 'w030', 'w045', 'w023', 'w075', 'w008', 'w044', 'w055'], cards=[
      ('The north-west: Piedmont', 'In the foothills of the Alps, Nebbiolo makes Barolo and Barbaresco: {w:w042}, {w:w043}.'),
      ('The north-east', 'Around Verona, the Veneto: Valpolicella and Amarone ({w:w026}, {w:w039}) and Soave ({w:w011}). Further north and east, the Alps of Trentino ({w:w002}) and Friuli ({w:w014}). Franciacorta, in Lombardy, makes Italy\'s Champagne-method sparkling ({w:w055}).'),
      ('Tuscany and Umbria', 'Sangiovese country: Chianti, Montalcino ({w:w030}, {w:w045}) and our house wines from near Pisa ({w:w012}, {w:w034}). Vin Santo is Tuscany\'s traditional sweet wine ({w:w075}). Umbria, next door, is home to {w:w023}.'),
      ('Sicily: Etna', 'Vineyards on the slopes of Europe\'s most active volcano, up to 1,000m high: {w:w008}, {w:w044}.'),
    ], quiz=[
      ('Barolo comes from…', ['Piedmont', 'Tuscany', 'Sicily', 'Veneto'], 0, 'The Langhe hills of Piedmont.'),
      ('Amarone and Valpolicella come from near…', ['Verona', 'Florence', 'Rome', 'Naples'], 0, 'The Veneto.'),
      ('Brunello di Montalcino is from…', ['Tuscany', 'Piedmont', 'Umbria', 'Friuli'], 0, 'Sangiovese from Montalcino.'),
    ]),
    dict(id='iberia', title='Spain and Portugal', wines=['w038', 'w029', 'w003', 'w018', 'w069', 'w070', 'w074'], cards=[
      ('Rioja', 'Spain\'s most famous red, mostly Tempranillo. Labels tell you how long it was aged; a <b>Gran Reserva</b> has spent at least five years ageing, at least two of them in oak ({w:w038}).'),
      ('Toro', 'A hot, high plateau on the Duero: powerful Tempranillo, locally called Tinta de Toro ({w:w029}).'),
      ('Rías Baixas', 'Galicia, the green, rainy Atlantic north-west: Albariño, made for seafood ({w:w003}).'),
      ('Catalonia', 'Penedès, near Barcelona, is Cava country; the {w:w018} shows the local Xarel·lo as a still wine.'),
      ('Port', 'The Douro valley in northern Portugal. Grape spirit is added during fermentation to keep the wine sweet. Ruby styles (like LBV, {w:w070}) are young and fruity; aged and white styles are nutty: {w:w069}, {w:w074}.'),
    ], quiz=[
      ('A Rioja Gran Reserva must be aged for at least…', ['Five years, two in oak', 'One year', 'Ten years, all in oak', 'Six months'], 0, 'The longest ageing category in Rioja.'),
      ('Albariño comes from…', ['Galicia', 'Rioja', 'Catalonia', 'The Douro'], 0, 'Rías Baixas in Galicia.'),
      ('Port comes from which valley?', ['The Douro', 'The Loire', 'The Rhône', 'The Ebro'], 0, 'Northern Portugal.'),
    ]),
    dict(id='further', title='Austria, England, Georgia and California', wines=['w006', 'w052', 'w005', 'w057', 'w059', 'w033', 'w041', 'w021'], cards=[
      ('Austria', 'Grüner Veltliner is the national grape. Our two Austrian wines are from AWM, a group of young natural winemakers ({w:w006}, {w:w052}).'),
      ('England', 'The south of England has chalk like Champagne\'s and a cool climate, and now makes world-class traditional-method sparkling ({w:w057}, {w:w059}) and aromatic whites ({w:w005}).'),
      ('Georgia', 'Often called the birthplace of wine, with 8,000 years of winemaking. The traditional vessel is the qvevri, a clay jar buried in the ground ({w:w033}).'),
      ('California', 'Warm and sunny, with cooler pockets near the ocean. Old-vine Zinfandel is a Californian speciality ({w:w041}); the Sta. Rita Hills are cooled by Pacific fog, good for Chardonnay ({w:w021}).'),
    ], quiz=[
      ('What is a qvevri?', ['A clay jar buried in the ground', 'A Georgian grape', 'An oak barrel', 'A sweet wine'], 0, 'Georgia\'s traditional winemaking vessel.'),
      ('English sparkling wine is made…', ['The same way as Champagne', 'In a tank like Prosecco', 'With added gas', 'Only from Bacchus'], 0, 'Traditional method, with the Champagne grapes.'),
      ('Austria\'s signature grape is…', ['Grüner Veltliner', 'Riesling', 'Zweigelt', 'Saperavi'], 0, 'Zweigelt is its most planted red.'),
    ]),
  ]),
]
