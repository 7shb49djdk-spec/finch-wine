# Bar Finch Wine: the floor team's wine app

A phone app for the Bar Finch floor team. It holds every wine on the list, what each one tastes like, one line to sell it, and how to steer a guest from the words they use. It also has flashcards and quizzes for learning the list. Staff can install it on their phones, and it works without a connection once it has been opened.

The wine data comes from the Bar Finch Cellar Book: prices, vintages, what is poured by the glass or on the Coravin, and where each bottle sits on the display wall. **There are no trade costs or supplier details anywhere in this project.**

## What's in it

The app has two halves, switched at the top of the screen.

**Info** is the wine bible, for looking things up.
- **Wines:** all 75 wines in menu order. Search covers everything: name, grape, region, tasting notes and food pairings (search "lamb" or "oysters"). Filters: by the glass, Coravin, colour, under £100, and style.
- **Each wine page:** prices, the "Sell it" line, anything to watch for, style at a glance (body, sweetness, acidity, tannin, oak, alcohol), what it tastes like, food, how it's served, a story to tell, and, folded away, the producer, vineyard, how it's made, the vintage, its place on the display wall and the sources.
- **By the glass:** the 28 glass pours with 125ml, 175ml, carafe and bottle prices.
- **Guests:** "When a guest says…" for 20 common requests, and the Sancerre page.
- **Reference:** how the list works, wine service at Finch, styles at a glance, grapes, glossary.

**Training** is for learning.
- **Courses:** 31 short lessons in four courses: Tasting basics, Styles on our list, Grapes on our list, and Regions on our list. Everything is built around the wines we pour. Each lesson ends with a quiz; 80% ticks it off.
- **Quizzes:** nine types, built from the list as it is today. Wrong answers go into a review deck.
- **Flashcards:** decks for the glass list, each colour, the whole list, guest requests, grapes and the glossary.
- Progress is kept on each phone.

## Putting it on GitHub (one time, about 5 minutes)

1. Sign in at github.com and click **New repository**.
   - Name it, for example `finch-wine`.
   - Choose **Public**: free GitHub accounts can only publish public repositories as a website.
   - Click **Create repository**.
2. On the new repository's page, click **uploading an existing file**. Drag in **everything inside this folder**, including the folders `css`, `js`, `fonts`, `icons`, `data` and `tools`. Then click **Commit changes**.
3. Go to **Settings → Pages**. Under "Build and deployment", set **Source: Deploy from a branch**, **Branch: main**, folder **/ (root)**, then click **Save**.
4. After a minute or two the page shows the address, something like `https://your-name.github.io/finch-wine/`. That link is the app: send it to the team.

## Installing it on a phone

- **iPhone:** open the link in Safari, tap **Share**, then **Add to Home Screen**.
- **Android:** open the link in Chrome, tap **⋮**, then **Install app** or **Add to Home screen**.

## Updating the list

When the list changes in the Cellar Book, the app needs a new `js/data.js` (and `sw.js`, which tells phones there is a new version).

- **The easy way:** ask Claude to refresh the staff app from the Cellar Book, then upload the two files it gives you to the repository (**Add file → Upload files**, which replaces the old ones).
- **By hand:**
  1. Export the Cellar Book wines and config to a folder, with the prices from its pricing engine in `prices.json`.
  2. Run `python3 tools/build_data.py snapshot <that-folder> prices.json`.
  3. Run `python3 tools/build_data.py build`.

The build refuses to run if the written guidance no longer matches the list. For example, it stops if a wine described as "by the glass" has become bottle only, or if a steering suggestion points at the wrong kind of pour. The wine pages are written in `tools/wines_sparkling.py`, `wines_white.py`, `wines_red.py` and `wines_rose_sweet.py`; food, style and sources come from the research via `tools/curate_research.py` into `tools/content_bible.json`. The guide is in `tools/content_guide.py` and the courses in `tools/content_training.py`.

Phones pick up the new version the next time they open the app online, and a message offers to reload.

## Privacy

GitHub Pages sites are public: anyone who has the link can open the app. It contains only what is on the guest menu plus the staff notes, with no costs, suppliers or stock. Training progress is stored only on each person's phone.

## Technical notes

- Plain HTML, CSS and JavaScript, with no build step and no outside services. The page loads nothing from other sites.
- `sw.js` caches the app for offline use. `tools/build_data.py` updates its version automatically.
- Fonts: Poppins (Indian Type Foundry), under the SIL Open Font License 1.1. See `fonts/OFL.txt`.
