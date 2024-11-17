# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/10/13 20:48
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 04validity_check.py
# @Software: PyCharm


import pandas as pd
import numpy as np
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')

columns =['INV1','INV2','INV3','INV4','INV5','INV6','INV7','INV8','INV9','INV10','INV11']
columnss =['AG','CASH','RECEIVABLE','INVENTORY','PPE','INTANGIBLE_ASSET','CURRENT_LIABILITY','NON_CURRENT_LIABILITY','LIABILITY','RETAINED_EARNINGS','CAPITAL']

data_all = pd.DataFrame(columns = columnss,index = ['alpha','t_value','p_value','significant'])
data_before = pd.DataFrame(columns = columnss,index = ['alpha','t_value','p_value','significant'])
data_after = pd.DataFrame(columns = columnss,index = ['alpha','t_value','p_value','significant'])
i = 0
for inv in columns:
    column = columnss[i]
    data = pd.read_csv('../02data/result/factors_{}.csv'.format(inv)).dropna()
    # data = data[data['Portfolio']=='SC']
    data = data.drop(columns=['Portfolio'])
    data = data.groupby('date').mean().reset_index()
    # 取全样本数据
    data1 = data.dropna()
    # data1 = data1[data1['date'] > '2000-01']
    # 取2007年6月之前的数据
    data2 = data[data['date'] < '2007-06'].dropna()
    # 取2007年6月之后的数据
    data3 = data[data['date']>'2007-06'].dropna()
    # 做冗余性检验，即投资因子CMA与其他四个因子做回归，看alpha是否有显著性
    X = sm.add_constant(data1[['rm-rf', 'SMB', 'HML', 'RMW']])
    model = sm.OLS(data1['CMA'], X).fit()
    data_all.loc['alpha',column] = model.params['const']
    data_all.loc['p_value',column] = model.pvalues['const']
    data_all.loc['t_value',column] = model.tvalues['const']
    if model.pvalues['const'] < 0.01:
        data_all.loc['significant',column] = '1%'
    elif model.pvalues['const'] < 0.05:
        data_all.loc['significant',column] = '5%'
    elif model.pvalues['const'] < 0.1:
        data_all.loc['significant',column] = '10%'
    else:
        data_all.loc['significant',column] = '不显著'

    X = sm.add_constant(data2[['rm-rf', 'SMB', 'HML', 'RMW']])
    model = sm.OLS(data2['CMA'], X).fit()
    data_before.loc['alpha',column] = model.params['const']
    data_before.loc['p_value',column] = model.pvalues['const']
    data_before.loc['t_value',column] = model.tvalues['const']
    if model.pvalues['const'] < 0.01:
        data_before.loc['significant',column] = '1%'
    elif model.pvalues['const'] < 0.05:
        data_before.loc['significant',column] = '5%'
    elif model.pvalues['const'] < 0.1:
        data_before.loc['significant',column] = '10%'
    else:
        data_before.loc['significant',column] = '不显著'

    X = sm.add_constant(data3[['rm-rf', 'SMB', 'HML', 'RMW']])
    model = sm.OLS(data3['CMA'], X).fit()
    data_after.loc['alpha',column] = model.params['const']
    data_after.loc['p_value',column] = model.pvalues['const']
    data_after.loc['t_value',column] = model.tvalues['const']
    if model.pvalues['const'] < 0.01:
        data_after.loc['significant',column] = '1%'
    elif model.pvalues['const'] < 0.05:
        data_after.loc['significant',column] = '5%'
    elif model.pvalues['const'] < 0.1:
        data_after.loc['significant',column] = '10%'
    else:
        data_after.loc['significant',column] = '不显著'
    i += 1

data_all.to_csv('../02data/result/冗余性检验_全样本.csv',index=True,encoding='utf-8-sig')
data_before.to_csv('../02data/result/冗余性检验_2007年6月之前.csv',index=True,encoding='utf-8-sig')
data_after.to_csv('../02data/result/冗余性检验_2007年6月之后.csv',index=True,encoding='utf-8-sig')


# 单独对INV1的每个因子做冗余性检验
factors =['rm-rf','SMB','HML','RMW','CMA']
data_inv1_all = pd.DataFrame(columns = factors
                         ,index = ['alpha','t_value','p_value','significant'])
data_inv1_before = pd.DataFrame(columns = factors
                            ,index = ['alpha','t_value','p_value','significant'])
data_inv1_after = pd.DataFrame(columns = factors
                            ,index = ['alpha','t_value','p_value','significant'])
for factor in factors:
    fac = factors.copy()
    fac.remove(factor)  # 如果是列表
    data = pd.read_csv('../02data/result/factors_INV1.csv').dropna()
    # data = data[data['Portfolio'] == 'SC']
    data = data.drop(columns=['Portfolio'])
    data = data.groupby('date').mean().reset_index()
    # 取全样本数据
    data1 = data.dropna()
    # data1 = data1[data1['date'] > '2000-01']
    # 取2007年6月之前的数据
    data2 = data[data['date']<'2007-06'].dropna()
    # 取2007年6月之后的数据
    data3 = data[data['date']>'2007-06'].dropna()
    # 做冗余性检验，遍历五个因子，分别对剩下的四个因子做回归，看alpha是否有显著性
    X = sm.add_constant(data1[fac])
    model = sm.OLS(data1[factor], X).fit()
    data_inv1_all.loc['alpha',factor] = model.params['const']
    data_inv1_all.loc['p_value',factor] = model.pvalues['const']
    data_inv1_all.loc['t_value',factor] = model.tvalues['const']
    if model.pvalues['const'] < 0.01:
        data_inv1_all.loc['significant',factor] = '1%'
    elif model.pvalues['const'] < 0.05:
        data_inv1_all.loc['significant',factor] = '5%'
    elif model.pvalues['const'] < 0.1:
        data_inv1_all.loc['significant',factor] = '10%'
    else:
        data_inv1_all.loc['significant',factor] = '不显著'

    X = sm.add_constant(data2[fac])
    model = sm.OLS(data2[factor], X).fit()
    # print(model.summary())
    data_inv1_before.loc['alpha',factor] = model.params['const']
    data_inv1_before.loc['p_value',factor] = model.pvalues['const']
    data_inv1_before.loc['t_value',factor] = model.tvalues['const']
    if model.pvalues['const'] < 0.01:
        data_inv1_before.loc['significant',factor] = '1%'
    elif model.pvalues['const'] < 0.05:
        data_inv1_before.loc['significant',factor] = '5%'
    elif model.pvalues['const'] < 0.1:
        data_inv1_before.loc['significant',factor] = '10%'
    else:
        data_inv1_before.loc['significant',factor] = '不显著'

    X = sm.add_constant(data3[fac])
    model = sm.OLS(data3[factor], X).fit()
    data_inv1_after.loc['alpha',factor] = model.params['const']
    data_inv1_after.loc['p_value',factor] = model.pvalues['const']
    data_inv1_after.loc['t_value',factor] = model.tvalues['const']
    if model.pvalues['const'] < 0.01:
        data_inv1_after.loc['significant',factor] = '1%'
    elif model.pvalues['const'] < 0.05:
        data_inv1_after.loc['significant',factor] = '5%'
    elif model.pvalues['const'] < 0.1:
        data_inv1_after.loc['significant',factor] = '10%'
    else:
        data_inv1_after.loc['significant',factor] = '不显著'

data_inv1_all.to_csv('../02data/result/冗余性检验_ag_全样本.csv',index=True,encoding='utf-8-sig')
data_inv1_before.to_csv('../02data/result/冗余性检验_ag_2007年6月之前.csv',index=True,encoding='utf-8-sig')
data_inv1_after.to_csv('../02data/result/冗余性检验_ag_2007年6月之后.csv',index=True,encoding='utf-8-sig')







