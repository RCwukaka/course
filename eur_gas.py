#coding=gbk

import csv

import pandas as pd
import matplotlib.pyplot as plt
df_data = []

csv_reader = csv.reader(open("eur_gas.csv"))
for row in csv_reader:
    df_data.append({'Date': row[0]+"", 'Price': float(row[1])})


data = pd.DataFrame(df_data, columns=['Date', 'Price'])
_data = data.sort_values(by="Date", ascending=True)

for i_data in range(len(_data['Date'])):
    if (i_data % 5) != 0:
        _data.iloc[i_data, 0] = ""

plt.subplots(figsize=(14, 6))
plt.plot(range(len(_data['Date'])), _data['Price'], 'b', label="eur_gas price")

plt.annotate('note!war', xy=(34, 300), xytext=(24, 280), fontsize=16,
             arrowprops=dict(facecolor='red', shrink=0.01))
plt.vlines([34], 260, 350, linestyles='dashed', colors='red')

plt.tick_params(labelsize=12)
plt.xticks([i for i in range(len(_data['Date']))], _data['Date'].values, rotation=70)
plt.grid(True)
plt.legend(loc='upper left')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.show()