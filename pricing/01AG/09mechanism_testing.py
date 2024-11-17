# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/11/13 14:34
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 09mechanism_testing.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import statsmodels.api as sm

invs = ['INV1', 'INV2', 'INV3', 'INV4', 'INV5', 'INV6', 'INV7', 'INV8', 'INV9', 'INV10', 'INV11']
columns = ['AG', 'CASH', 'RECEIVABLE', 'INVENTORY', 'PPE', 'INTANGIBLE_ASSET', 'CURRENT_LIABILITY', 'NON_CURRENT_LIABILITY', 'LIABILITY', 'RETAINED_EARNINGS', 'CAPITAL']
factors = ['emotion', 'financial', 'consume', 'production']

for factor in factors:
    data_all = pd.DataFrame(columns=columns, index=['alpha', 't_value', 'p_value', 'significant'])
    data_before = pd.DataFrame(columns=columns, index=['alpha', 't_value', 'p_value', 'significant'])
    data_after = pd.DataFrame(columns=columns, index=['alpha', 't_value', 'p_value', 'significant'])
    factor_data = pd.read_csv('../02data/result/macro_{}.csv'.format(factor)).dropna()
    print("+++++++++++++++++++++++{}+++++++++++++++++++++++".format(factor))
    for inv in invs:
        data = pd.read_csv('../02data/result/factors_{}.csv'.format(inv)).dropna()
        data = data.drop(columns=['Portfolio'])
        # 按照时间分组，取平均
        data = data.groupby('date').mean().reset_index()
        data1 = data.dropna()
        data1 = data1[data1['date'] > '2000-01']
        data2 = data[data['date'] < '2007-06'].dropna()
        data3 = data[data['date'] > '2007-06'].dropna()

        data1 = pd.merge(data1, factor_data, on='date', how='left').dropna()
        data2 = pd.merge(data2, factor_data, on='date', how='left').dropna()
        data3 = pd.merge(data3, factor_data, on='date', how='left').dropna()

        X = data1[['rm-rf', 'CMA', 'HML', 'SMB', 'RMW']]
        # 将factor_data的第二列标准化
        factor_data[factor_data.columns[1]] = (factor_data[factor_data.columns[1]] - factor_data[factor_data.columns[1]].mean()) / factor_data[factor_data.columns[1]].std()
        y = data1[factor_data.columns[1]]
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()
        print('全样本数据')
        print(model.summary())

        X = data2[['rm-rf', 'CMA', 'HML', 'SMB', 'RMW']]
        # 将factor_data的第二列标准化
        factor_data[factor_data.columns[1]] = (factor_data[factor_data.columns[1]] - factor_data[factor_data.columns[1]].mean()) / factor_data[factor_data.columns[1]].std()
        y = data2[factor_data.columns[1]]
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()
        print('2007年6月之前数据')
        print(model.summary())

        X = data3[['rm-rf', 'CMA', 'HML', 'SMB', 'RMW']]
        # 将factor_data的第二列标准化
        factor_data[factor_data.columns[1]] = (factor_data[factor_data.columns[1]] - factor_data[factor_data.columns[1]].mean()) / factor_data[factor_data.columns[1]].std()
        y = data3[factor_data.columns[1]]
        X = sm.add_constant(X)
        model = sm.OLS(y, X).fit()
        print('2007年6月之后数据')
        print(model.summary())

