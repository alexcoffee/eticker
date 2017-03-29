import sys
import requests
import re
from HTMLParser import HTMLParser

EXCHANGES = ['SKLN', 'JNUG']
ST_BASE_URL = 'https://api.stocktwits.com/api/2/'


# ---------------------------------------------------------------------
# Basic StockTwits interface
# ---------------------------------------------------------------------

def get_watched_stocks(ticker):
    r = requests.get(ST_BASE_URL + 'streams/symbol/{}.json'.format(ticker))
    h = HTMLParser()

    messages = r.json()
    messages = messages['messages']

    for message in messages:
        name = message['user']['name'].encode('utf-8')
        text = message['body'].encode('utf-8')
        body = h.unescape(text)

        body = body.replace('$SKLN', '') if body.startswith("$SKLN") else body
        body = re.sub(r'https?:\/\/.*[\s?]', "[link] ", body, flags=re.MULTILINE)
        body = body.replace('\n', ' ')

        print("{:20.20}: {:.200}".format(name.strip(), body.strip()))


if "__main__" == __name__:
    try:
        get_watched_stocks("SKLN")
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass
