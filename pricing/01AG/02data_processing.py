# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/8/21 19:53
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 02data_processing.py
# @Software: PyCharm

import pandas as pd


def get_metrics():
    data = pd.read_csv('../02data/result/data.csv')
    data = data.sort_values(by=['code', 'date'])

    # 1 Size
    data['Size'] = data['mv']

    # 2 账面市值比B/M
    data['BM'] = data['equity'] / data['mv']

    # 3 营运利润率OP
    data['OP'] = data['profit'] / data['equity']

    # 4 投资风格
    # 左边
    data['INV1'] = (data['asset'] - data['asset'].shift()) / data['asset'].shift()
    data['INV1'] = data['INV1'].fillna(0)
    data['INV2'] = (data['cash'] - data['cash'].shift()) / data['asset'].shift()
    data['INV3'] = (data['receivable'] - data['receivable'].shift()) / data['asset'].shift()
    data['INV4'] = (data['inventory'] - data['inventory'].shift()) / data['asset'].shift()
    data['INV5'] = (data['ppe'] - data['ppe'].shift()) / data['asset'].shift()
    data['INV6'] = (data['intangible_asset'] - data['intangible_asset'].shift()) / data['asset'].shift()
    # 右边
    data['INV7'] = (data['current_liability'] - data['current_liability'].shift()) / data['asset'].shift()
    data['INV8'] = (data['non_current_liability'] - data['non_current_liability'].shift()) / data['asset'].shift()
    data['INV9'] = (data['liability'] - data['liability'].shift()) / data['asset'].shift()
    data['INV10'] = (data['surplus']+data['undistributed_profit'] - (data['surplus']+data['undistributed_profit']).shift()) / data['asset'].shift()
    data['INV11'] = (data['capital'] - data['capital'].shift()) / data['asset'].shift()

    # 5 rm-rf
    data['rm-rf'] = data['rm'] - data['rf']/100
    data['rf'] = data['rf']/100

    df = data[['code', 'date', 'r', 'rm-rf', 'rf', 'Size', 'BM', 'OP', 'INV1', 'INV2', 'INV3', 'INV4', 'INV5', 'INV6', 'INV7', 'INV8', 'INV9', 'INV10', 'INV11']]
    print(df)

    # 对df按照date和code进行分组，每一组将0值替换为nan，然后用后一个非nan值填充
    # df = df.groupby('code').apply(lambda x: x.replace(0, pd.NA).fillna(method='bfill'))
    df.to_csv('../02data/result/metrics.csv', index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    get_metrics()





