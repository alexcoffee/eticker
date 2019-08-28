import sys
from render import welcome


def main():
    image = welcome.generate_frame()
    image.show()


if "__main__" == __name__:
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass
