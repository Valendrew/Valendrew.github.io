"""Regenerate social preview cards with Python 3 and Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SCALE = 2
FONTS = Path('/usr/share/fonts/truetype/dejavu')

def card(filename, lines, subtitle, url):
    im = Image.new('RGB', (2400, 1260), '#f8f7f3')
    draw = ImageDraw.Draw(im)
    def text(x, y, value, size, color='#142337', bold=False):
        font = ImageFont.truetype(str(FONTS / ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')), size*SCALE)
        draw.text((x*SCALE, y*SCALE), value, font=font, fill=color, anchor='lt')
    text(88, 80, 'Andrea Valente', 30)
    for i, line in enumerate(lines):
        text(88, 186+i*78, line, 62, bold=True)
    text(88, 376, subtitle, 29, '#536174')
    draw.line((176, 954, 2224, 954), fill='#d3d9df', width=2)
    text(88, 519, url, 25, '#35608a')
    im.resize((1200, 630), Image.Resampling.LANCZOS).save(ROOT / 'assets' / filename, optimize=True)

card('portfolio-preview.png', ['Computer Vision', '& Applied ML'], 'Selected projects', 'valendrew.github.io')
card('cv-preview.png', ['Curriculum vitae'], 'Computer Vision & Applied ML', 'valendrew.github.io/cv')
