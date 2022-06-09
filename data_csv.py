# 导入 csv 库
import csv
import pandas as pd
import matplotlib.pyplot as plt

df_data = []

font1 = {'family': 'SimHei',
         'weight': 'normal',
         'size': 12,
         }

# 打开文件
with open("Food_price_indices_data_jun.csv", encoding="utf-8-sig", mode="r") as f:
    # 基于打开的文件，创建csv.DictReader实例
    reader = csv.DictReader(f)

    # 输出信息
    for row in reader:
        df_data.append({'Date': row['Date'], 'Food Price Index': float(row['Food Price Index']),
                        'Meat': float(row['Meat']), 'Dairy': float(row['Dairy']), 'Cereals': float(row['Cereals']),
                        'Oils': float(row['Oils']),
                        'Sugar': float(row['Sugar'])})

data = pd.DataFrame(df_data, columns=['Date', 'Food Price Index', 'Meat', 'Dairy', 'Cereals', 'Oils', 'Sugar'])
data.drop_duplicates()

plt.subplots(figsize=(14, 6))
plt.plot(data['Date'], data['Food Price Index'], 'b', label="Food Price Index")
plt.plot(data['Date'], data['Meat'], 'g', label="Meat")
plt.plot(data['Date'], data['Dairy'], 'r', label="Dairy")
plt.plot(data['Date'], data['Cereals'], 'c', label="Cereals")
plt.plot(data['Date'], data['Oils'], 'm', label="Oils")
plt.plot(data['Date'], data['Sugar'], 'y', label="Sugar")
plt.tick_params(labelsize=12)
plt.xticks(rotation=70)
plt.grid(True)
plt.xlabel("time", font1)
plt.legend(loc='upper left')

plt.annotate('note!war', xy=('Feb-22', 120), xytext=('Feb-21', 150), fontsize=16,
             arrowprops=dict(facecolor='red', shrink=0.01))
plt.vlines(['Feb-22'], 50, 250, linestyles='dashed', colors='red')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
