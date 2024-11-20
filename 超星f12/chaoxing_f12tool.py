from time import *
from DragWindows import *
import pyautogui as gui
import tkinter.font as tf


def remove_operation():
    # 点击浏览器页面，定位到浏览器
    gui.click(1450, 530)
    # F12
    gui.press('f12')
    sleep(0.5)
    # 点击Eventlistener
    gui.doubleClick(1390, 640)
    sleep(0.5)
    # 点击mouseout
    gui.click(1162, 1008)
    sleep(0.5)
    # 下拉按钮下拉几下
    gui.click(1908, 1020)
    gui.click()
    gui.click()
    sleep(0.5)
    # # 滚动
    # gui.scroll(-140)
    # 点击remove
    gui.doubleClick(1234, 973)
    sleep(0.5)
    # 关闭控制台
    gui.press('f12')
    sleep(0.5)


def click_play():
    pos1 = None
    pos2 = None
    i = 0
    while pos1 is None and pos2 is None and i < 5:
        sleep(0.5)
        pos1 = gui.locateOnScreen('start_light.png', grayscale=False, region=(192, 192, 900, 800))
        print(pos1)
        if pos1 is not None:
            gui.click(gui.center(pos1))
            return True
        else:
            # 找不到亮着的播放键，就找暗的
            pos2 = gui.locateOnScreen('start.png', grayscale=False, region=(192, 192, 900, 800))
            print(pos2)
            if pos2 is not None:
                gui.click(gui.center(pos2))
                return True
        i += 1  # 重复循环
    if pos1 is None and pos2 is None:
        a = gui.alert(text='未发现播放按钮', title='tip')
        print(a)
        return False


def quitbtn():
    root.destroy()


def minimize():
    root.state('iconic')


def all_operation():
    print("click my button")
    rgb_now = gui.screenshot().getpixel((180, 112))
    if rgb_now == (58, 67, 87):
        remove_operation()
        video_status = click_play()  # 点击播放按钮
        if video_status:
            minimize()
    else:
        a = gui.alert(text='不在超星页面！', title='tip')
        print(a)


# from tkinter import messagebox
# window = tk.Tk()  # 创建主窗口
# window.minsize(200, 100)  # 大小
# # window.overrideredirect(True)  # 隐藏标题栏
# window.wm_attributes('-alpha', 0.75)
# window.wm_attributes('-topmost', True)

root = DragWindow()
root.title('超星小工具')
root.set_window_size(200, 300)
root.set_display_postion(1000, 500)
# root.overrideredirect(True)  # 隐藏标题栏

myfont = tf.Font(root=root, family='Times', size=18)
btn1 = tk.Button(root, text='消除鼠标限制', font=myfont, command=all_operation)
btn1.pack(side='top', fill='x', ipady='20pix')  # 内部按钮拓展
btn2 = tk.Button(root, text='最小化', font=myfont, command=minimize)
btn2.pack(side='bottom', fill='x', ipady='20pix')  # 内部按钮拓展
btn3 = tk.Button(root, text='***', font=myfont)
btn3.pack(expand=1, fill='x')
root.mainloop()
