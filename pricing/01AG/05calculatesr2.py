# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/10/7 20:59
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 04calculatesr2.py
# @Software: PyCharm

import numpy as np
import pandas as pd
from scipy.stats import t
import statsmodels.api as sm

def barillas_shanken_maxsr_test(data1, data2, modelA_factors, modelB_factors, common_factors=None):
    # Ensure common_factors is a list if provided
    if common_factors is None:
        common_factors = []

        # Combine factors for both models
    fnames1 = modelA_factors + common_factors
    fnames2 = modelB_factors + common_factors

    # Extract the relevant columns from the dataframe
    df_factors1 = data1[fnames1]
    df_factors2 = data2[fnames2]

    # 删除重复行
    # df_factors1 = df_factors1.drop_duplicates()
    # df_factors2 = df_factors2.drop_duplicates()

    # Calculate means and covariances for both sets of factors
    mu1 = df_factors1.mean()
    V1 = df_factors1.cov()

    mu2 = df_factors2.mean()
    V2 = df_factors2.cov()

    # Number of observations (T) and factors (n1, n2)
    T = len(data1)
    n1 = len(fnames1)
    n2 = len(fnames2)

    # Calculate the adjusted maximum Sharpe Ratio squared (thetasq)
    th1 = mu1.dot(np.linalg.inv(V1)).dot(mu1)
    thetasq1 = (th1 * (T - n1 - 2) / T) - (n1 / T)

    th2 = mu2.dot(np.linalg.inv(V2)).dot(mu2)
    thetasq2 = (th2 * (T - n2 - 2) / T) - (n2 / T)

    # Calculate the difference in max Sharpe Ratios
    sr_diff = thetasq1 - thetasq2
    # print(sr_diff)

    # Calculate the U terms for asymptotics (simplified, without loops)
    muV1 = mu1.dot(np.linalg.inv(V1))
    U1 = (df_factors1 - mu1).dot(muV1.reshape(-1, 1))

    muV2 = mu2.dot(np.linalg.inv(V2))
    U2 = (df_factors2 - mu2).dot(muV2.reshape(-1, 1))

    # Calculate dt_squared for the asymptotic variance
    dt_squared = (2 * (U1 - U2) - (U1 ** 2 - U2 ** 2) + sr_diff) ** 2
    # print(dt_squared)
    sample_var = dt_squared.mean()
    std_error = np.sqrt(sample_var / T)

    # Calculate the t-statistic and p-value
    tstat = sr_diff / std_error
    # print(len(tstat))
    df_t = T - np.max([n1, n2]) - 1  # Degrees of freedom for the t-test
    # print(df_t)
    if sr_diff > 0:
        pval = 2 * (1 - t.cdf(tstat, df_t))  # Two-tailed test, but only considering positive difference
    else:
        pval = 2 * t.cdf(-tstat, df_t)  # Same here, but considering negative difference
    # print(pval)
    # Determine significance level with stars
    stars = ''
    if pval < 0.1:
        stars += '*'
    if pval < 0.05:
        stars += '*'
    if pval < 0.01:
        stars += '*'
    if pval > 0.1:
        stars = '不显著'

        # Return results as a dictionary
    results = {
        'sr_diff': sr_diff,
        'dt_squared': dt_squared.mean(),  # Note: returning mean of dt_squared, not the series
        'sample_var': sample_var,
        'std_error': std_error,
        'tstat': tstat,
        'pval': pval,
        'thetasq1': thetasq1,
        'thetasq2': thetasq2,
        'stars': stars,
        'T': T,
        'V1': V1.values,  # Converting to numpy array for consistency
        'V2': V2.values  # Same here
    }

    return sr_diff, tstat, pval, stars

columns =['INV2','INV3','INV4','INV5','INV6','INV7','INV8','INV9','INV10','INV11']
columnss =['CASH','RECEIVABLE','INVENTORY','PPE','INTANGIBLE_ASSET','CURRENT_LIABILITY','NON_CURRENT_LIABILITY','LIABILITY','RETAINED_EARNINGS','CAPITAL']
data_sr2_after = pd.DataFrame(columns = columnss,index = ['sr_diff','pval','stars'])
data_sr2_before = pd.DataFrame(columns = columnss,index = ['sr_diff','pval','stars'])
data_sr2 = pd.DataFrame(columns = columnss,index = ['sr_diff','pval','stars'])
data_sr2_sl = pd.DataFrame(columns = columnss,index = ['sr_diff','pval','stars'])
i = 0
for inv in columns:
    column = columnss[i]
    significant = pd.read_csv('../02data/result/冗余性检验_2007年6月之后.csv').loc['significant',column]
    data1 = pd.read_csv('../02data/result/factors_{}.csv'.format(inv))
    data1 = data1[data1['date']>'2007-06'].dropna()
    if significant == '不显著':
        # 如果不显著，则CMA与其他四个因子做回归，并将残差作为新的因子
        X = sm.add_constant(data1[['rm-rf', 'SMB', 'HML', 'RMW']])
        model = sm.OLS(data1['CMA'], X).fit()
        data1['CMA'] = model.resid
    data1 = data1.dropna()
    data2 = pd.read_csv('../02data/result/factors_{}.csv'.format('INV1')).dropna()
    data2 = data2[data2['date']>'2007-06'].dropna()
    sr_diff, tstat, pval, stars = barillas_shanken_maxsr_test(data1, data2, ['SMB', 'HML', 'RMW', 'CMA','rm-rf'], ['SMB', 'HML', 'RMW', 'CMA','rm-rf'])
    data_sr2_after.loc['sr_diff',column] = sr_diff
    data_sr2_after.loc['pval',column] = pval
    data_sr2_after.loc['stars',column] = stars

    data1 = pd.read_csv('../02data/result/factors_{}.csv'.format(inv))
    data1 = data1[data1['date']<'2007-06'].dropna()
    data2 = pd.read_csv('../02data/result/factors_{}.csv'.format('INV1')).dropna()
    data2 = data2[data2['date']<'2007-06'].dropna()
    sr_diff, tstat, pval, stars = barillas_shanken_maxsr_test(data1, data2, ['SMB', 'HML', 'RMW', 'CMA','rm-rf'], ['SMB', 'HML', 'RMW', 'CMA','rm-rf'])
    data_sr2_before.loc['sr_diff',column] = sr_diff
    data_sr2_before.loc['pval',column] = pval
    data_sr2_before.loc['stars',column] = stars

    data1 = pd.read_csv('../02data/result/factors_{}.csv'.format(inv))
    data1 = data1.dropna()
    data2 = pd.read_csv('../02data/result/factors_{}.csv'.format('INV1')).dropna()
    data2 = data2.dropna()
    sr_diff, tstat, pval, stars = barillas_shanken_maxsr_test(data1, data2, ['SMB', 'HML', 'RMW', 'CMA','rm-rf'], ['SMB', 'HML', 'RMW', 'CMA','rm-rf'])
    data_sr2.loc['sr_diff',column] = sr_diff
    data_sr2.loc['pval',column] = pval
    data_sr2.loc['stars',column] = stars
    i += 1

    data1 = pd.read_csv('../02data/result/factors_{}.csv'.format(inv))
    data1 = data1[data1['date']>'2007-06'].dropna()
    # data1 = data1[data1['Portfolio'].isin(['SC', 'SA', 'SN_INV','SL', 'SH', 'SN_BM','SM', 'SW', 'SN_OP'])].dropna()
    data1 = data1[data1['Portfolio'].isin(['BC', 'BA', 'BN_INV', 'BL', 'BH', 'BN_BM'])].dropna()
    data2 = pd.read_csv('../02data/result/factors_{}.csv'.format('INV1')).dropna()
    data2 = data2[data2['date']>'2007-06'].dropna()
    # data2 = data2[data2['Portfolio'].isin(['SC', 'SA', 'SN_INV','SL', 'SH', 'SN_BM','SM', 'SW', 'SN_OP'])].dropna()
    data2 = data2[data2['Portfolio'].isin(['BC', 'BA', 'BN_INV', 'BL', 'BH', 'BN_BM'])].dropna()
    sr_diff, tstat, pval, stars = barillas_shanken_maxsr_test(data1, data2, ['SMB', 'HML', 'RMW', 'CMA','rm-rf'], ['SMB', 'HML', 'RMW', 'CMA','rm-rf'])
    data_sr2_sl.loc['sr_diff',column] = sr_diff
    data_sr2_sl.loc['pval',column] = pval
    data_sr2_sl.loc['stars',column] = stars


print(data_sr2_after)
print(data_sr2_before)
print(data_sr2)
data_sr2_after.to_csv('../02data/result/data_sr2_after.csv', encoding='utf-8-sig')
data_sr2_before.to_csv('../02data/result/data_sr2_before.csv', encoding='utf-8-sig')
data_sr2.to_csv('../02data/result/data_sr2.csv', encoding='utf-8-sig')
data_sr2_sl.to_csv('../02data/result/data_sr2_sl.csv', encoding='utf-8-sig')



# ag,cash,receivable,inventory,ppe,intangible_asset,current_liability,non_current_liability,liability,留存收益
# inventory 0.23440946
# ppe 1.99
# current_liability 1.9971091
# non_current_liability 1.80804906
# capital留存收益 0.19961456


