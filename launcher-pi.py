import sys
import time
from render import welcome
from papirus import Papirus


def main():
    image = welcome.generate_frame()

    screen = Papirus()
    screen.clear()

    print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=screen.panel, w=screen.width, h=screen.height, v=screen.version, g=screen.cog, f=screen.film))

    screen.display(image)
    screen.partial_update()
    time.sleep(.5)


if "__main__" == __name__:
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass
