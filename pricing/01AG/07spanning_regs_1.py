# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/10/14 17:02
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 07spanning_regs_1.py
# @Software: PyCharm

import pandas as pd
import numpy as np
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm


CASH = pd.read_csv('../02data/result/factors_INV2.csv')[['date','rm-rf', 'SMB', 'HML', 'RMW','CMA']]
CASH = CASH[CASH['date']>'2007-06'].dropna()
CASH = CASH.rename({'CMA': 'CASH'}, axis=1)
RECEIVABLE = pd.read_csv('../02data/result/factors_INV3.csv')[['date','rm-rf', 'SMB', 'HML', 'RMW','CMA']]
RECEIVABLE = RECEIVABLE[RECEIVABLE['date']>'2007-06'].dropna()
RECEIVABLE = RECEIVABLE.rename({'CMA': 'RECEIVABLE'}, axis=1)
# INTANGIBLE_ASSET = pd.read_csv('../02data/result/factors_INV6.csv')
# INTANGIBLE_ASSET = INTANGIBLE_ASSET[INTANGIBLE_ASSET['date']>'2007-06'].dropna()
# INTANGIBLE_ASSET = INTANGIBLE_ASSET.rename({'CMA': 'INTANGIBLE_ASSET'}, axis=1)

columns =['INV1','INV4','INV5','INV6']
columnss =['AG','INVENTORY','PPE','INTANGIBLE_ASSET']
cashs =['cash1','cash2','cash3','cash4']
receivables =['receivable1','receivable2','receivable3','receivable4']
# columns =['INV1','INV4','INV5']
# columnss =['AG','INVENTORY','PPE']

data_spanning_cash = pd.DataFrame(columns = cashs,index = ['alpha','t_value','p_value','MKT','t_value_MKT','p_value_MKT','SMB','t_value_SMB','p_value_SMB',
                                                         'HML','t_value_HML','p_value_HML','RMW','t_value_RMW','p_value_RMW','AG','t_value_AG','p_value_AG',
                                                         'INVENTORY','t_value_INVENTORY','p_value_INVENTORY','PPE','t_value_PPE','p_value_PPE',
                                                         'INTANGIBLE_ASSET','t_value_INTANGIBLE_ASSET','p_value_INTANGIBLE_ASSET'])
data_spanning_receivable = pd.DataFrame(columns = receivables,index = ['alpha','t_value','p_value','MKT','t_value_MKT','p_value_MKT','SMB','t_value_SMB','p_value_SMB',
                                                            'HML','t_value_HML','p_value_HML','RMW','t_value_RMW','p_value_RMW','AG','t_value_AG','p_value_AG',
                                                            'INVENTORY','t_value_INVENTORY','p_value_INVENTORY','PPE','t_value_PPE','p_value_PPE',
                                                            'INTANGIBLE_ASSET','t_value_INTANGIBLE_ASSET','p_value_INTANGIBLE_ASSET'])


maxlags = 12
for i in range(len(columns)):
    data = pd.read_csv('../02data/result/factors_{}.csv'.format(columns[i])).dropna().rename({'CMA': columnss[i]}, axis=1)
    data = data[['date',columnss[i]]]
    data = data[data['date'] > '2007-06']
    xvars = ['rm-rf', 'SMB', 'HML', 'RMW', columnss[i]]
    data1 = pd.merge(data, CASH, on='date', how='left').dropna()
    data2 = pd.merge(data, RECEIVABLE, on='date', how='left').dropna()
    # data1 = pd.merge(data1, INTANGIBLE_ASSET, on='date', how='left').dropna()
    # 删除重复行
    # data1 = data1.drop(columns=['Portfolio','r'])
    data1 = data1.drop_duplicates()
    print(data1)
    data2 = data2.drop_duplicates()
    print(data2)
    # 选择一个组合
    # data1 = data1[data1['Portfolio'] == 'SA']
    # data1 = data1.drop_duplicates()
    # print(data1)
    # 在自变量列表中添加常数项
    xvars_with_const = sm.add_constant(data1[xvars])
    model = OLS(data1['CASH'], xvars_with_const).fit()
    res_robust = model.get_robustcov_results(cov_type='HAC', maxlags=maxlags)
    model.params.values[:] = res_robust.params
    model.tvalues.values[:] = res_robust.tvalues
    model.pvalues.values[:] = res_robust.pvalues
    print(model.summary())

    data_spanning_cash.loc['alpha',cashs[i]] = model.params['const']
    data_spanning_cash.loc['t_value',cashs[i]] = model.tvalues['const']
    data_spanning_cash.loc['p_value',cashs[i]] = model.pvalues['const']
    data_spanning_cash.loc['MKT',cashs[i]] = model.params['rm-rf']
    data_spanning_cash.loc['t_value_MKT',cashs[i]] = model.tvalues['rm-rf']
    data_spanning_cash.loc['p_value_MKT',cashs[i]] = model.pvalues['rm-rf']
    data_spanning_cash.loc['SMB',cashs[i]] = model.params['SMB']
    data_spanning_cash.loc['t_value_SMB',cashs[i]] = model.tvalues['SMB']
    data_spanning_cash.loc['p_value_SMB',cashs[i]] = model.pvalues['SMB']
    data_spanning_cash.loc['HML',cashs[i]] = model.params['HML']
    data_spanning_cash.loc['t_value_HML',cashs[i]] = model.tvalues['HML']
    data_spanning_cash.loc['p_value_HML',cashs[i]] = model.pvalues['HML']
    data_spanning_cash.loc['RMW',cashs[i]] = model.params['RMW']
    data_spanning_cash.loc['t_value_RMW',cashs[i]] = model.tvalues['RMW']
    data_spanning_cash.loc['p_value_RMW',cashs[i]] = model.pvalues['RMW']
    data_spanning_cash.loc['{}'.format(columnss[i]),cashs[i]] = model.params[columnss[i]]
    data_spanning_cash.loc['t_value_{}'.format(columnss[i]),cashs[i]] = model.tvalues[columnss[i]]
    data_spanning_cash.loc['p_value_{}'.format(columnss[i]),cashs[i]] = model.pvalues[columnss[i]]

    xvars_with_const = sm.add_constant(data2[xvars])
    model = OLS(data2['RECEIVABLE'], xvars_with_const).fit()
    res_robust = model.get_robustcov_results(cov_type='HAC', maxlags=maxlags)
    model.params.values[:] = res_robust.params
    model.tvalues.values[:] = res_robust.tvalues
    model.pvalues.values[:] = res_robust.pvalues
    print(model.summary())

    data_spanning_receivable.loc['alpha',receivables[i]] = model.params['const']
    data_spanning_receivable.loc['t_value',receivables[i]] = model.tvalues['const']
    data_spanning_receivable.loc['p_value',receivables[i]] = model.pvalues['const']
    data_spanning_receivable.loc['MKT',receivables[i]] = model.params['rm-rf']
    data_spanning_receivable.loc['t_value_MKT',receivables[i]] = model.tvalues['rm-rf']
    data_spanning_receivable.loc['p_value_MKT',receivables[i]] = model.pvalues['rm-rf']
    data_spanning_receivable.loc['SMB',receivables[i]] = model.params['SMB']
    data_spanning_receivable.loc['t_value_SMB',receivables[i]] = model.tvalues['SMB']
    data_spanning_receivable.loc['p_value_SMB',receivables[i]] = model.pvalues['SMB']
    data_spanning_receivable.loc['HML',receivables[i]] = model.params['HML']
    data_spanning_receivable.loc['t_value_HML',receivables[i]] = model.tvalues['HML']
    data_spanning_receivable.loc['p_value_HML',receivables[i]] = model.pvalues['HML']
    data_spanning_receivable.loc['RMW',receivables[i]] = model.params['RMW']
    data_spanning_receivable.loc['t_value_RMW',receivables[i]] = model.tvalues['RMW']
    data_spanning_receivable.loc['p_value_RMW',receivables[i]] = model.pvalues['RMW']
    data_spanning_receivable.loc['{}'.format(columnss[i]),receivables[i]] = model.params[columnss[i]]
    data_spanning_receivable.loc['t_value_{}'.format(columnss[i]),receivables[i]] = model.tvalues[columnss[i]]
    data_spanning_receivable.loc['p_value_{}'.format(columnss[i]),receivables[i]] = model.pvalues[columnss[i]]

print(data_spanning_cash)
print(data_spanning_receivable)
data_spanning_cash.to_csv('../02data/result/data_spanning_cash.csv', encoding='utf-8-sig')
data_spanning_receivable.to_csv('../02data/result/data_spanning_receivable.csv', encoding='utf-8-sig')


# 所有变量一起


