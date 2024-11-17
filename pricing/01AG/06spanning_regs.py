# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/10/14 11:46
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 06spanning_regs.py
# @Software: PyCharm

import pandas as pd
import numpy as np
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm


CASH = pd.read_csv('../02data/result/factors_INV2.csv')
CASH = CASH[CASH['date']>'2007-06'][['date','CMA']].dropna()
CASH = CASH.rename({'CMA': 'CASH'}, axis=1)
RECEIVABLE = pd.read_csv('../02data/result/factors_INV3.csv')
RECEIVABLE = RECEIVABLE[RECEIVABLE['date']>'2007-06'][['date','CMA']].dropna()
RECEIVABLE = RECEIVABLE.rename({'CMA': 'RECEIVABLE'}, axis=1)
# INTANGIBLE_ASSET = pd.read_csv('../02data/result/factors_INV6.csv')
# INTANGIBLE_ASSET = INTANGIBLE_ASSET[INTANGIBLE_ASSET['date']>'2007-06'][['date','CMA']].dropna()
# INTANGIBLE_ASSET = INTANGIBLE_ASSET.rename({'CMA': 'INTANGIBLE_ASSET'}, axis=1)

columns =['INV1','INV4','INV5','INV6']
columnss =['AG','INVENTORY','PPE','INTANGIBLE_ASSET']
# columns =['INV1','INV4','INV5']
# columnss =['AG','INVENTORY','PPE']

data_spanning = pd.DataFrame(columns = columnss,index = ['alpha','t_value','p_value','MKT','t_value_MKT','p_value_MKT','SMB','t_value_SMB','p_value_SMB',
                                                         'HML','t_value_HML','p_value_HML','RMW','t_value_RMW','p_value_RMW','CASH','t_value_CASH','p_value_CASH',
                                                         'RECEIVABLE','t_value_RECEIVABLE','p_value_RECEIVABLE'])

yvar = 'CMA'
maxlags = 12
xvars = ['rm-rf', 'SMB', 'HML', 'RMW', 'CASH', 'RECEIVABLE']
for i in range(len(columns)):
    data = pd.read_csv('../02data/result/factors_{}.csv'.format(columns[i])).dropna()
    data = data[data['date'] > '2007-06']
    xvars = ['rm-rf', 'SMB', 'HML', 'RMW', 'CASH', 'RECEIVABLE']
    data1 = pd.merge(data, CASH, on='date', how='left').dropna()
    data1 = pd.merge(data1, RECEIVABLE, on='date', how='left').dropna()
    # data1 = pd.merge(data1, INTANGIBLE_ASSET, on='date', how='left').dropna()
    # 删除重复行
    data1 = data1.drop(columns=['Portfolio','r'])
    data1 = data1.drop_duplicates()
    print(data1)
    # 选择一个组合
    # data1 = data1[data1['Portfolio'] == 'SA']
    # data1 = data1.drop_duplicates()
    # print(data1)
    # 在自变量列表中添加常数项
    xvars_with_const = sm.add_constant(data1[xvars])
    model = OLS(data1[yvar], xvars_with_const).fit()
    res_robust = model.get_robustcov_results(cov_type='HAC', maxlags=maxlags)
    model.params.values[:] = res_robust.params
    model.tvalues.values[:] = res_robust.tvalues
    model.pvalues.values[:] = res_robust.pvalues
    print(model.summary())
    data_spanning.loc['alpha',columnss[i]] = model.params['const']
    data_spanning.loc['t_value',columnss[i]] = model.tvalues['const']
    data_spanning.loc['p_value',columnss[i]] = model.pvalues['const']
    data_spanning.loc['MKT',columnss[i]] = model.params['rm-rf']
    data_spanning.loc['t_value_MKT',columnss[i]] = model.tvalues['rm-rf']
    data_spanning.loc['p_value_MKT',columnss[i]] = model.pvalues['rm-rf']
    data_spanning.loc['SMB',columnss[i]] = model.params['SMB']
    data_spanning.loc['t_value_SMB',columnss[i]] = model.tvalues['SMB']
    data_spanning.loc['p_value_SMB',columnss[i]] = model.pvalues['SMB']
    data_spanning.loc['HML',columnss[i]] = model.params['HML']
    data_spanning.loc['t_value_HML',columnss[i]] = model.tvalues['HML']
    data_spanning.loc['p_value_HML',columnss[i]] = model.pvalues['HML']
    data_spanning.loc['RMW',columnss[i]] = model.params['RMW']
    data_spanning.loc['t_value_RMW',columnss[i]] = model.tvalues['RMW']
    data_spanning.loc['p_value_RMW',columnss[i]] = model.pvalues['RMW']
    data_spanning.loc['CASH',columnss[i]] = model.params['CASH']
    data_spanning.loc['t_value_CASH',columnss[i]] = model.tvalues['CASH']
    data_spanning.loc['p_value_CASH',columnss[i]] = model.pvalues['CASH']
    data_spanning.loc['RECEIVABLE',columnss[i]] = model.params['RECEIVABLE']
    data_spanning.loc['t_value_RECEIVABLE',columnss[i]] = model.tvalues['RECEIVABLE']
    data_spanning.loc['p_value_RECEIVABLE',columnss[i]] = model.pvalues['RECEIVABLE']
    # data_spanning.loc['INTANGIBLE_ASSET',columnss[i]] = model.params['INTANGIBLE_ASSET']
    # data_spanning.loc['t_value_INTANGIBLE_ASSET',columnss[i]] = model.tvalues['INTANGIBLE_ASSET']
    # data_spanning.loc['p_value_INTANGIBLE_ASSET',columnss[i]] = model.pvalues['INTANGIBLE_ASSET']

print(data_spanning)
data_spanning.to_csv('../02data/result/data_spanning.csv', encoding='utf-8-sig')






# res.params.values[:] = res_robust.params
# res.tvalues.values[:] = res_robust.tvalues
# res.pvalues.values[:] = res_robust.pvalues
#
# print(res.summary())
# data_spanning.loc['alpha','AG'] = res.params['const']
# data_spanning.loc['p_value','AG'] = res.pvalues['const']
# data_spanning.loc['MKT','AG'] = res.params['rm-rf']
# data_spanning.loc['p_value_MKT','AG'] = res.pvalues['rm-rf']
# data_spanning.loc['SMB','AG'] = res.params['SMB']
# data_spanning.loc['p_value_SMB','AG'] = res.pvalues['SMB']
# data_spanning.loc['HML','AG'] = res.params['HML']
# data_spanning.loc['p_value_HML','AG'] = res.pvalues['HML']
# data_spanning.loc['RMW','AG'] = res.params['RMW']
# data_spanning.loc['p_value_RMW','AG'] = res.pvalues['RMW']
# data_spanning.loc['CASH','AG'] = res.params['CASH']
# data_spanning.loc['p_value_CASH','AG'] = res.pvalues['CASH']
# data_spanning.loc['RECEIVABLE','AG'] = res.params['RECEIVABLE']
# data_spanning.loc['p_value_RECEIVABLE','AG'] = res.pvalues['RECEIVABLE']
#
# print(data_spanning)