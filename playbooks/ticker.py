from render import ticker


class Ticker:
    def __init__(self, args):
        self.symbol = args[0] if len(args) > 0 else 'amd'

    def main(self):
        return ticker.generate_frame(self.symbol)
