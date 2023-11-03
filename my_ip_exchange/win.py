# 窗体设置
import tkinter

win = tkinter.Tk()  # 构造窗体
win.title('title')

def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)

def ten_to_two():
    print('化学，狗都不学！！！！')



center_window(win, 420, 300)

# 按钮设置
b1 = tkinter.Button(win, text='化学，狗都不学！', command=ten_to_two)
b1.pack()

win.mainloop()  # 进入消息循环