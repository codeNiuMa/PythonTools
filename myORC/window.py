import tkinter
import os
from datetime import datetime
from PIL import Image, ImageGrab
import pytesseract
import pyperclip
import Baidu_Text_transAPI as baidu
import PyQt5




# 窗体设置
win = tkinter.Tk()  # 构造窗体
win.title('文字识别')
win.geometry('700x450')
f = tkinter.Frame(win)

# 文本框
s1 = tkinter.Scrollbar(f, orient=tkinter.VERTICAL)
text = tkinter.Text(f, height=25, width=75, yscrollcommand=s1.set, wrap='word', font=12)

s1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
s1.config(command=text.yview)
text.pack()
f.pack()


# 滚动条与text联动


# 按钮1
def myORC():
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image):
        img_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.jpg'
        path = './' + img_name
        im.save(path)  # 把剪贴板图片保存到这个路径
        print('已保存')
        # 旧的识别模型
        data = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
        # 新的模型
        # ocr = CnOcr()
        # puredata = ocr.ocr_for_single_line(path)

        puredata = data.strip('\n')
        # print(text, end='')
        # clear_clipboard()
        text.delete('1.0', tkinter.END)  # 清空原内容
        text.insert('1.0', puredata)
        # pyperclip.copy(data)  # 文字写入剪贴板
        os.remove(path)  # 删除临时照片
    else:
        text.delete('1.0', tkinter.END)
        text.insert('1.0', '剪贴板无图片\n')


btn1 = tkinter.Button(win, text='ORC', command=myORC)
btn1.pack(side='left', ipadx=20, pady=10, padx=50)


# 按钮2
def translate():
    yuan = text.get('1.0', tkinter.END)
    baidu.query = yuan
    fanyi_list = baidu.main()  # 返回是个列表，需要转成几行字符串
    fanyi = ''
    for i in range(0, len(fanyi_list)):
        fanyi += fanyi_list[i] + '\n'
    text.insert(tkinter.END, '\n=======百度翻译=======\n' + fanyi)


btn2 = tkinter.Button(win, text='翻译', command=translate)
btn2.pack(side='left', ipadx=20, pady=10, padx=0)


# 按钮3
def copy():
    data = text.get(1.0, tkinter.END).strip('\n')
    pyperclip.copy(data)  # 文字写入剪贴板
    text.insert(tkinter.END, '\n\n====== 复制成功 ======\n')


btn3 = tkinter.Button(win, text='复制', command=copy)
btn3.pack(side='left', ipadx=20, pady=10, padx=55)

def fmt():
    data = text.get(1.0, tkinter.END)
    data = data.replace(' ', '')
    data = data.replace('\n', '')
    text.delete('1.0', tkinter.END)  # 清空原内容
    text.insert('1.0', data)


btn4 = tkinter.Button(win, text='去空格', command=fmt)
btn4.pack(side='left', ipadx=20, pady=10, padx=10)

# 进入消息循环
win.mainloop()
