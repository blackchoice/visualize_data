import csv

import matplotlib.pyplot as plt

filename = 'data/3322881.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取最高温度
    highs = []
    for row in reader:
        if (row[8] != ''):
            high = int(row[8])
        else:
            high = 0
        highs.append(high)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(highs, c='red')

    # 设置图形的格式
    ax.set_title("New York Max Temperature", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel('温度（F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

print(highs)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)
