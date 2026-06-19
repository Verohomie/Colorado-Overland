# Images to Populate the Guide

The guide looks for these files in **/images**. Until a file exists, the page
shows a labeled placeholder (no broken-image icon). Two ways to fill them:

1. **Auto:** run `python3 download_images.py` — it searches Wikimedia Commons
   (free / public-domain / CC) and grabs a good photo for each slot.
2. **By hand:** drop your own photos in with the exact names below, OR scrape
   one of the source links listed (all free-to-use sources).

Route maps (`day1-map.png` … `day9-map.png`): screenshot each day's Google Maps
directions (the “Open in Google Maps” button) or an OnX/Gaia map, and save with
that name.

**Done so far:** `day2-map.png`, `day3-map.png` (route screenshots), plus two TrailsOffroad
waypoint maps wired into the day pages: `day3-trail.png` (Park Creek Rd #1–24) and
`day7-trail.png` (Rimrocker #1–74).
**Still needed:** `day1-map.png`, `day4-map.png`, `day5-map.png`, `day6-map.png`,
`day7-map.png`, `day8-map.png`, `day9-map.png`.

| File | Used for | Subject | Free image sources to scrape |
|------|----------|---------|------------------------------|
| `00.jpg` | Cover hero | San Juan Mountains / overall mood | [Commons: San Juan Mountains](https://commons.wikimedia.org/wiki/Category:San_Juan_Mountains) · [Commons: Colorado mountains](https://commons.wikimedia.org/wiki/Category:Mountains_of_Colorado) |
| `01.jpg` | Day 1 banner | Great Sand Dunes + Sangre de Cristos | [NPS GRSA media](https://www.nps.gov/grsa/learn/photosmultimedia/index.htm) · [Commons: Great Sand Dunes NP](https://commons.wikimedia.org/wiki/Category:Great_Sand_Dunes_National_Park_and_Preserve) |
| `02.jpg` | Day 2 banner | Conejos River / Platoro high country | [Commons: Conejos County](https://commons.wikimedia.org/wiki/Category:Conejos_County,_Colorado) · [Commons: Rio Grande NF](https://commons.wikimedia.org/wiki/Category:Rio_Grande_National_Forest) |
| `03.jpg` | Day 3 banner | Wolf Creek Pass / Treasure Falls | [Commons: Wolf Creek Pass](https://commons.wikimedia.org/wiki/Category:Wolf_Creek_Pass) · [Commons: San Juan NF](https://commons.wikimedia.org/wiki/Category:San_Juan_National_Forest) |
| `04.jpg` | Day 4 banner | Animas Forks ghost town | [Commons: Animas Forks](https://commons.wikimedia.org/wiki/Category:Animas_Forks,_Colorado) · [BLM Alpine Loop](https://www.blm.gov/visit/alpine-loop) |
| `05.jpg` | Day 5 banner | American Basin wildflowers / Handies | [Commons: American Basin](https://commons.wikimedia.org/wiki/Category:American_Basin_(Colorado)) · [USFS wildflowers: American Basin](https://www.fs.usda.gov/wildflowers/regions/Rocky_Mountain/AmericanBasin/index.shtml) |
| `06.jpg` | Day 6 banner | Ouray town in its box canyon | [Commons: Ouray, Colorado](https://commons.wikimedia.org/wiki/Category:Ouray,_Colorado) · [Commons: Million Dollar Highway](https://commons.wikimedia.org/wiki/Category:U.S._Route_550) |
| `07.jpg` | Day 7 banner | Paradox Valley / Rimrocker rim | [Commons: Paradox Valley](https://commons.wikimedia.org/wiki/Category:Paradox_Valley) · [BLM Rimrocker](https://www.blm.gov/visit/rimrocker-trailhead) |
| `08.jpg` | Day 8 banner | Canyonlands Overlook / Moab rim | [Commons: Canyon Rims](https://commons.wikimedia.org/wiki/Category:Canyon_Rims_Recreation_Area) · [Commons: Canyonlands NP](https://commons.wikimedia.org/wiki/Category:Canyonlands_National_Park) |
| `09.jpg` | Day 9 banner | Salt Lake City / Wasatch Front | [Commons: Salt Lake City](https://commons.wikimedia.org/wiki/Category:Salt_Lake_City) · [Commons: Wasatch Range](https://commons.wikimedia.org/wiki/Category:Wasatch_Range) |

## Optional inline photos
The CSS supports `.photo-strip` photo rows (see Day 1 in the AZ reference).
Drop extras (e.g. `fire-wave.jpg`-style) in `/images` and reference them where
you want a 2- or 3-up photo strip.

## Attribution
Wikimedia Commons images are mostly CC-BY / CC-BY-SA / public domain. For a
personal trip guide you're fine; if you ever publish it widely, keep a credits
line. NPS / BLM / USFS photos are generally public domain.

## Historic / mining photos to obtain (added for the new history sections)
Free/archival sources for the Day 4–6 mining-history boxes. Wikimedia = free to reuse;
Denver Public Library & History Colorado hold historic B&W photos (check rights per image).

- **Animas Forks ghost town (Day 4)** — Duncan House, Kalamazoo House, street views:
  Wikimedia https://commons.wikimedia.org/wiki/Category:Animas_Forks,_Colorado ·
  Denver Public Library https://digital.denverlibrary.org/digital/search/searchterm/Animas%20Forks ·
  History Colorado https://www.historycolorado.org/location/animas-forks
- **Engineer Pass / Otto Mears toll road (Day 5)** —
  Western Mining History https://westernmininghistory.com/2239/photos-of-the-otto-mears-toll-road/ ·
  Wikimedia Otto Mears https://commons.wikimedia.org/wiki/Category:Otto_Mears
- **Henson & Ute-Ulay Mine (Day 5)** —
  Legends of America https://www.legendsofamerica.com/henson-colorado/ ·
  History Colorado https://www.historycolorado.org/location/ute-ulay-mine-and-mill ·
  Wikimedia Lake City https://commons.wikimedia.org/wiki/Category:Lake_City,_Colorado
- **Red Mountain District / Yankee Girl Mine (Day 6)** —
  Wikimedia https://commons.wikimedia.org/wiki/Category:Red_Mountain_Mining_District ·
  Yankee Girl https://commons.wikimedia.org/wiki/Category:Yankee_Girl_Mine ·
  Legends of America https://www.legendsofamerica.com/red-mountain-mining-district/ ·
  Denver Public Library https://digital.denverlibrary.org/digital/search/searchterm/Yankee%20Girl%20Mine

To drop these into the guide, save as e.g. `images/hist-animas-forks.jpg`, `hist-ute-ulay.jpg`,
`hist-yankee-girl.jpg`, then tell me where to place them (the history boxes have room for a photo).
