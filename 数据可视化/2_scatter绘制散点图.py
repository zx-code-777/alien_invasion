from matplotlib import pyplot

x_values = list(range(1, 101))
y_values = [x ** 2 for x in x_values]
pyplot.style.use('seaborn')
fig, ax = pyplot.subplots()
# ax.scatter(x_values, y_values, c='yellow', s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Reds, s=10)
# 设置图表标题并给坐标轴加上标签
ax.set_title('平方数', fontproperties='SimHei', fontsize=24)
ax.set_xlabel('值', fontproperties='SimHei', fontsize=14)
ax.set_ylabel("值的平方", fontproperties='SimHei', fontsize=14)
# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 120, 0, 11000])
pyplot.savefig('squares_plot.png',bbox_inches='tight')
