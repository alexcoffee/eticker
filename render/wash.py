from PIL import Image
from PIL import ImageDraw

WHITE = 1
BLACK = 0
FONT_FILE_SMALL = 'fonts/Roboto-Thin.ttf'
FONT_FILE = 'fonts/Roboto-Bold.ttf'
SIZE = (200, 96)


def generate_frame():
    image = Image.new('1', SIZE, BLACK)
    draw = ImageDraw.Draw(image)
    width, height = image.size

    draw.rectangle((0, 0, width, height), fill=BLACK, outline=WHITE)

    return image
