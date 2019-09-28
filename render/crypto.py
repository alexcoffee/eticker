import time
import requests

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

WHITE = 1
BLACK = 0
FONT_FILE_SMALL = 'fonts/Roboto-Thin.ttf'
FONT_FILE = 'fonts/Roboto-Bold.ttf'
SIZE = (200, 96)


def generate_frame(ticker, robinhood=None):
    image = Image.new('1', SIZE, WHITE)

    draw = ImageDraw.Draw(image)
    width, height = image.size

    big_font = ImageFont.truetype(FONT_FILE, 40)
    small_font = ImageFont.truetype(FONT_FILE_SMALL, 20)

    while 1:
        if robinhood is None:
            price = get_crypto_price(ticker)
        else:
            price = get_robin_price(robinhood)

        draw.rectangle((0, 0, width, height), fill=WHITE, outline=WHITE)

        # add vertical symbol name
        img_symbol = draw_symbol(ticker.upper())
        image.paste(img_symbol, (2, 0, img_symbol.width + 2, height))

        # print price
        txt_price = '${:0.0f}'.format(price) if isinstance(price, float) else price

        size_price = big_font.getsize(txt_price)
        x = width / 2 - size_price[0] / 2 + img_symbol.width / 2
        draw.text((x, 20), txt_price, fill=BLACK, font=big_font)

        # print time
        txt_time = '{}'.format(time.strftime("%_I:%M %p", time.localtime()))
        size_time = small_font.getsize(txt_time)
        draw.text((width - size_time[0] + 1, height - size_time[1] - 2), txt_time, fill=BLACK, font=small_font)

        # divider
        draw.line([img_symbol.width, 0, img_symbol.width, height])

        return image


def draw_symbol(name):
    txt_ticker = '{}'.format(name)
    small_font = ImageFont.truetype(FONT_FILE_SMALL, 20)
    height = SIZE[1]

    size_ticker = small_font.getsize(txt_ticker)
    img_txt = Image.new('1', (height, size_ticker[1]), WHITE)  # (width, height)

    draw_txt = ImageDraw.Draw(img_txt)
    draw_txt.text((height / 2 - (size_ticker[0] / 2), -4), txt_ticker, font=small_font)
    img_txt = img_txt.rotate(90, expand=1)

    return img_txt
    # dest_image.paste(img_txt, (0, 0, size_ticker[1], height))


def get_crypto_price(ticker):
    try:
        bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/' + ticker + '/'
        response = requests.get(bitcoin_api_url)
        response_json = response.json()

        return float(response_json[0].get('price_usd'))

    except:
        print("Cannot get crypto price for ", ticker)
        return "fail"


def get_robin_price(robinhood):
    try:
        return float(robinhood.get_btc())
    except:
        return "fail"
