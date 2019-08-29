import sys
from render import ticker


def main():
    symbol = sys.argv[1] if len(sys.argv) == 2 else 'LK'

    image = ticker.generate_frame(symbol)
    image.show()


if "__main__" == __name__:
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass
