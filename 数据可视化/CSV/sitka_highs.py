import csv

filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# 对例表调用enumerate()来获取每个元素的索引及其值
# for index,column_header in enumerate(header_row):
#     print(index,column_header)
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
print(highs)





