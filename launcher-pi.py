import sys
import time
from render import welcome
from EPD import EPD


def main():
    image = welcome.generate_frame()

    epd = EPD()
    epd.clear()
    print('panel = {p:s} {w:d} x {h:d}  version={v:s} COG={g:d} FILM={f:d}'.format(p=epd.panel, w=epd.width, h=epd.height, v=epd.version, g=epd.cog, f=epd.film))

    epd.display(image)
    epd.partial_update()
    time.sleep(.5)


if "__main__" == __name__:
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('interrupted')
        pass
