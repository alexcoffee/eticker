import sys
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from EPD import EPD

WHITE = 1
BLACK = 0
FONT_SIZE = 40
FONT_FILE_SMALL = '/usr/share/fonts/truetype/roboto/Roboto-Thin.ttf'
FONT_FILE = '/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf'


def main():
    epd = EPD()
    epd.clear()

    print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version, g=epd.cog, f=epd.film))
    welcome(epd)


def welcome(epd):
    image = Image.new('1', epd.size, WHITE)
    draw = ImageDraw.Draw(image)
    width, height = image.size
    big_font = ImageFont.truetype(FONT_FILE, FONT_SIZE)
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

    epd.display(image)
    epd.partial_update()


if "__main__" == __name__:
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass
