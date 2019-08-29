from render import crypto


class Crypto:
    def __init__(self, args):
        self.symbol = args[0] if len(args) > 0 else 'bitcoin'

    def main(self):
        return crypto.generate_frame(self.symbol)
