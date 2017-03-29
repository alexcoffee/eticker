import sys
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from EPD import EPD
from yahoo_finance import Share

WHITE = 1
BLACK = 0
FONT_SIZE = 60
MAX_START = 0xffff
FONT_FILE_SMALL = '/usr/share/fonts/truetype/roboto/Roboto-Thin.ttf'
FONT_FILE = '/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf'


def main():
    ticker = 'JNUG'
    epd = EPD()
    epd.clear()

    print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version, g=epd.cog, f=epd.film))
    print_price(epd, ticker)


def print_price(epd, ticker):
    image = Image.new('1', epd.size, WHITE)
    draw = ImageDraw.Draw(image)
    width, height = image.size
    big_font = ImageFont.truetype(FONT_FILE, FONT_SIZE)
    small_font = ImageFont.truetype(FONT_FILE_SMALL, 20)

    price = Share(ticker)

    while 1:
        draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)
        price.refresh()

        # add vertical symbol name
        txt_ticker = '{}'.format(ticker)
        size_ticker = small_font.getsize(txt_ticker)
        img_txt = Image.new('1', (height, size_ticker[1]), WHITE)
        draw_txt = ImageDraw.Draw(img_txt)
        draw_txt.text((height / 2 - (size_ticker[0] / 2), -4), txt_ticker, font=small_font)
        img_txt = img_txt.rotate(90, expand=0)
        image.paste(img_txt, (0, 0, size_ticker[1], height))

        # print price
        txt_price = '{}'.format(price.get_price())
        size_price = big_font.getsize(txt_price)
        draw.text((width / 2 - size_price[0] / 2 + size_ticker[1] / 2, -5), txt_price, fill=BLACK, font=big_font)

        # print time
        txt_time = '{}'.format(time.strftime("%H:%M:%S %p", time.localtime()))
        size_time = small_font.getsize(txt_time)
        draw.text((width - size_time[0] + 1, height - size_time[1] - 2), txt_time, fill=BLACK, font=small_font)

        # divider
        draw.line([size_ticker[1], 0, size_ticker[1], height])

        epd.display(image)
        epd.partial_update()
        time.sleep(.5)


if "__main__" == __name__:
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass
