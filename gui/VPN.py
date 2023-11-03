from time import time
import pyautogui as gui
from time import sleep
import os

os.startfile(r'C:\Users\Public\Desktop\EasyConnect.lnk')

jud = False
yes = jud
start = time()

cnt = 0
while yes is jud:
    cnt += 1
    yes = gui.pixelMatchesColor(900, 520, (255, 255, 255))
    # yes = gui.locateOnScreen('密码.jpg')
    sleep(0.5)
    print(f'第{cnt}次尝试', yes)
    t = time() - start
    if t > 10:
        print('没找到')
        break

if yes is not jud:
    sleep(0.5)
    gui.doubleClick(920, 535)
    gui.typewrite('y\n2220802')
    gui.typewrite('\t')
    gui.typewrite('5059@suep')
else:
    print('彻底没找到')
    input('')
