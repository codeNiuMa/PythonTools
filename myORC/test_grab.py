from datetime import datetime

from PIL import Image, ImageGrab
import pytesseract


def get_file_name():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'


def paste_pic():
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        im.save('./pic.jpg')


if __name__ == '__main__':
    paste_pic()

