import matplotlib.pyplot as plt

# 创建一个画布
fig = plt.figure()

# 绘制一个圆
circle = plt.Circle((0, 0), radius=1, color='r')
fig.add_artist(circle)

# 绘制蒙娜丽莎的眼睛
left_eye = plt.Circle((-0.3, 0.3), radius=0.1, color='b')
fig.add_artist(left_eye)
right_eye = plt.Circle((0.3, 0.3), radius=0.1, color='b')
fig.add_artist(right_eye)

# 绘制蒙娜丽莎的嘴巴
plt.plot([-0.2, 0.2], [-0.1, -0.1], 'c')

# 显示图像
plt.show()
