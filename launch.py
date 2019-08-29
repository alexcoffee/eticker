import sys
import time
import os
from playbooks import *


def main():
    playbook = sys.argv[1] if len(sys.argv) > 1 else 'welcome'
    args = sys.argv[2:] if len(sys.argv) > 2 else []

    playbooks = {
        'ticker': Ticker,
        'welcome': Welcome,
        'crypto': Crypto
    }

    klass = playbooks.get(playbook, Welcome)
    image = klass(args).main()

    if is_running_on_pi():
        paper(image)
    else:
        show(image)


def is_running_on_pi():
    return os.path.exists('/dev/epd')


def show(image):
    image.show()


def paper(image):
    from papirus import Papirus

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
