from render import wash


class Wash:
    def __init__(self, args):
        self.args = args

    def main(self):
        return wash.generate_frame()
