import matplotlib.pyplot as plt
from random_walk import RandomWalk

# while True:
    # 创建一个RandomWalk实例
rw = RandomWalk(50000)
rw.fill_walk()
# 将所有的点都绘制出来
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9))
# 颜色映射
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
# 突出起点和终端
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
# 隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()

    # keep_running = input("创建其他漫步？(y/n)")
    # if keep_running == 'n':
    #     break
