#!/usr/bin/env python3
"""
Generate GPX tracks + waypoints for the Colorado Overland trip.
Output goes to the 'gpx files/' folder. Import into OnX Offroad / Gaia GPS.

Usage:  python3 make_gpx.py
"""
import os

OUT = "gpx files"
os.makedirs(OUT, exist_ok=True)

HEAD = ('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<gpx version="1.1" creator="Colorado Overland Guide" '
        'xmlns="http://www.topografix.com/GPX/1/1">\n')
FOOT = "</gpx>\n"


def wpt(lat, lon, name, desc=""):
    return (f'  <wpt lat="{lat}" lon="{lon}">\n'
            f'    <name>{name}</name>\n'
            + (f'    <desc>{desc}</desc>\n' if desc else "")
            + '  </wpt>\n')


def trk(name, pts):
    s = f'  <trk>\n    <name>{name}</name>\n    <trkseg>\n'
    for lat, lon in pts:
        s += f'      <trkpt lat="{lat}" lon="{lon}"></trkpt>\n'
    s += '    </trkseg>\n  </trk>\n'
    return s


def write(fname, waypoints, track_name, track_pts):
    body = HEAD
    for w in waypoints:
        body += wpt(*w)
    if track_pts:
        body += trk(track_name, track_pts)
    body += FOOT
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(body)
    print(f"  wrote {fname}  ({len(waypoints)} wpts, {len(track_pts)} trkpts)")


# ── Day 1: Medano Pass Road ─────────────────────────────────────────
write("01_Medano_Pass_Road.gpx",
    [(37.7339, -105.5117, "GRSA Visitor Center", "Road report + airdown info"),
     (37.7456, -105.5197, "Main Dunes Lot", "Dune access / Medano Creek"),
     (37.6233, -105.5503, "Zapata Falls TH", "0.9 mi RT waterfall slot"),
     (37.7385, -105.5106, "Pinon Flats CG", "Backup reservable campground"),
     (37.82401, -105.45907, "Medano Pass camp (pin)", "Your dispersed site pin")],
    "Medano Pass Primitive Road",
    [(37.7456, -105.5197), (37.78, -105.49), (37.82401, -105.45907), (37.8889, -105.43)])

# ── Day 2: Conejos / Park Creek ─────────────────────────────────────
write("02_Conejos_ParkCreek.gpx",
    [(37.13094, -106.34928, "Horca / FSR 250 (pin)", "Turn up the Conejos"),
     (37.348, -106.531, "Platoro", "Tiny village; seasonal fuel/food"),
     (37.356, -106.535, "Platoro Reservoir camp", "Night 2 - dispersed north shore"),
     (37.347, -106.548, "Mix Lake CG", "Sheltered backup, 22 sites"),
     (37.398, -106.585, "Stunner CG / Park Creek", "Toward Stunner Pass & FSR 380")],
    "Conejos FSR250 to Platoro Reservoir / Park Creek Rd 380",
    [(37.13094, -106.34928), (37.25, -106.46), (37.348, -106.531),
     (37.356, -106.535), (37.398, -106.585), (37.45, -106.62)])

# ── Day 4-6: Alpine Loop (clockwise) ────────────────────────────────
write("04_Alpine_Loop_clockwise.gpx",
    [(37.8119, -107.6645, "Silverton", "Fuel + supplies before the loop"),
     (37.7479, -107.6896, "Molas Lake", "MDH overlook"),
     (37.9289, -107.5722, "Animas Forks", "Ghost town hub"),
     (37.9722, -107.5447, "Engineer Pass", "12,800 ft - climb clockwise"),
     (38.0303, -107.3151, "Lake City", "Resupply / fuel"),
     (37.9356, -107.5036, "Cinnamon Pass", "12,640 ft"),
     (37.9258, -107.5044, "American Basin TH", "Handies Peak trailhead"),
     (37.9131, -107.5042, "Handies Peak", "14,058 ft summit"),
     (37.8089, -107.7717, "South Mineral dispersed", "Sheltered camp option")],
    "Alpine Loop clockwise",
    [(37.8119, -107.6645), (37.9289, -107.5722), (37.9722, -107.5447),
     (38.0303, -107.3151), (37.9356, -107.5036), (37.9258, -107.5044),
     (37.9289, -107.5722)])

# ── Day 6: Million Dollar Hwy (Silverton -> Ouray) ──────────────────
write("06_Million_Dollar_Hwy.gpx",
    [(37.8119, -107.6645, "Silverton", "Start north on US-550"),
     (37.8969, -107.7114, "Red Mountain Pass", "11,018 ft - mining ruins"),
     (37.9889, -107.6603, "Bear Creek Falls overlook", "Roadside 227-ft falls"),
     (38.0228, -107.6712, "Ouray", "Quality Inn / hot springs"),
     (38.0206, -107.6745, "Box Canon Falls", "285-ft slot falls")],
    "Million Dollar Highway Silverton to Ouray",
    [(37.8119, -107.6645), (37.8969, -107.7114), (37.9889, -107.6603),
     (38.0228, -107.6712)])

# ── Day 7-8: Rimrocker Trail ────────────────────────────────────────
write("07_Rimrocker_Trail.gpx",
    [(38.4783, -107.8762, "Montrose", "Full resupply + fuel"),
     (38.2678, -108.5462, "Nucla", "Small-town fuel"),
     (38.33, -108.88, "Paradox Valley Overlook", "Rim camp (scout)"),
     (38.27, -108.88, "Buckeye Reservoir", "Sheltered established camp"),
     (38.5733, -109.5498, "Moab", "Western end / resupply")],
    "Rimrocker Trail Montrose to Moab",
    [(38.4783, -107.8762), (38.2678, -108.5462), (38.33, -108.88),
     (38.27, -108.88), (38.45, -109.2), (38.5733, -109.5498)])

# ── Day 8: Moab rim camps ───────────────────────────────────────────
write("08_Moab_Rim_Camps.gpx",
    [(38.5733, -109.5498, "Moab", "Resupply / fuel"),
     (38.404384, -109.708790, "Canyonlands Overlook (pin)", "South rim camp - grand view"),
     (38.710668, -109.729128, "Arch/slickrock camp (pin)", "North rim camp - best for SLC AM")],
    "", [])

# ── Full trip overview ──────────────────────────────────────────────
write("00_Full_Trip_Overview.gpx",
    [(39.7392, -104.9903, "Denver START", "Day 1 depart"),
     (37.82401, -105.45907, "Medano Pass camp", "Night 1"),
     (37.356, -106.535, "Platoro Reservoir", "Night 2"),
     (37.2987, -107.8723, "Durango (Hampton)", "Night 3"),
     (37.95, -107.56, "Alpine Loop camp", "Nights 4-5"),
     (38.0228, -107.6712, "Ouray (Quality Inn)", "Night 6"),
     (38.33, -108.88, "Paradox rim", "Night 7"),
     (38.404384, -109.708790, "Moab rim camp", "Night 8"),
     (40.7608, -111.8910, "Salt Lake City FINISH", "Day 9 home")],
    "Colorado Overland - full route",
    [(39.7392, -104.9903), (37.82401, -105.45907), (37.13094, -106.34928),
     (37.398, -106.585), (37.2987, -107.8723), (37.8119, -107.6645),
     (37.9289, -107.5722), (38.0228, -107.6712), (38.4783, -107.8762),
     (38.33, -108.88), (38.5733, -109.5498), (38.404384, -109.708790),
     (40.7608, -111.8910)])

print("\nDone. GPX files are in the 'gpx files/' folder — import into OnX Offroad or Gaia GPS.")
