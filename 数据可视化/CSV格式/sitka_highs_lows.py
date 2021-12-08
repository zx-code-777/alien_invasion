import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# 对例表调用enumerate()来获取每个元素的索引及其值
# for index,column_header in enumerate(header_row):
#     print(index,column_header)
    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"{current_date}数据丢失")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# 根据最高温度和最低温度绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs,  c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式
ax.set_title('2018年每日最高和最低温度', fontproperties='SimHei', fontsize=24)
ax.set_xlabel('', fontproperties='SimHei', fontsize=16)
# 绘制倾斜的日期标签
fig.autofmt_xdate()
ax.set_ylabel('温度', fontproperties='SimHei', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()




