# Colorado Overland — Handoff / Resume Notes

_Updated 2026-06-18 (session 4). Everything below is DONE + pushed to GitHub (main).
Waypoint reference data retained for future tweaks._

## CURRENT STATE (resume here)
- ✅ Days 3/7/8 enriched from TrailsOffroad PDFs (Park Creek/Elwood Pass + Rimrocker).
- ✅ Pushed to GitHub `Verohomie/Colorado-Overland` (main). NOT on GitHub Pages yet (offered).
- ✅ **Lat/long audit done** — 19 pins corrected vs TopoZone/NPS/14ers/recreation.gov.
  Full before/after + flag-list in `VERIFY-PINS.md`. Worst were Treasure Falls (~2.3mi),
  Engineer Pass (~2.1mi), Cinnamon Pass (~1.9mi), Black Canyon S-Rim (~1.8mi), Andrews Lake (~1.4mi).
- ✅ Brad's 4 images incorporated: `day2-map.png`, `day3-map.png` (route screenshots),
  `day3-trail.png` (Park Creek #1–24), `day7-trail.png` (Rimrocker #1–74).

## STILL OPEN / NEXT
- Route-map screenshots still needed: day1, day4, day5, day6, day7, day8, day9 `-map.png`
  (Brad screenshots Google Maps/OnX; placeholders show until then). Tracked in IMAGES.md.
- Flagged dispersed pins in `VERIFY-PINS.md` need Brad's visual confirm OR exact GPX export
  from his OnX/TrailsOffroad accounts (drop into `gpx files/`, then I swap approximate tracks).
- Offer still open: enable GitHub Pages (`gh`) to make it live.
- Tidy (optional): `download_images.py` has dead `search_first_file()` (lines 34–54), unused.
- Reminder given to Brad: rotate OnX/TrailsOffroad passwords (were pasted in chat; never stored).

## STATUS
- ✅ Project built: `index.html` (cover + 9 days + reference), live Open-Meteo weather
  (verified working), 7 GPX files, 10 Wikimedia photos downloaded, `download_images.py`,
  `IMAGES.md`, `CLAUDE.md`, `make_gpx.py`. Git initialized + committed locally.
- ✅ Remote set to https://github.com/Verohomie/Colorado-Overland.git — **NOT pushed yet**
  (waiting on Brad's go-ahead).
- ✅ Day 2 camp = Platoro Reservoir (Mamouth reference dropped per Brad).

## NEXT (in progress when we stopped): enrich Days 3, 7, 8 from Brad's two TrailsOffroad PDFs
Brad shared full waypoint guides for **Park Creek Road (#380)** and **Rimrocker**.
Fold the real waypoints/camps/hazards below into the HTML. Key line anchors:
`id="day-3"` ~L589, `id="day-7"` ~L1192, `id="day-8"` ~L1338.

### ROUTE CORRECTION (important)
- **Park Creek Rd (FSR 380)** = EASY graded dirt, **27 mi, ~3 hrs**, 2WD-HC ok (4WD if wet).
  Connects **Hwy 160 (SW of South Fork, MM 178–179)** ↔ **Stunner Camp** over **ELWOOD
  PASS (11,631 ft)** — NOT Stunner Pass. High point is Elwood Pass.
- **FSR 250 (Alamosa River Rd)** is the separate link: Stunner Camp → over **Stunner Pass**
  → Platoro → Hwy 17 → Antonito.
- So the real flow: **Day 2** Sand Dunes → Hwy 17 → Horca → FSR 250 → **Platoro Reservoir
  (camp)**. **Day 3** FSR 250 over Stunner Pass → Stunner Camp → full Park Creek Rd (380)
  over Elwood Pass → Hwy 160 → US-160 W over Wolf Creek → Pagosa → Durango.
- Day 3 is therefore the **Park Creek trail day + drive to Durango** (currently framed as a
  light resupply day — rebalance it).

### PARK CREEK ROAD (FSR 380) — waypoints (N→S, Hwy 160 → Stunner; Brad drives S→N)
- WP1 Hwy 160 Trailhead (0 mi) — bridge + staging area, just N of Park Creek CG, MM 178–179.
- WP2 Creekside Camping (1.77) — several creekside sites, tent to multi-vehicle.
- WP3 Large Campsite (1.91) — big, level, creekside, good for hammocks.
- WP4 Dispersed Area (2.35) — large open both sides, RV/group, sites close together.
- WP5 Fox Mountain Rd / Corral Park (3.06) — open-meadow camping.
- WP6 Demi John Rd (3.91) — **incredible aspen campsite overlooking the valley** (S side).
- WP7 Meadow Camping / Coal Mine Park (4.82) — large open sites, popular in hunting season.
- WP8–10 Swale Lake Rd (6.73–9.3) — narrow rocky spur to Swale Lake.
- WP15 Summitville Rd (14.6) — 12,536-ft South Mountain in view; 330 → Summitville Superfund.
- WP16 **Alpine Campsite (15.56) — 11,266 ft, spectacular 360° views, pine wind-block from W.**
- WP19 **Mountain View Campsites (17.42)** — grassy plateau, level, views of Cropsy/Lookout/
  Prospect/Long Trek/Montezuma Peaks; overlooks Schinzel Flats.
- WP20 **Elwood Cabin (17.81)** — reservable FS cabin (recreation.gov), built 1911 as telephone
  "line shack", overlooks Schinzel Flats. Cool history.
- WP21 Elwood Pass + East Fork Rd (18.1) — saddle of Elwood Pass; East Fork Rd = harder, rocky.
- WP22 Campsites (19.5) — small sites near Crater Lake hiking trail / CDT resupply spot.
- WP23 Treasure Creek Rd (22.54) — around Lake De Nolda (private, no access), rougher/bumpier.
- WP24 **Stunner Cabin & Campground (26.66)** — 5 sites, tables, fire pits, vault toilet; small
  (popups only). Historic rebuilt Stunner Cabin.
- WP25 Alamosa River Rd / FSR 250 jct (26.99) — old Stunner Mining Camp. Right/S = Stunner Pass
  → Platoro → Hwy 17. Left/N = Alamosa River → Jasper → Terrace Reservoir → Alamosa.
- Camping: abundant dispersed entire length; Elwood Cabin (reservable) + Stunner CG (improved).

### RIMROCKER — 160.88 mi, MODERATE (3/3), Stock SUV HC + 4-low. Open 5/16–11/30. ~2 days.
Concerns: Width, Mud, Pinstriping, High Water Crossings. 4 segments:
- **Montrose→Nucla (WP1–21, 0–59mi):** Uncompahgre NF, graded gravel 2-wide, most vehicles ok.
  Abundant dispersed. Logging trucks. Slick when wet.
- **Nucla→Manti-La Sal (WP21–52):** rougher dirt, HC+4WD rec, single-vehicle width, desert,
  uranium-mining history, cattle. Tabeguache Creek crossing 12–24" swift.
- **Manti-La Sal→La Sal Pass Rd (WP52–58):** well-graded; **most beautiful section** (E of La Sals);
  camping = designated-only near Buckeye.
- **La Sal Pass Rd→Moab (WP58–74):** bumpy/slow; WP59–63 rough rocky two-track, pinstriping,
  NOT suitable for camping; then Black Ridge eases into Moab.
Key waypoints:
- WP1 **Rimrocker Trailhead = Dry Creek Recreation Area BLM lot (Montrose), mi 0** — air down here.
- WP4 **Iron Springs CG (14.81)** — rustic, 8 tent sites, vault toilet.
- WP11 **Tabeguache Overlook (29.72)** — short loop pullout, photo op of Tabeguache Basin.
- WP12 **Columbine Pass / Columbine CG (30.52)** — turn L/S onto Delta-Nucla Rd (USFS 503);
  CG is 1/2 mi N, 6 tent sites + vault toilet.
- WP15–21 **Nucla (~52mi)** — small town. **No gas station anymore** → go S on CO-97 to **Naturita
  (10 min) for fuel/supplies.**
- WP25 **Tabeguache River Crossing (68.81)** — 12–24" deep, swift; most dangerous obstacle.
- WP26 **Rock Raven Mine / Uravan ghost town (71.69)** — uranium/vanadium Manhattan-Project town,
  EPA Superfund; green-hued rocks = uranium ore.
- WP47 **"Epic Campsite" (98.57)** — great dispersed ridge site overlooking **Paradox Valley**
  (THIS is the real "Paradox overlook" camp; replace my ~38.33,-108.88 estimate / Day 7 best-view).
- WP52–53 **Buckeye Reservoir (107–108.26)** — popular, old-growth pines, vistas; **camping
  DESIGNATED-ONLY here**, fills fast without planning.
- WP54 CO/UT state line (108.84).
- WP58 **La Sal Pass Rd (124.68)** — popular dispersed camping; lots of ATV traffic.
- WP59–63 (125.9–134.48) — narrow/rough/pinstriping; no camping; trailers not advised.
- WP64 Black Ridge Trail (137.28) — winding canyon road, final drop to Moab.
- WP74 Trail ends south side of Moab (160.73).
Day split: Day 7 Montrose(0) → Epic Campsite Paradox (98.6, camp). Day 8 → Buckeye → La Sal →
rough 59–63 → Black Ridge → Moab → out to Brad's rim camp (N arch pin best for Day 9 SLC).

## ALSO TODO
- Update `make_gpx.py` (02 Park Creek: add Stunner Camp, Elwood Pass, Elwood Cabin, Alpine
  Campsite; 07 Rimrocker: Dry Creek TH, Iron Springs, Columbine, Tabeguache crossing, Uravan,
  Epic Campsite mi98.6, Buckeye, La Sal Pass) then regenerate.
- Update reference POI table + CLAUDE.md with corrected Elwood Pass / Epic Campsite / Dry Creek TH.
- Ask Brad: push to GitHub? route-map screenshots (dayN-map.png)?
- Brad to rotate OnX/TrailsOffroad passwords (shared in chat) + can export real GPX from his
  accounts to drop in `gpx files/`.
