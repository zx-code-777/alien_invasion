from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# 创建一个D6
die_1 = Die()
die_2 = Die()
# 掷几次骰子并将结果存储在一个列表上
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果
frequencies = []
two_result = die_1.num_sides + die_2.num_sides
for value in range(2, two_result + 1):
    # 遍历可能的点数（这里为1～6），计算每种点数在results中出现了多少次
    frequency = results.count(value)
    frequencies.append(frequency)
# 对结果进行可视化
x_values = list(range(2, two_result + 1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷两个D6 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='2D6.html')
