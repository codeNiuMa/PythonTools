import os
from datetime import datetime
from ctypes import windll
from PIL import Image, ImageGrab
import pytesseract
import pyperclip
from time import sleep


# 清空剪贴板
def clear_clipboard():
    if windll.user32.OpenClipboard(None):  # 打开剪切板
        windll.user32.EmptyClipboard()  # 清空剪切板
        windll.user32.CloseClipboard()  # 关闭剪切板


def myORC():
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        img_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        path = './img/' + img_name
        im.save(path)
        print('已保存')
        text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
        # print(text, end='')
        # clear_clipboard()
        pyperclip.copy(text)  # 文字写入剪贴板
        os.remove(path)  # 删除临时照片
    else:
        print('剪贴板无图片')


def main():
    while True:
        myORC()
        sleep(2)


if __name__ == '__main__':
    main()
