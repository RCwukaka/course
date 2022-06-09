# coding=utf-8

import requests
import re
import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts

font1 = {'family': 'SimHei',
         'weight': 'normal',
         'size': 12,
         }

pro = ts.pro_api('809e1cd982cabb44bcf52bb954e665438df8b1c84191e6aaf70dbf1c')
# 拉取数据
df1 = pro.fut_daily(**{
    "trade_date": "",
    "ts_code": "SCL.INE",
    "exchange": "INE",
    "start_date": "20220110",
    "end_date": "",
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "pre_close",
    "pre_settle",
    "open",
    "high",
    "low",
    "close",
    "settle",
    "change1",
    "change2",
    "vol",
    "amount",
    "oi",
    "oi_chg"
])

User_Agent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
]

headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-HK;q=0.6,zh-TW;q=0.5",
           'host': 'api.jijinhao.com',
           'referer': 'https://www.cngold.org/',
           'X-Requested-With': 'XMLHttpRequest'
           }

query = {
    'code': 'JO_50797',
    'pageSize': 1000
}

query_path = 'https://api.jijinhao.com/sQuoteCenter/kDataList.htm'
res = requests.get(query_path, headers=headers, params=query)

content = res.text.replace("var  KLC_KL = {\"data\":[[", '').replace('[', '').strip(']]}') + "}"

datas = content.split("},{")

df_data = []

for data in datas:
    time = int(re.search('"time":([1-9]\d*)', data).group().split(":")[1])
    if time > 1642800000000:
        day = re.search('"day":"\d*/\d*/\d*"', data).group().replace("\"", "").replace("/", "").split(":")[1]
        price = float(re.search('"close":\d*.\d', data).group().split(":")[1])
        oil = df1[df1["trade_date"] == day].head().close
        try:
            oil = float(oil)
        except Exception as e:
            continue
        df_data.append({'time': time, 'day': day, 'price': price, 'oil': oil})
        print(oil)

df = pd.DataFrame(df_data, columns=['time', 'day', 'price', 'oil'])

data = df.sort_values(by="time", ascending=True)
data.drop_duplicates()

for i_data in range(len(df['day'])):
    if (i_data % 5) != 0:
        df.iloc[i_data, 1] = ""

fig, ax1 = plt.subplots(figsize=(14, 6))
plt.plot(range(len(df['day'])), data['price'], 'b', label="美麦数据")
ax1.tick_params(labelsize=12)
ax1.set_xticklabels(labels=data['day'], rotation=70, fontsize=8)
plt.grid(True)
plt.xlabel("time", font1)
plt.ylabel('美麦数据', font1)
plt.legend(loc='upper left')

ax2 = ax1.twinx()
plt.plot(range(len(df['day'])), data['oil'],  'g', label="oil")
plt.legend(loc='upper right')
ax2.tick_params(labelsize=12)
ax2.set_ylabel("原油数据", font1)

plt.annotate('note!war', xy=(18, 926), xytext=(24, 800), fontsize=16,
             arrowprops=dict(facecolor='red', shrink=0.01))
plt.vlines([18], 500, 1400, linestyles='dashed', colors='red')

plt.xticks([i for i in range(len(df['day']))], df['day'].values, rotation=70)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()
