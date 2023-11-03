import pyautogui as gui
from time import sleep

# 获得鼠标位置，在这起到给old_pos一个初始值的作用
old_pos = gui.position()

# print(mouse_location)

while True:
    # 获得当前鼠标位置
    mouse_location = gui.position()
    # 当前位置和旧位置不同时，输出鼠标位置
    if mouse_location != old_pos:
        print("("+str(mouse_location.x)+", "+str(mouse_location.y)+")")
        # print("旧位置：("+str(old_pos.x)+", "+str(old_pos.y)+")")
        # print("=======")
        # 当前位置变成旧位置，再度循环看是否变化位置
        old_pos = mouse_location
    # 刷新率
    sleep(0.05)
