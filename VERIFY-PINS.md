# Lat/Long Verification — June 2026 audit

Every pin in the guide was re-checked against authoritative sources (TopoZone/USGS GNIS,
NPS, recreation.gov, 14ers.com, TheDyrt, TrailsOffroad). Below: what was **corrected**
(2+ source agreement) and what still **needs your eyes** (couldn't get 2 clean matches —
mostly dispersed campsites with no published coordinate).

_Note: GPX files were removed from the project 2026-06-19 (navigation is via OnX/TrailsOffroad/Gaia).
Coordinates below live in index.html map/camp links only._

## ✅ Corrected (2+ source agreement) — applied to index.html

| Place | Was (wrong) | Now (verified) | Off by | Sources |
|-------|-------------|----------------|--------|---------|
| Engineer Pass | 37.9722, -107.5447 | **37.9756, -107.5845** | ~2.1 mi | TopoZone, onX |
| Cinnamon Pass | 37.9356, -107.5036 | **37.9339, -107.5378** | ~1.9 mi | TopoZone |
| American Basin TH | 37.9258, -107.5044 | **37.9203, -107.5164** | ~0.7 mi | 14ers.com |
| Andrews Lake TH (Crater Lake) | 37.7283, -107.7060 | **37.7492, -107.7096** | ~1.4 mi | UncoverCO, gjhikes |
| Treasure Falls | 37.4708, -106.8503 | **37.4431, -106.8739** | ~2.3 mi | TopoZone/USGS |
| Black Canyon S-Rim VC | 38.5754, -107.6912 | **38.5778, -107.7243** | ~1.8 mi | NPS, recreation.gov |
| Zapata Falls TH | 37.6233, -105.5503 | **37.6216, -105.5595** | ~0.5 mi | AllTrails, onX |
| Box Cañon Falls (entrance) | 38.0206, -107.6745 | **38.0195, -107.6769** | ~0.2 mi | WorldWaterfallDB |
| Cascade Falls (lower TH) | 38.0258, -107.6680 | **38.0225, -107.6586** | ~0.5 mi | Trailforks, AllTrails |
| Upper Cascade Falls TH | 38.0258, -107.6680 | **38.0216, -107.6666** | ~0.3 mi | Trailforks |
| Ouray Hot Springs | 38.0247, -107.6716 | **38.0290, -107.6725** | ~0.3 mi | TopoZone |
| South Mineral CG | 37.8089, -107.7717 | **37.8061, -107.7742** | ~0.3 mi | FS, climb13ers |
| Animas Forks | 37.9289, -107.5722 | **37.9311, -107.5715** | ~0.15 mi | TopoZone/GNIS |
| Molas Lake | 37.7479, -107.6896 | **37.7475, -107.6832** | ~0.4 mi | molaslake.com |
| Mix Lake CG | 37.3470, -106.5480 | **37.3583, -106.5381** | ~1.0 mi | TopoZone, FS |
| Red Mountain Pass | 37.8969, -107.7114 | **37.8989, -107.7120** | ~0.15 mi | TopoZone |
| GSD Visitor Center | 37.7339, -105.5117 | **37.7337, -105.5107** | ~0.05 mi | NPS (see flag) |
| GSD Dunes day-use lot | 37.7456, -105.5197 | **37.7356, -105.5108** | ~0.8 mi | NPS (see flag) |
| Piñon Flats CG | 37.7385, -105.5106 | **37.7426, -105.5110** | ~0.3 mi | NPS "1 mi N of VC" |

## ✅ Confirmed already-correct
Handies Peak summit (37.9131, -107.5042), Silverton, Lake City, Montrose, Moab, SLC,
Durango Animas River Trail — all matched within a block.

## 🚩 NEEDS YOUR EYES — no published coordinate / 2nd match (tap to view, then drag-pin if needed)

These are **dispersed campsites or mile-marker references** with no authoritative point. The
links open my best estimate in Google Maps — eyeball the satellite view and adjust if wrong.

- **Day 1 — lower Medano Pass timbered sites (#3–#7):** https://maps.google.com/?q=37.785,-105.490 — approximate; real spot is whichever numbered site is open.
- **Day 2 — Platoro Reservoir north-shore camp:** https://maps.google.com/?q=37.356,-106.535 — reservoir centroid is ~37.349,-106.550; pick a north-shore pullout.
- **Day 4 — Engineer Pass approach dispersed camp:** https://maps.google.com/?q=37.955,-107.560 — scout pullouts above Animas Forks; not a fixed site.
- **Day 5 — American Basin camp:** https://maps.google.com/?q=37.9203,-107.5164 — set to the trailhead; camping is in pullouts just below, fragile tundra.
- **Day 5 — Burrows Park / Grassy Gulch camp:** https://maps.google.com/?q=37.940,-107.420 — approximate; CR-30 dispersed toward Lake City.
- **Day 7 — Rimrocker "Epic Campsite" (mi 98.6, Paradox rim):** https://maps.google.com/?q=38.33,-108.88 — TrailsOffroad lists it by mile only; confirm on your OnX track.
- **Day 7 — Dry Creek Rec Area (Rimrocker mi 0):** Day 7 links to it by name; confirm the BLM Dry Creek lot in OnX.
- **Day 6 — Bear Creek Falls overlook:** US-550 bridge pullout ~2.9 mi S of Ouray (single source) — confirm in OnX/Gaia.
- **Day 3 — Park Creek Rd waypoints (Elwood Pass/Cabin/Alpine camps):** see the `day3-trail.png` map; the exact TrailsOffroad #380 trail in your app is the source of truth.
- **Your 4 dropped pins** (Medano camp 37.82401,-105.45907 · Horca 37.13094,-106.34928 · Canyonlands Overlook 38.404384,-109.708790 · Arch 38.710668,-109.729128) — taken straight from your Google Maps drops; kept as-is.

## Note on the Great Sand Dunes cluster
Online geocoders disagreed (several returned 37.79,-105.59, which is out in the dune field/Sand
Creek — clearly a bad park-centroid geocode). I used the NPS facility locations (~37.733–37.743,
-105.511) and NPS's "Piñon Flats is 1 mi north of the Visitor Center." Worth a 10-second satellite
glance to confirm the day-use lot pin.
