from render import welcome


class Welcome:
    def __init__(self, args):
        self.args = args

    def main(self):
        return welcome.generate_frame()
