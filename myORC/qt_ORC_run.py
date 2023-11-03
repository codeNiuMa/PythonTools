import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
import os
from datetime import datetime
from PIL import Image, ImageGrab
import pytesseract
import pyperclip
import Baidu_Text_transAPI as baidu



class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("./test.ui")
        self.text = self.ui.textEdit

        self.ui.pushButton_orc.clicked.connect(self.orc)
        self.ui.pushButton_copy.clicked.connect(self.copy)
        self.ui.pushButton_clear.clicked.connect(self.text.clear)
        self.ui.pushButton_trans.clicked.connect(self.trans)
        self.ui.pushButton_enter.clicked.connect(self.fmt)




    def orc(self):
        im = ImageGrab.grabclipboard()
        if isinstance(im, Image.Image):
            img_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
            path = './' + img_name
            im.save(path)  # 把剪贴板图片保存到这个路径
            print('已保存')
            # 旧的识别模型
            data = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
            puredata = data.strip('\n')
            # print(text, end='')
            # clear_clipboard()
            self.text.clear()  # 清空原内容
            self.text.setText(puredata)
            # pyperclip.copy(data)  # 文字写入剪贴板
            os.remove(path)  # 删除临时照片
        else:
            self.text.clear()
            self.text.append('\n剪贴板无图片')

    def copy(self):
        data = self.text.toPlainText()
        data = data.replace('=== 复制成功 ===', '')
        self.text.setText(data.strip())
        pyperclip.copy(data)  # 文字写入剪贴板
        self.text.append('=== 复制成功 ===')

    def trans(self):
        yuan = self.text.toPlainText()
        baidu.query = yuan
        fanyi_list = baidu.main()  # 返回是个列表，需要转成几行字符串
        fanyi = ''
        for i in range(0, len(fanyi_list)):
            fanyi += fanyi_list[i] + '\n'
        self.text.append('=======百度翻译=======\n' + fanyi)

    def fmt(self):
        data = self.text.toPlainText()
        if self.ui.select_blank.isChecked() is True:
            data = data.replace(' ', '')
            self.ui.select_blank.setChecked(False)
        data = data.replace('\n', '')
        self.text.clear()  # 清空原内容
        self.text.append(data)





app = QApplication(sys.argv)
s = Stats()
s.ui.show()
app.exec_()
