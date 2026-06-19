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
    [(37.7337, -105.5107, "GRSA Visitor Center", "Road report + airdown info"),
     (37.7356, -105.5108, "Main Dunes Lot", "Dune access / Medano Creek"),
     (37.6216, -105.5595, "Zapata Falls TH", "0.9 mi RT waterfall slot"),
     (37.7426, -105.5110, "Pinon Flats CG", "Backup reservable campground"),
     (37.82401, -105.45907, "Medano Pass camp (pin)", "Your dispersed site pin")],
    "Medano Pass Primitive Road",
    [(37.7356, -105.5108), (37.78, -105.49), (37.82401, -105.45907), (37.8889, -105.43)])

# ── Day 2: Conejos / Park Creek ─────────────────────────────────────
write("02_Conejos_ParkCreek.gpx",
    [(37.13094, -106.34928, "Horca / FSR 250 (pin)", "Turn up the Conejos"),
     (37.348, -106.531, "Platoro", "Tiny village; seasonal fuel/food"),
     (37.356, -106.535, "Platoro Reservoir camp", "Night 2 - dispersed north shore"),
     (37.3583, -106.5381, "Mix Lake CG", "Sheltered backup, 22 sites"),
     (37.398, -106.585, "Stunner CG / Park Creek", "Toward Stunner Pass & FSR 380")],
    "Conejos FSR250 to Platoro Reservoir",
    [(37.13094, -106.34928), (37.25, -106.46), (37.348, -106.531),
     (37.356, -106.535)])

# ── Day 3: Park Creek Rd (FSR 380) over Elwood Pass ─────────────────
# Coords approximate (TrailsOffroad #380); verify in OnX/Gaia.
write("03_Park_Creek_Rd.gpx",
    [(37.356, -106.535, "Platoro Reservoir camp", "Day 3 start"),
     (37.398, -106.585, "Stunner Camp / FSR250 jct", "5 sites, toilet; pick up FSR 380"),
     (37.47, -106.61, "Elwood Pass (approx)", "High point 11,631 ft; East Fork Rd spur"),
     (37.50, -106.66, "Elwood Cabin (approx)", "Reservable 1911 cabin, Schinzel Flats"),
     (37.55, -106.70, "Alpine/Mountain View camps", "Approx; high meadow sites"),
     (37.585, -106.745, "Hwy 160 Trailhead (approx)", "North end SW of South Fork")],
    "Park Creek Rd FSR 380 Stunner to Hwy 160",
    [(37.356, -106.535), (37.398, -106.585), (37.47, -106.61),
     (37.50, -106.66), (37.55, -106.70), (37.585, -106.745)])

# ── Day 4-6: Alpine Loop (clockwise) ────────────────────────────────
write("04_Alpine_Loop_clockwise.gpx",
    [(37.8119, -107.6645, "Silverton", "Fuel + supplies before the loop"),
     (37.7475, -107.6832, "Molas Lake", "MDH overlook"),
     (37.9311, -107.5715, "Animas Forks", "Ghost town hub"),
     (37.9756, -107.5845, "Engineer Pass", "12,800 ft - climb clockwise"),
     (38.0303, -107.3151, "Lake City", "Resupply / fuel"),
     (37.9339, -107.5378, "Cinnamon Pass", "12,640 ft"),
     (37.9203, -107.5164, "American Basin TH", "Handies Peak trailhead"),
     (37.9131, -107.5042, "Handies Peak", "14,058 ft summit"),
     (37.8061, -107.7742, "South Mineral dispersed", "Sheltered camp option")],
    "Alpine Loop clockwise",
    # Silverton -> Animas Forks -> Engineer -> Lake City -> American Basin -> Cinnamon -> Animas Forks
    [(37.8119, -107.6645), (37.9311, -107.5715), (37.9756, -107.5845),
     (38.0303, -107.3151), (37.9203, -107.5164), (37.9339, -107.5378),
     (37.9311, -107.5715)])

# ── Day 6: Million Dollar Hwy (Silverton -> Ouray) ──────────────────
write("06_Million_Dollar_Hwy.gpx",
    [(37.8119, -107.6645, "Silverton", "Start north on US-550"),
     (37.8989, -107.7120, "Red Mountain Pass", "11,018 ft - mining ruins"),
     (37.9889, -107.6603, "Bear Creek Falls overlook", "Roadside 227-ft falls"),
     (38.0228, -107.6712, "Ouray", "Quality Inn / hot springs"),
     (38.0195, -107.6769, "Box Canon Falls", "285-ft slot falls")],
    "Million Dollar Highway Silverton to Ouray",
    [(37.8119, -107.6645), (37.8989, -107.7120), (37.9889, -107.6603),
     (38.0228, -107.6712)])

# ── Day 7-8: Rimrocker Trail ────────────────────────────────────────
write("07_Rimrocker_Trail.gpx",
    [(38.4783, -107.8762, "Montrose", "Resupply + fuel before trail"),
     (38.47, -107.95, "Dry Creek TH (approx)", "Rimrocker mi 0 - air down"),
     (38.2678, -108.5462, "Nucla", "NO gas station - fuel in Naturita (CO-97)"),
     (38.33, -108.88, "Epic Campsite (mi 98.6)", "Night 7 - Paradox rim (scout)"),
     (38.27, -108.88, "Buckeye Reservoir (mi 107)", "DESIGNATED sites only - fills fast"),
     (38.5733, -109.5498, "Moab (mi 160.7)", "Trail ends south side of town")],
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
     (37.9311, -107.5715), (38.0228, -107.6712), (38.4783, -107.8762),
     (38.33, -108.88), (38.5733, -109.5498), (38.404384, -109.708790),
     (40.7608, -111.8910)])

print("\nDone. GPX files are in the 'gpx files/' folder — import into OnX Offroad or Gaia GPS.")
