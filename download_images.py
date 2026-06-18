#!/usr/bin/env python3
"""
Fetch free, public-domain / CC landmark photos from Wikimedia Commons
into the images/ folder, named to match index.html (00.jpg cover,
01-09.jpg day banners).

It SEARCHES Commons for each term and grabs the top image result, so it
doesn't depend on exact filenames. Anything it can't find, just drop your
own photo in with the right name (see IMAGES.md for hand-picked sources).

Usage:  python3 download_images.py
Needs:  Python 3 standard library only.
Note:   Won't overwrite an image you've already placed.
"""
import os, time, json, urllib.request, urllib.parse

UA = 'ColoradoOverlandGuide/1.0 (personal trip planner; contact: bradnorman287@gmail.com)'

# slot -> (search term, thumbnail width)
SLOTS = [
    ("00", "San Juan Mountains Colorado autumn",        1400),  # cover
    ("01", "Great Sand Dunes National Park dunes",        1200),  # Day 1
    ("02", "Conejos River Colorado",                       1200),  # Day 2
    ("03", "Wolf Creek Pass Colorado",                     1200),  # Day 3
    ("04", "Animas Forks ghost town Colorado",             1200),  # Day 4
    ("05", "American Basin wildflowers Colorado",          1200),  # Day 5
    ("06", "Ouray Colorado town",                          1200),  # Day 6
    ("07", "Paradox Valley Colorado",                      1200),  # Day 7
    ("08", "Canyonlands Island in the Sky overlook",       1200),  # Day 8
    ("09", "Salt Lake City Wasatch mountains",             1200),  # Day 9
]


def search_first_file(term):
    """Return a File: title for the top image search hit on Commons."""
    params = urllib.parse.urlencode({
        'action': 'query', 'format': 'json',
        'generator': 'search', 'gsrsearch': term,
        'gsrnamespace': 6,        # File namespace
        'gsrlimit': 5,
        'prop': 'imageinfo', 'iiprop': 'url|mime', 'iiurlwidth': 1200,
    })
    url = 'https://commons.wikimedia.org/w/api.php?' + params
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        data = json.loads(r.read())
    pages = data.get('query', {}).get('pages', {})
    # pick the first JPEG/PNG with a thumburl
    for p in pages.values():
        ii = p.get('imageinfo', [{}])[0]
        mime = ii.get('mime', '')
        if ii.get('thumburl') and ('jpeg' in mime or 'png' in mime):
            return ii['thumburl']
    return None


def get_thumb(term, width):
    """Search then return a thumbnail URL at the requested width."""
    params = urllib.parse.urlencode({
        'action': 'query', 'format': 'json',
        'generator': 'search', 'gsrsearch': term,
        'gsrnamespace': 6, 'gsrlimit': 5,
        'prop': 'imageinfo', 'iiprop': 'url|mime', 'iiurlwidth': width,
    })
    url = 'https://commons.wikimedia.org/w/api.php?' + params
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        data = json.loads(r.read())
    pages = data.get('query', {}).get('pages', {})
    best = sorted(pages.values(), key=lambda p: p.get('index', 99))
    for p in best:
        ii = p.get('imageinfo', [{}])[0]
        mime = ii.get('mime', '')
        if ii.get('thumburl') and ('jpeg' in mime or 'png' in mime):
            return ii['thumburl']
    return None


def main():
    os.makedirs('images', exist_ok=True)
    ok = fail = skip = 0
    for slot, term, width in SLOTS:
        dest = f'images/{slot}.jpg'
        if os.path.exists(dest):
            print(f'  {slot}  exists — skipping')
            skip += 1
            continue
        try:
            thumb = get_thumb(term, width)
            if not thumb:
                raise RuntimeError('no image result')
            req = urllib.request.Request(thumb, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                img = r.read()
            with open(dest, 'wb') as f:
                f.write(img)
            print(f'  {slot}  OK  {len(img)//1024} KB  ({term})')
            ok += 1
        except Exception as e:
            print(f'  {slot}  FAIL  {e}  — add your own {dest} (see IMAGES.md)')
            fail += 1
        time.sleep(2)
    print(f'\nDone: {ok} downloaded, {skip} skipped, {fail} failed.')
    print('Review each image, replace any you do not like, then commit the images/ folder.')
    print('Day route maps (day1-map.png ... day9-map.png): screenshot Google Maps / OnX yourself.')


if __name__ == '__main__':
    main()
