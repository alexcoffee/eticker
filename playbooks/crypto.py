from render import crypto
from services.robinhood import Robinhood

class Crypto:
    def __init__(self, args):
        self.symbol = args[0] if len(args) > 0 else 'bitcoin'
        self.robinhood = Robinhood()

    def main(self):
        return crypto.generate_frame(self.symbol, self.robinhood)
