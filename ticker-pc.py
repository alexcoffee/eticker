import sys
from render import ticker


def main():
    image = ticker.generate_frame('BTC')
    image.show()


if "__main__" == __name__:
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass
