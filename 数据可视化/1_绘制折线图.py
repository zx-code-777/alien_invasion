from matplotlib import pyplot

input_value = [1,2,3,4,5]
squares = [1, 4, 8, 16, 23]
pyplot.style.use('seaborn')
fig, ax = pyplot.subplots()
ax.plot(input_value, squares, linewidth=3)
# 设置图标标题并给坐标轴加上标签
ax.set_title("平方数", fontproperties="SimHei", fontsize=24)
ax.set_xlabel("值", fontproperties="SimHei", fontsize=14)
ax.set_ylabel("值的平方", fontproperties="SimHei", fontsize=14)
# 设置刻度标记大小
ax.tick_params(axis='both', labelsize=14)
pyplot.show()
