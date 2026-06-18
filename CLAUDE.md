# Colorado Overland — Project Guide

A single-file, self-contained HTML trip guide for a 9-day overland trip
(Denver → San Luis Valley → San Juans → Moab → Salt Lake City),
**June 21–29, 2026**. Two adventurers, one Land Cruiser. Primary author: Brad.

Modeled on the sibling project `/Users/brad-mbp/Desktop/PROJECTS/az-overland`
(same design system). Repo: https://github.com/Verohomie/Colorado-Overland.git
Hosting target: GitHub Pages or Render (static site).

## Files
- **index.html** — the entire guide (cover + 9 day pages + reference). Self-contained
  HTML/CSS/JS, no build step, no dependencies. Open it directly in a browser.
- **images/** — `00.jpg` (cover), `01–09.jpg` (day banners), `dayN-map.png` (route maps).
  Missing images render as labeled placeholders (no broken icons).
- **gpx files/** — GPX tracks/waypoints for OnX Offroad, Gaia GPS, Google Maps.
- **make_gpx.py** — regenerates the GPX files from waypoint definitions.
- **download_images.py** — fetches free landmark photos from Wikimedia Commons.
- **IMAGES.md** — every image slot + free source links to scrape.

## How it works
- **Vanilla only** — plain HTML/CSS/JS. No React/Vue, no framework, no bundler
  (matches Brad's stack conventions).
- **Live weather** — each day's `.weather-box[data-lat][data-lon][data-date]`
  fetches a forecast from **Open-Meteo** (`api.open-meteo.com`, no API key) on
  load and fills the cells. Open-Meteo only forecasts ~16 days out, so live data
  resolves when viewed near the trip; otherwise each cell falls back to its
  `data-fallback` (late-June seasonal norm) and the status line says so.
- **Design system** — copied/adapted from az-overland: Playfair Display + Source
  Serif 4 + JetBrains Mono; rust/ember/gold/sage/alpine palette; `.book` page,
  `.day-banner`, `.feel-box`, `.options-grid`, `.hikes-grid`, `.camp-grid`,
  `.golden-hour`, `.quick-decisions`, `.fuel-box`, `.lc-box`, `.weather-box`.
- **Each day page** follows Brad's locked spec: What Today Feels Like → live
  Weather → GPX → 3–4 “Choose Your Day” options → Short Hikes → decision-ready
  Camp grid (Best View / Wind-Protected / Easy Backup) → Golden Hour → Quick
  Decisions + Fuel → Land Cruiser Advantage. Every element links to Google Maps.

## Editing conventions
- Add a day: copy a `.day-page` block, bump the id (`day-N`), update the
  `.weather-box` `data-lat/lon/date` + each cell's `data-fallback`, and add a
  row to the cover `.cover-table`.
- Coordinates: camp + trailhead pins are in the reference table. Pins marked
  “~ scout” are approximate — verify in OnX/Gaia before relying on them.
- Map links use either `maps.google.com/?q=LAT,LON` or `?q=Place+Name`, and the
  per-day banner uses a `maps/dir/...` directions URL.

## Open items / to confirm with Brad
- **Day 2 camp = Platoro Reservoir** (resolved). Brad dropped the "Mamouth"
  reference; camp is the Platoro Reservoir north-shore dispersed area, with Mix
  Lake CG (1 mi W, 22 sites, treed) as the sheltered backup.
- **OnX / TrailsOffroad trail data**: incorporating their detailed trail tracks
  (Park Creek Rd #8613, Rim Rocker, Alpine Loop) needs login access — those
  pages are behind auth. If Brad shares access (or exports GPX from his
  accounts), drop the GPX into `gpx files/` and link it from the day pages.
- **Photos**: run `download_images.py` or hand-place per IMAGES.md.
- **Route maps**: screenshot Google Maps/OnX per day → `images/dayN-map.png`.

## Don't break
- Keep it a single self-contained `index.html` (works offline except live weather).
- Keep the image-placeholder + weather-fallback JS at the end of `index.html`.
- Touch-first / iPad-friendly: large tap targets, no hover-only interactions
  required (hover is enhancement only).
