import requests
import re
import json


class Robinhood:
    def __init__(self):
        self.access = self.login()

    def login(self):
        try:
            response = requests.get('https://robinhood.com/crypto/BTC')
            m = re.search('window\.auth ?= ?(.*);', response.text)
            auth = json.loads(m.group(1))
            return auth['access_token']

        except Exception as e:
            print("Cannot get access token for robinhood crypto: " + str(e))

    def get_btc(self):
        try:
            response = requests.get(
                'https://api.robinhood.com/marketdata/forex/quotes/3d961844-d360-45fc-989b-f6fca761d511/',
                headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + self.access},
            )

            response_json = response.json()
            return response_json.get('mark_price')

        except Exception as e:
            print("Cannot get btc price: " + str(e))
