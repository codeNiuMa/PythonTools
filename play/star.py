from turtle import *
from random import *

Turtle().hideturtle()
speed(100)
colormode(255)  # rgb色彩模式
setup(800, 600)  # 画布大小
bgcolor(10, 10, 10)  # 背景色

for i in range(100):  # 画的个数
    pu()  # 抬起画笔
    x, y = randint(-400, 400), randint(-300, 300)
    goto(x, y)
    pd()  # 放下画笔
    r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
    # 填充颜色
    color(r, g, b)
    begin_fill()
    L = randint(1, 5)
    circle(L)
    # left(72)
    # for i in range(5):
    #     fd(L)  # 前进多少
    #     right(144)
    end_fill()
ht()