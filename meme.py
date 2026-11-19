from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 1536, 960
INK = (20, 8, 40)
bone = (238, 232, 216)
outline = (30, 26, 30)
img = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)


def gradient_color(y):
    stops = [
        (0, (38, 16, 84)),
        (300, (150, 32, 130)),
        (480, (232, 74, 127)),
        (640, (255, 150, 66)),
    ]
    for index in range(len(stops) - 1):
        start_y, start_color = stops[index]
        end_y, end_color = stops[index + 1]
        if y <= end_y:
            fraction = (y - start_y) / (end_y - start_y)
            return tuple(round(a + (b - a) * fraction) for a, b in zip(start_color, end_color))
    return stops[-1][1]


for y in range(640):
    draw.line((0, y, WIDTH, y), fill=gradient_color(y))

draw.ellipse((280, 460, 580, 760), fill=(255, 214, 120), outline=(255, 140, 60), width=6)

building_specs = [
    (0, 535, 76), (74, 500, 82), (156, 526, 64), (220, 480, 91),
    (311, 520, 75), (386, 492, 88), (474, 545, 70), (544, 505, 92),
    (636, 476, 83), (719, 520, 74), (793, 488, 105), (898, 532, 68),
    (966, 500, 82), (1048, 540, 72), (1120, 490, 95), (1215, 515, 84),
    (1299, 475, 93), (1392, 525, 74), (1466, 500, 70),
]
for x, top, width in building_specs:
    draw.rectangle((x, top, min(x + width, WIDTH), 640), fill=(24, 10, 48))

window_positions = [
    (16, 550), (38, 574), (92, 520), (122, 546), (172, 550), (198, 572),
    (236, 500), (267, 526), (285, 552), (328, 540), (357, 566), (402, 514),
    (437, 540), (495, 562), (518, 530), (559, 526), (590, 551), (650, 497),
    (680, 525), (700, 551), (735, 543), (765, 568), (808, 510), (838, 538),
    (870, 558), (912, 550), (943, 575), (979, 524), (1008, 552), (1060, 558),
    (1088, 582), (1140, 514), (1170, 540), (1233, 540), (1264, 565), (1318, 500),
    (1348, 528), (1410, 550), (1438, 574), (1480, 524),
]
for x, y in window_positions:
    draw.rectangle((x, y, x + 4, y + 6), fill=(255, 220, 130))

draw.rectangle((0, 640, WIDTH, 740), fill=(18, 90, 120))
streaks = [
    (80, 660, 230), (310, 680, 145), (520, 653, 215), (760, 697, 180),
    (1010, 670, 250), (1310, 710, 160), (190, 722, 190), (430, 705, 120),
    (620, 675, 140), (880, 655, 200), (1080, 724, 180), (1260, 682, 130),
    (20, 690, 115), (690, 730, 230),
]
for x, y, length in streaks:
    draw.line((x, y, x + length, y), fill=(90, 200, 220), width=3)

draw.rectangle((0, 740, WIDTH, 960), fill=(233, 196, 138))
draw.rectangle((0, 880, WIDTH, 960), fill=(214, 170, 110))


def draw_palm(points, crown, left=True):
    for start, end in zip(points, points[1:]):
        draw.line((start, end), fill=INK, width=26)
    cx, cy = crown
    if left:
        tips = [(-150, -110), (-132, -165), (-75, -205), (-10, -190), (52, -155), (105, -100), (144, -37)]
    else:
        tips = [(150, -105), (132, -165), (75, -205), (10, -190), (-52, -155), (-105, -100), (-144, -37)]
    for dx, dy in tips:
        mid = (cx + dx * 0.48, cy + dy * 0.58)
        draw.line((crown, mid, (cx + dx, cy + dy)), fill=INK, width=12, joint="curve")


draw_palm([(95, 960), (112, 790), (130, 625), (150, 430)], (150, 430), True)
draw_palm([(1445, 960), (1428, 790), (1410, 625), (1395, 415)], (1395, 415), False)

draw.rectangle((1120, 470, 1475, 645), fill=(30, 14, 58))
stripe_count = 10
stripe_width = 385 / stripe_count
for index in range(stripe_count):
    x0 = 1105 + index * stripe_width
    x1 = x0 + stripe_width + 1
    stripe_color = (90, 20, 90) if index % 2 == 0 else (200, 60, 140)
    draw.polygon([(x0, 440), (x1, 440), (x1 - 4, 478), (x0 + 4, 478)], fill=stripe_color)

draw.rounded_rectangle((1150, 495, 1445, 575), radius=14, fill=(16, 8, 36), outline=(255, 60, 190), width=5)
sign_font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf", 64)
sign_text = "make.fun"
sign_box = draw.textbbox((0, 0), sign_text, font=sign_font, stroke_width=6)
sign_x = (1150 + 1445 - (sign_box[2] - sign_box[0])) // 2
sign_y = (495 + 575 - (sign_box[3] - sign_box[1])) // 2 - sign_box[1]
for color, stroke in [((255, 60, 190), 6), ((255, 120, 220), 3), ((255, 205, 245), 1)]:
    draw.text((sign_x, sign_y), sign_text, font=sign_font, fill=color, stroke_width=stroke, stroke_fill=color)

draw.ellipse((285, 845, 915, 905), fill=(190, 150, 95))
draw.rounded_rectangle((300, 655, 900, 800), radius=36, fill=(13, 102, 114), outline=(6, 60, 68), width=6)
draw.rounded_rectangle((320, 770, 595, 845), radius=20, fill=(17, 122, 134), outline=(6, 60, 68), width=4)
draw.rounded_rectangle((605, 770, 880, 845), radius=20, fill=(17, 122, 134), outline=(6, 60, 68), width=4)
draw.rounded_rectangle((285, 715, 345, 855), radius=20, fill=(10, 84, 94), outline=(6, 60, 68), width=5)
draw.rounded_rectangle((855, 715, 915, 855), radius=20, fill=(10, 84, 94), outline=(6, 60, 68), width=5)

draw.ellipse((415, 455, 540, 590), fill=bone, outline=outline, width=7)
draw.rounded_rectangle((440, 565, 515, 625), radius=10, fill=bone, outline=outline, width=6)
draw.ellipse((442, 505, 472, 545), fill=(5, 5, 8))
draw.ellipse((488, 505, 518, 545), fill=(5, 5, 8))
draw.polygon([(472, 545), (492, 545), (482, 568)], fill=(5, 5, 8))
for tooth_x in (453, 468, 483, 498):
    draw.line((tooth_x, 584, tooth_x, 614), fill=outline, width=4)

draw.line((478, 625, 478, 720), fill=bone, width=14)
for bounds in [(415, 630, 545, 690), (410, 655, 550, 715), (415, 680, 545, 740), (425, 705, 535, 760)]:
    draw.arc(bounds, start=0, end=180, fill=bone, width=9)
draw.ellipse((435, 735, 525, 775), fill=bone, outline=outline, width=4)

draw.line((520, 650, 575, 720), fill=bone, width=13)
draw.line((575, 720, 610, 775), fill=bone, width=13)
draw.line((445, 655, 585, 782), fill=bone, width=13)
draw.line((455, 770, 620, 800), fill=bone, width=14)
draw.line((505, 775, 655, 805), fill=bone, width=14)
draw.line((620, 800, 625, 875), fill=bone, width=12)
draw.line((655, 805, 660, 878), fill=bone, width=12)
draw.ellipse((606, 864, 644, 886), fill=bone, outline=outline, width=3)
draw.ellipse((641, 867, 679, 889), fill=bone, outline=outline, width=3)

web_color = (205, 205, 215)
web_lines = [((310, 665), (335, 660)), ((310, 665), (380, 657)), ((310, 665), (425, 660)), ((310, 665), (335, 720)), ((310, 665), (315, 780))]
for start, end in web_lines:
    draw.line((start, end), fill=web_color, width=3)
for bounds in [(316, 657, 370, 683), (326, 657, 405, 696), (337, 658, 430, 710)]:
    draw.arc(bounds, start=180, end=280, fill=web_color, width=3)
for end in [(450, 470), (478, 460), (510, 472)]:
    draw.line(((450, 460), end), fill=web_color, width=3)

draw.rounded_rectangle((560, 748, 690, 806), radius=16, fill=(32, 32, 42), outline=(10, 10, 14), width=5)
draw.rectangle((580, 766, 606, 792), fill=(120, 120, 135))
draw.rectangle((589, 759, 597, 799), fill=(120, 120, 135))
draw.ellipse((610, 758, 634, 782), fill=(230, 60, 160))
draw.ellipse((640, 770, 664, 794), fill=(50, 200, 190))


def ghost_path():
    points = []
    for step in range(37):
        angle = 180 - step * 5
        import math
        radians = math.radians(angle)
        points.append((1107 + 105 * math.cos(radians), 640 - 95 * math.sin(radians)))
    points.extend([(1212, 800)])
    for scallop in range(3):
        right = 1212 - scallop * 70
        left = right - 70
        for step in range(1, 13):
            fraction = step / 12
            x = right + (left - right) * fraction
            y = 800 + 35 * math.sin(math.pi * fraction)
            points.append((x, y))
    points.append((1002, 640))
    return points


ghost = ghost_path()
draw.polygon(ghost, fill=(10, 10, 14))
center = (1107, 690)
inner_ghost = [(center[0] + (x - center[0]) * 0.94, center[1] + (y - center[1]) * 0.94) for x, y in ghost]
draw.polygon(inner_ghost, fill=(238, 248, 250))


def sparkle(cx, cy, outer_vertical=30, outer_horizontal=13, inner=9):
    points = []
    for index in range(8):
        angle = 90 - index * 45
        import math
        radius = outer_vertical if index % 2 == 0 else inner
        if angle % 180 == 0:
            radius = outer_horizontal if index % 2 == 0 else inner
        radians = math.radians(angle)
        points.append((cx + math.cos(radians) * radius, cy - math.sin(radians) * radius))
    return points


draw.polygon(sparkle(1062, 645), fill=(10, 10, 14))
draw.polygon(sparkle(1152, 645), fill=(10, 10, 14))
draw.ellipse((971, 688, 1025, 742), fill=(238, 248, 250), outline=(10, 10, 14), width=8)
draw.ellipse((1142, 677, 1258, 793), fill=(228, 0, 138), outline=(150, 0, 90), width=8)
draw.polygon(sparkle(1200, 735, 30, 30, 13), fill=(255, 255, 255))

for center_x, count in [(1268, 5), (1352, 8), (1432, 4)]:
    for coin_index in range(count):
        top = 872 - coin_index * 11
        draw.ellipse((center_x - 32, top, center_x + 32, top + 16), fill=(246, 192, 64), outline=(176, 128, 22), width=3)
draw.ellipse((1268, 834, 1332, 850), fill=(230, 40, 150), outline=(150, 0, 90), width=3)
draw.ellipse((1294, 847, 1358, 863), fill=(230, 40, 150), outline=(150, 0, 90), width=3)

caption_font_path = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"


def fitting_font(text, start_size, max_width):
    size = start_size
    while size > 1:
        font = ImageFont.truetype(caption_font_path, size)
        box = draw.textbbox((0, 0), text, font=font, stroke_width=8)
        if box[2] - box[0] <= max_width:
            return font
        size -= 1
    return ImageFont.truetype(caption_font_path, 1)


def caption(text, start_size, top):
    font = fitting_font(text, start_size, 1456)
    box = draw.textbbox((0, 0), text, font=font, stroke_width=8)
    x = (WIDTH - (box[2] - box[0])) // 2 - box[0]
    y = top - box[1]
    draw.text((x, y), text, font=font, fill=(255, 255, 255), stroke_width=8, stroke_fill=(8, 8, 12))


caption("WAITING FOR GTA VI SINCE 2013", 96, 30)
caption("MY AI AGENT GOT PAID ON make.fun IN WEEK ONE", 68, 884)

img.save("meme.png")
print(f"{len(open('meme.png', 'rb').read())} bytes")
