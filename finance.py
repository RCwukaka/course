#coding=gbk
import matplotlib.pyplot as plt
import tushare as ts

# ��ʼ��pro�ӿ�
pro = ts.pro_api('809e1cd982cabb44bcf52bb954e665438df8b1c84191e6aaf70dbf1c')

# ��ȡ����
XIN9 = pro.index_global(**{
    "ts_code": "XIN9",
    "trade_date": "",
    "start_date": 20220101,
    "end_date": 20220620,
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "close"
])

CSX5P = pro.index_global(**{
    "ts_code": "CSX5P",
    "trade_date": "",
    "start_date": 20220101,
    "end_date": 20220620,
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "close"
])

SPX = pro.index_global(**{
    "ts_code": "SPX",
    "trade_date": "",
    "start_date": 20220101,
    "end_date": 20220620,
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "close"
])

RTS = pro.index_global(**{
    "ts_code": "RTS",
    "trade_date": "",
    "start_date": 20220101,
    "end_date": 20220620,
    "limit": "",
    "offset": ""
}, fields=[
    "ts_code",
    "trade_date",
    "close"
])

font1 = {'family': 'SimHei',
         'weight': 'normal',
         'size': 12,
         }


fig, axes = plt.subplots(2, 2, figsize=(16, 8))  # �˴���һ��2*2��ͼ
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
ax1 = axes[0, 0]
ax2 = axes[0, 1]
ax3 = axes[1, 0]
ax4 = axes[1, 1]

#��ʱ�й�A50ָ�� (��ʱA50)
XIN9_data = XIN9.sort_values(by="trade_date", ascending=True)

for i_data in range(len(XIN9_data['trade_date'])):
    if (i_data % 5) != 0:
        XIN9_data.iloc[i_data, 1] = ""

ax1.plot(range(len(XIN9_data['trade_date'])), XIN9_data['close'], label="��ʱ�й�A50ָ��")
ax1.set_xticks([i for i in range(len(XIN9_data['trade_date']))], XIN9_data['trade_date'].values, rotation=70, fontsize=7)
ax1.vlines([38], 13000, 15500, linestyles='dashed', colors='red')
ax1.annotate('note!war', xy=(38, 13500), xytext=(44, 13000), fontsize=16,
             arrowprops=dict(facecolor='red', shrink=0.01))

#STOXXŷ��50ָ��
CSX5P_data = CSX5P.sort_values(by="trade_date", ascending=True)

for i_data in range(len(CSX5P_data['trade_date'])):
    if (i_data % 5) != 0:
        CSX5P_data.iloc[i_data, 1] = ""

ax2.plot(range(len(CSX5P_data['trade_date'])), CSX5P_data['close'], label="ŷ��50ָ��")
ax2.set_xticks([i for i in range(len(CSX5P_data['trade_date']))], CSX5P_data['trade_date'].values, rotation=70, fontsize=7)
ax2.vlines([38], 3500, 4400, linestyles='dashed', colors='red')
ax2.annotate('note!war', xy=(38, 3700), xytext=(45, 3500), fontsize=16,
             arrowprops=dict(facecolor='red', shrink=0.01))

#����500ָ��
SPX_data = SPX.sort_values(by="trade_date", ascending=True)

for i_data in range(len(SPX_data['trade_date'])):
    if (i_data % 5) != 0:
        SPX_data.iloc[i_data, 1] = ""

ax3.plot(range(len(SPX_data['trade_date'])), SPX_data['close'], label="����500ָ��")
ax3.set_xticks([i for i in range(len(SPX_data['trade_date']))], SPX_data['trade_date'].values, rotation=70, fontsize=7)
ax3.vlines([38], 4000, 4800, linestyles='dashed', colors='red')
ax3.annotate('note!war', xy=(38, 4300), xytext=(45, 4100), fontsize=16,
             arrowprops=dict(facecolor='red', shrink=0.01))

#����˹RTSָ��
RTS_data = RTS.sort_values(by="trade_date", ascending=True)

for i_data in range(len(RTS_data['trade_date'])):
    if (i_data % 5) != 0:
        RTS_data.iloc[i_data, 1] = ""

ax4.plot(range(len(RTS_data['trade_date'])), RTS_data['close'], label="����˹RTSָ��")
ax4.set_xticks([i for i in range(len(RTS_data['trade_date']))], RTS_data['trade_date'].values, rotation=70, fontsize=7)
ax4.vlines([38], 800, 1600, linestyles='dashed', colors='red')
ax4.annotate('note!war', xy=(38, 800), xytext=(45, 800), fontsize=16,
             arrowprops=dict(facecolor='red', shrink=0.01))\

for i in range(2):
    for j in range(2):
        axes[i, j].grid(True)
        axes[i, j].legend(loc='upper left')

plt.show()

