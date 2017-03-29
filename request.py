import os
import logging as log
import json
import requests

# StockTwits details
ST_BASE_URL = 'https://api.stocktwits.com/api/2/'
ST_BASE_PARAMS = dict(access_token=os.getenv('ST_ACCESS_TOKEN'))

class Requests():
    def get_json(url, params=None):

        resp = None
        for i in range(4):
            try:
                resp = requests.get(url, params=params, timeout=5)
            except requests.Timeout:
                trimmed_params = {k: v for k, v in params.iteritems() if k not in ST_BASE_PARAMS.keys()}
                log.error('GET Timeout to {} w/ {}'.format(url[len(ST_BASE_URL):], trimmed_params))
            if resp is not None:
                break
        if resp is None:
            log.error('GET loop Timeout')
            return None
        else:
            return json.loads(resp.content)

    def post_json(url, params=None, deadline=30):
        """ Tries to post a couple times in a loop before giving up if a timeout.
        """
        resp = None
        for i in range(4):
            try:
                resp = requests.post(url, params=params, timeout=5)
            except requests.Timeout:
                trimmed_params = {k: v for k, v in params.iteritems() if k not in ST_BASE_PARAMS.keys()}
                log.error('POST Timeout to {} w/ {}'.format(url[len(ST_BASE_URL):], trimmed_params))
            if resp is not None:
                break
        # TODO wrap in appropriate try/except
        return json.loads(resp.content)
