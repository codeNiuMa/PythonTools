import tkinter
import pyperclip


def ten_to_two():
    text_two.delete(0, 'end')  # 清空
    data = text_ten.get().split('.')
    # print('二进制：', end='')
    for single in data:
        # 转化二进制
        if single is not data[-1]:
            single = '{:08b}'.format(int(single))
            text_two.insert('end', single)  # 赋值
            text_two.insert('end', '.')  # 赋值
            # print(single, end='.')
        else:
            single = '{:08b}'.format(int(single))
            text_two.insert('end', single)  # 赋值
    # text_two.insert(0, '十转二test')  # 赋值


def two_to_ten():
    text_ten.delete(0, 'end')  # 清空
    data = text_two.get().split('.')
    for single in data:
        # 转化十进制
        if single is not data[-1]:
            single = int(single, 2)
            text_ten.insert('end', str(single))  # 赋值
            text_ten.insert('end', '.')  # 赋值
        else:
            single = int(single, 2)
            text_ten.insert('end', str(single))  # 赋值


def copy_1():
    # 实现复制文本框的内容
    pyperclip.copy(text_two.get())


def copy_2():
    pyperclip.copy(text_ten.get())


def clear():
    text_two.delete(0, 'end')
    text_ten.delete(0, 'end')


# 窗体设置
win = tkinter.Tk()  # 构造窗体
win.title('进制转换 by:yuange')


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


center_window(win, 420, 300)

# 标签设置
# label1
tkinter.Label(win, text="二进制:").grid(row=0, column=0, padx=20, pady=10, sticky='e')
# label2
tkinter.Label(win, text="十进制:").grid(row=1, column=0, padx=20, pady=10)

# 文本框
text_two = tkinter.Entry(win, width=35)
text_two.insert(0, '11111111.11111111.11111111.11111111')
text_two.grid(row=0, column=1, padx=10, pady=50, sticky='w')

text_ten = tkinter.Entry(win, width=35)
text_ten.insert(0, '255.255.255.255')
text_ten.grid(row=1, column=1, padx=10, pady=10)

# 按钮设置
b1 = tkinter.Button(win, text='十转二', command=ten_to_two)
b1.grid(row=3, column=1, padx=40, pady=5, sticky='w')
b2 = tkinter.Button(win, text='二转十', command=two_to_ten)
b2.grid(row=4, column=1, padx=40, pady=5, sticky='w')
b3 = tkinter.Button(win, text='复制', command=copy_1)
b3.grid(row=0, column=2, padx=0, pady=5, sticky='w')
b4 = tkinter.Button(win, text='复制', command=copy_2)
b4.grid(row=1, column=2, padx=0, pady=5, sticky='w')
b5 = tkinter.Button(win, text='清空', height=2, width=8, command=clear)
b5.grid(row=3, column=1, padx=0, pady=5, sticky='e')

win.mainloop()  # 进入消息循环
