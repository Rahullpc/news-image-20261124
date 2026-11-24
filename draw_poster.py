#!/usr/bin/env python3
"""Draw the news-image-20261124 poster: one front page summing up
Tuesday 24 November 2026 in eight stories plus a short also-today strip.

Written from scratch in-session (adapted layout from the 23 Nov edition).
Deterministic: no network, no clock, no randomness.
Output is a 1024x1024 PNG.
"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 229)
INK = (20, 20, 20)
RED = (176, 30, 36)
NAVY = (31, 56, 100)
GREEN = (31, 107, 58)
MUTED = (96, 89, 74)
TINT = (233, 226, 207)
RULE = (198, 188, 162)
ORANGE = (212, 104, 24)
GOLD = (214, 158, 32)

FD = "/usr/share/fonts/truetype"
SERIF_B = os.path.join(FD, "liberation/LiberationSerif-Bold.ttf")
SANS_B = os.path.join(FD, "liberation/LiberationSans-Bold.ttf")
SANS = os.path.join(FD, "liberation/LiberationSans-Regular.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def tracked(d, cx, y, text, f, fill, tr=4):
    w = sum(d.textlength(c, font=f) for c in text) + tr * (len(text) - 1)
    x = cx - w / 2
    for c in text:
        d.text((x, y), c, font=f, fill=fill)
        x += d.textlength(c, font=f) + tr


# ---------------------------------------------------------------- icons
def icon_globe(d, x0, y0, s, ink, accent):
    cx, cy, r = x0 + s / 2, y0 + s / 2, s / 2 - 6
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=ink, width=3)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r], outline=ink, width=2)
    d.line([cx - r, cy, cx + r, cy], fill=ink, width=2)
    d.line([cx - r * 0.82, cy - r * 0.55, cx + r * 0.82, cy - r * 0.55],
           fill=ink, width=2)
    d.line([cx - r * 0.82, cy + r * 0.55, cx + r * 0.82, cy + r * 0.55],
           fill=ink, width=2)
    d.line([(cx - r * 0.1, cy - r), (cx + r * 0.2, cy - r * 0.3),
            (cx - r * 0.15, cy), (cx + r * 0.25, cy + r * 0.35),
            (cx - r * 0.05, cy + r)], fill=accent, width=4)


def icon_radar(d, x0, y0, s, ink, accent):
    cx, cy = x0 + s / 2, y0 + s / 2
    for r in (s / 2 - 6, s / 2 - 22, s / 2 - 38):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=ink, width=2)
    d.line([cx, cy - s / 2 + 6, cx, cy + s / 2 - 6], fill=ink, width=2)
    d.line([cx - s / 2 + 6, cy, cx + s / 2 - 6, cy], fill=ink, width=2)
    d.line([(cx, cy), (cx + s * 0.34, cy - s * 0.34)], fill=accent, width=4)
    d.ellipse([cx + s * 0.22 - 6, cy - s * 0.22 - 6,
               cx + s * 0.22 + 6, cy - s * 0.22 + 6], fill=accent)


def icon_missile(d, x0, y0, s, ink, accent):
    p = 8
    d.polygon([(x0 + s - p - 14, y0 + p + 8), (x0 + s - p, y0 + p),
               (x0 + p + 22, y0 + s - p - 6), (x0 + p + 8, y0 + s - p - 20)],
              fill=ink)
    d.polygon([(x0 + p + 22, y0 + s - p - 6), (x0 + p + 8, y0 + s - p - 20),
               (x0 + p - 2, y0 + s - p - 2)], fill=accent)
    d.polygon([(x0 + p + 2, y0 + s - p - 14), (x0 + p + 14, y0 + s - p - 2),
               (x0 + p + 2, y0 + s - p - 2)], fill=ink)
    d.polygon([(x0 + p + 2, y0 + s - p - 2), (x0 + p - 8, y0 + s - p + 10),
               (x0 + p + 12, y0 + s - p + 4)], fill=ORANGE)


def icon_chart(d, x0, y0, s, ink, accent):
    p = 10
    d.line([(x0 + p, y0 + p + 6), (x0 + p, y0 + s - p)], fill=ink, width=3)
    d.line([(x0 + p, y0 + s - p), (x0 + s - p, y0 + s - p)], fill=ink, width=3)
    pts = [(x0 + p + 4, y0 + s - p - 8), (x0 + p + 20, y0 + s - p - 22),
           (x0 + p + 32, y0 + s - p - 18), (x0 + p + 46, y0 + p + 26),
           (x0 + s - p - 4, y0 + p + 6)]
    d.line(pts, fill=accent, width=4)
    d.polygon([(x0 + s - p - 4, y0 + p + 6), (x0 + s - p - 16, y0 + p + 8),
               (x0 + s - p - 6, y0 + p + 18)], fill=accent)


def icon_cuffs(d, x0, y0, s, ink, accent):
    c1 = (x0 + s * 0.32, y0 + s * 0.55)
    c2 = (x0 + s * 0.68, y0 + s * 0.55)
    r = 13
    for c in (c1, c2):
        d.ellipse([c[0] - r, c[1] - r, c[0] + r, c[1] + r],
                  outline=ink, width=4)
        d.ellipse([c[0] - 4, c[1] - 4, c[0] + 4, c[1] + 4], fill=accent)
    d.line([c1, c2], fill=ink, width=4)


def icon_drone(d, x0, y0, s, ink, accent):
    cx, cy = x0 + s / 2, y0 + s / 2
    d.rectangle([cx - 10, cy - 8, cx + 10, cy + 8], fill=ink)
    for sx, sy in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        d.line([(cx, cy), (cx + sx * 24, cy + sy * 24)], fill=ink, width=3)
        d.ellipse([cx + sx * 24 - 8, cy + sy * 24 - 8,
                   cx + sx * 24 + 8, cy + sy * 24 + 8],
                  outline=accent, width=3)


def icon_bolt(d, x0, y0, s, ink, accent):
    cx = x0 + s / 2
    d.polygon([(cx + 8, y0 + 8), (cx - 16, y0 + s * 0.55),
               (cx - 2, y0 + s * 0.55), (cx - 10, y0 + s - 8),
               (cx + 16, y0 + s * 0.45), (cx + 2, y0 + s * 0.45)],
              fill=accent)
    d.line([(x0 + 14, y0 + s - 12), (x0 + s - 14, y0 + s - 12)],
           fill=ink, width=3)


def icon_wave(d, x0, y0, s, ink, accent):
    for k, yy in enumerate((0.30, 0.50, 0.70)):
        y = y0 + s * yy
        pts = []
        for i in range(9):
            px = x0 + 12 + i * (s - 24) / 8
            py = y + (10 if i % 2 == 0 else -10)
            pts.append((px, py))
        d.line(pts, fill=accent if k == 1 else ink, width=4)


def icon_jet(d, x0, y0, s, ink, accent):
    cx = x0 + s / 2
    d.polygon([(cx, y0 + 10), (cx + 10, y0 + s - 22),
               (cx, y0 + s - 14), (cx - 10, y0 + s - 22)], fill=ink)
    d.polygon([(cx - 8, y0 + s * 0.55), (cx - s * 0.38, y0 + s - 14),
               (cx - 8, y0 + s - 18)], fill=ink)
    d.polygon([(cx + 8, y0 + s * 0.55), (cx + s * 0.38, y0 + s - 14),
               (cx + 8, y0 + s - 18)], fill=ink)
    d.polygon([(cx - 6, y0 + 22), (cx + 6, y0 + 22),
               (cx + 4, y0 + 40), (cx - 4, y0 + 40)], fill=accent)


def icon_flame(d, x0, y0, s, ink, accent):
    cx = x0 + s / 2
    d.polygon([(cx, y0 + 8), (cx + 20, y0 + 40), (cx + 16, y0 + s - 10),
               (cx - 16, y0 + s - 10), (cx - 20, y0 + 40)], fill=accent)
    d.polygon([(cx, y0 + 34), (cx + 9, y0 + 52), (cx + 7, y0 + s - 16),
               (cx - 7, y0 + s - 16), (cx - 9, y0 + 52)], fill=GOLD)


ICONS = {"globe": icon_globe, "radar": icon_radar,
         "missile": icon_missile, "chart": icon_chart,
         "cuffs": icon_cuffs, "drone": icon_drone,
         "bolt": icon_bolt, "wave": icon_wave, "jet": icon_jet,
         "flame": icon_flame}


# ---------------------------------------------------------------- stories
# (kicker, accent, headline, fact, icon)
STORIES = [
    ("WAR — UKRAINE", RED, "SEA DRONES HIT WARSHIP OFF LIBYA",
     "Drones strike a Russian warship at a Libyan base; a refinery burns in Russia.",
     "drone"),
    ("IRAN — U.S.", RED, "TRUMP: NEW IRAN STRIKES UNLIKELY",
     "Oil hits 3-month low; U.S. sanctions Iran's shadow banks.",
     "bolt"),
    ("MARKETS", NAVY, "ASIAN STOCKS SURGE ON AI TRADE",
     "Nikkei +4.5%, Kospi +7.5% as Huang's return revives the AI rally; Samsung +8%.",
     "chart"),
    ("MEXICO", NAVY, "EL CHAPO ISIDRO TO FACE MEXICAN TRIAL",
     "Mexico to prosecute the cartel boss at home, defying a U.S. extradition request.",
     "cuffs"),
    ("GAZA", RED, "AIRSTRIKE KILLS 3 AT GAZA POLICE POST",
     "At least 3 dead, 5 wounded near a police post in Khan Younis.",
     "missile"),
    ("INDONESIA", RED, "24 DEAD, 30 MISSING IN FACTORY FIRE",
     "Search goes on at Java candy plant; DNA tests to name victims.",
     "flame"),
]


def draw_panel(d, x, y, w, h, story):
    kicker, accent, headline, fact, icon = story
    isz = 76
    d.rectangle([x, y, x + isz, y + isz], fill=TINT, outline=RULE, width=1)
    ICONS[icon](d, x, y, isz, INK, accent)
    tx = x + isz + 14
    tw = x + w - tx
    fk = font(SANS_B, 15)
    fh = font(SANS_B, 25)
    ff = font(SANS, 19)
    d.text((tx, y + 2), kicker, font=fk, fill=accent)
    hl = wrap(d, headline, fh, tw)
    yy = y + 24
    for ln in hl[:2]:
        d.text((tx, yy), ln, font=fh, fill=INK)
        yy += 30
    fl = wrap(d, fact, ff, tw)
    yy += 2
    for ln in fl[:2]:
        d.text((tx, yy), ln, font=ff, fill=INK)
        yy += 23


def draw():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # outer border
    d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=3)
    d.rectangle([16, 16, W - 17, H - 17], outline=RULE, width=1)

    # ---- masthead
    fm = font(SERIF_B, 92)
    d.text((W / 2, 28), "THE WORLD", font=fm, fill=INK, anchor="ma")
    fd = font(SANS_B, 23)
    tracked(d, W / 2, 128, "TUESDAY, 24 NOVEMBER 2026", fd, INK, tr=5)
    d.rectangle([28, 160, W - 28, 165], fill=RED)
    fs = font(SANS_B, 15)
    tracked(d, W / 2, 174, "THE DAY'S WORLD NEWS — IN ONE PAGE", fs, MUTED, tr=3)

    # ---- lead story: Poland / NATO airspace
    ly = 204
    fk = font(SANS_B, 17)
    d.text((28, ly), "NATO — POLAND", font=fk, fill=RED)
    fh = font(SERIF_B, 42)
    d.text((28, ly + 26), "RUSSIAN DRONE", font=fh, fill=INK)
    d.text((28, ly + 72), "IN NATO AIRSPACE", font=fh, fill=INK)
    ff = font(SANS, 19)
    fact = ("Shoot-down authorised, then held; "
            "NATO sends AWACS to Poland.")
    fl = wrap(d, fact, ff, 676)
    yy = ly + 124
    for ln in fl[:2]:
        d.text((28, yy), ln, font=ff, fill=INK)
        yy += 25
    # lead radar, right side
    gx, gy, gs = 716, ly - 6, 148
    d.rectangle([gx, gy, gx + gs, gy + gs], fill=TINT, outline=RULE, width=1)
    icon_radar(d, gx, gy, gs, INK, RED)

    # ---- grid 2 x 3
    gy0 = 372
    row_h, gap = 170, 8
    col_w = 468
    d.line([(28, gy0 - 12), (W - 28, gy0 - 12)], fill=RULE, width=1)
    for i, story in enumerate(STORIES):
        r, c = divmod(i, 2)
        x = 28 + c * (col_w + 32)
        y = gy0 + r * (row_h + gap)
        draw_panel(d, x, y, col_w, row_h, story)
    d.line([(512, gy0), (512, gy0 + 3 * row_h + 2 * gap)], fill=RULE, width=1)
    d.line([(28, gy0 + row_h + 4), (W - 28, gy0 + row_h + 4)],
           fill=RULE, width=1)
    d.line([(28, gy0 + 2 * row_h + 12), (W - 28, gy0 + 2 * row_h + 12)],
           fill=RULE, width=1)

    # ---- bottom band: South Korea + also today
    by = 898
    d.line([(28, by - 10), (W - 28, by - 10)], fill=INK, width=2)
    korea = ("S. KOREA", RED, "RUSSIAN JETS ENTER DEFENCE ZONE",
             "Jets scramble as Russian planes enter defence zone.",
             "jet")
    draw_panel(d, 28, by, 580, 96, korea)
    ax = 648
    d.line([(ax - 20, by), (ax - 20, by + 92)], fill=RULE, width=1)
    fa = font(SANS_B, 16)
    d.text((ax, by + 2), "ALSO TODAY", font=fa, fill=RED)
    fi = font(SANS, 17)
    fb = font(SANS_B, 17)
    also = [("EU — ", "22nd Russia sanctions proposed"),
            ("UN — ", "Guterres seeks global AI rules"),
            ("SPORT — ", "NZ hold India to Wellington draw")]
    yy = by + 26
    for lead, rest in also:
        d.text((ax, yy), lead, font=fb, fill=INK)
        wlead = d.textlength(lead, font=fb)
        d.text((ax + wlead, yy), rest, font=fi, fill=INK)
        yy += 23

    # ---- footer
    d.text((W / 2, 996), "All events reported on Tuesday, 24 November 2026. "
           "Sources: wire reports.", font=font(SANS, 12), fill=MUTED,
           anchor="ma")
    return img


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    img = draw()
    img.save(out, "PNG", optimize=True)
    print(out, img.size)


if __name__ == "__main__":
    main()
