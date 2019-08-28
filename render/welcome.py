import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

WHITE = 1
BLACK = 0
FONT_FILE_SMALL = 'fonts/Roboto-Thin.ttf'
FONT_FILE = 'fonts/Roboto-Bold.ttf'
SIZE = (200, 96)


def generate_frame():
    image = Image.new('1', SIZE, WHITE)
    draw = ImageDraw.Draw(image)
    width, height = image.size

    big_font = ImageFont.truetype(FONT_FILE, 40)
    small_font = ImageFont.truetype(FONT_FILE_SMALL, 20)

    draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)

    # print welcome message
    txt_banner = 'eTicker'
    size_banner = big_font.getsize(txt_banner)
    draw.text((width / 2 - size_banner[0] / 2, -5), txt_banner, fill=BLACK, font=big_font)

    # print time
    txt_time = '{}'.format(time.strftime("%H:%M:%S %p", time.localtime()))
    size_time = small_font.getsize(txt_time)
    draw.text((width - size_time[0] + 1, height - size_time[1] - 2), txt_time, fill=BLACK, font=small_font)

    return image
