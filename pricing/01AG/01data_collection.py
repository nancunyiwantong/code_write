# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/8/21 19:52
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 01data_collection.py
# @Software: PyCharm

# 证券代码,会计期间,报表类型,货币资金,其中:客户资金存款,结算备付金,其中：客户备付金,现金及存放中央银行款项,存放同业款项,贵金属,拆出资金净额,交易性金融资产,衍生金融资产,短期投资净额,
# 应收票据净额,应收账款净额,预付款项净额,应收保费净额,应收分保账款净额,应收代位追偿款净额,应收分保合同准备金净额,其中:应收分保未到期责任准备金净额,其中:应收分保未决赔款准备金净额,
# 其中:应收分保寿险责任准备金净额,其中:应收分保长期健康险责任准备金净额,应收利息净额,应收股利净额,其他应收款净额,买入返售金融资产净额,存货净额,一年内到期的非流动资产,存出保证金,
# 其他流动资产,流动资产合计,保户质押贷款净额,定期存款,发放贷款及垫款净额,可供出售金融资产净额,持有至到期投资净额,长期应收款净额,长期股权投资净额,长期债权投资净额,长期投资净额,
# 存出资本保证金,独立账户资产,投资性房地产净额,固定资产净额,在建工程净额,工程物资,固定资产清理,生产性生物资产净额,油气资产净额,无形资产净额,其中:交易席位费,开发支出,商誉净额,
# 长期待摊费用,递延所得税资产,其他非流动资产,非流动资产合计,其他资产,资产总计,短期借款,其中:质押借款,向中央银行借款,吸收存款及同业存放,其中：同业及其他金融机构存放款项,其中：吸收存款,
# 拆入资金,交易性金融负债,衍生金融负债,应付票据,应付账款,预收款项,卖出回购金融资产款,应付手续费及佣金,应付职工薪酬,应交税费,应付利息,应付股利,应付赔付款,应付保单红利,保户储金及投资款,
# 保险合同准备金,其中:未到期责任准备金,其中:未决赔款准备金,其中:寿险责任准备金,其中:长期健康险责任准备金,其他应付款,应付分保账款,代理买卖证券款,代理承销证券款,预收保费,
# 一年内到期的非流动负债,其他流动负债,递延收益-流动负债,流动负债合计,长期借款,独立账户负债,应付债券,长期应付款,专项应付款,长期负债合计,预计负债,递延所得税负债,其他非流动负债,
# 递延收益-非流动负债,非流动负债合计,其他负债,负债合计,实收资本(或股本),其他权益工具,其中：优先股,其中：永续债,其中：其他,资本公积,其中：库存股,盈余公积,一般风险准备,未分配利润,
# 外币报表折算差额,加：未确认的投资损失,交易风险准备,专项储备,其他综合收益,归属于母公司所有者权益合计,少数股东权益,所有者权益合计,负债与所有者权益总计,应收款项融资,合同资产,债权投资,\
#            其他债权投资,其他权益工具投资,其他非流动金融资产,合同负债,使用权资产,租赁负债,是否发生差错更正,差错更正披露日期,证券简称,代理业务资产,代理业务负债,查询成功



import pandas as pd
import numpy as np


data1 = pd.read_csv('../02data/used/stock/月_月个股回报率文件.csv')
data2 = pd.read_excel('../02data/used/market/国债利率季度.xlsx')
data3 = pd.read_csv('../02data/used/company/季_利润表.csv')
data4 = pd.read_csv('../02data/used/company/季_资产负债表.csv')
# data3 = pd.read_csv('../02data/csmar/月_利润表.csv')
# data4 = pd.read_csv('../02data/csmar/月_资产负债表.csv')


data1 = data1[['证券代码', '交易月份', '月个股总市值', '不考虑现金红利再投资的月个股回报率', '考虑现金红利再投资的月个股回报率']]\
    .rename(columns={'证券代码': 'code', '交易月份': 'date', '月个股总市值': 'mv', '不考虑现金红利再投资的月个股回报率': 'r', '考虑现金红利再投资的月个股回报率': 'r_dividend'})
data2.drop(columns=['序号'], inplace=True)
data2 = data2[['日期', '固定利率国债:发行利率:3个月']]\
    .rename(columns={'日期': 'date', '固定利率国债:发行利率:3个月': 'rf'})
data3 = data3[['证券代码', '会计期间', '利润总额']]\
    .rename(columns={'证券代码': 'code', '会计期间': 'date', '利润总额': 'profit'})
data4 = data4[['证券代码', '会计期间', '资产总计',  '所有者权益合计', '货币资金', '应收账款净额', '存货净额', '非流动资产合计', '无形资产净额', '流动负债合计',
               '非流动负债合计', '负债合计','实收资本(或股本)','盈余公积','未分配利润']]\
    .rename(columns={'证券代码': 'code', '会计期间': 'date', '资产总计': 'asset', '所有者权益合计': 'equity', '货币资金': 'cash', '应收账款净额': 'receivable', '存货净额': 'inventory', '非流动资产合计': 'ppe', '无形资产净额': 'intangible_asset',
                     '流动负债合计': 'current_liability', '非流动负债合计': 'non_current_liability', '负债合计': 'liability', '实收资本(或股本)': 'capital', '盈余公积': 'surplus', '未分配利润': 'undistributed_profit'})
data1['code'] = data1['code'].astype(int)
data3['code'] = data3['code'].astype(int)
data4['code'] = data4['code'].astype(int)


# 处理获得无风险利率
# 将data2转换成季度数据
data2['date'] = pd.to_datetime(data2['date'])
data2['date'] = data2['date'].dt.to_period('M')
# data2['date'] = data2['date'].map(lambda x: x[:7])
data2 = data2.groupby('date').mean().reset_index()
data2['date'] = data2['date'].astype(str)
# 把q1, q2, q3, q4转换成月份
# data2['date'] = data2['date'].map(lambda x: x[:4] + '-' + str(int(x[-1]) * 3).zfill(2))
print(data2)
data2.to_csv('../02data/result/无风险利率.csv', index=False, encoding='utf-8-sig')


# 将date转换为月份
data1['date'] = data1['date'].map(lambda x: x[:7])
data2['date'] = data2['date'].map(lambda x: x[:7])
data3['date'] = data3['date'].map(lambda x: x[:7])
data4['date'] = data4['date'].map(lambda x: x[:7])


# 将数据根据年份时间和证券代码合并
data = pd.merge(data1, data3, on=['code', 'date'], how='left')
print(data.shape)
data = pd.merge(data, data4, on=['code', 'date'], how='left')
print(data.shape)
data = pd.merge(data, data2, on='date', how='left')
# 按照code和date分组，对于每一组的每一列，如果有缺失值，那么用后一个非缺失值填充
# data = data.groupby('code').apply(lambda x: x.fillna(method='bfill'))
# data = data.dropna()
print(data)

# 计算rm
dates = data['date'].unique()
print(dates)
rms = []
for date in dates:
    rm = data[data['date'] == date]
    rm = rm['r_dividend']*rm['mv']/rm['mv'].sum()
    rms.append(rm.sum())
data_rm = pd.DataFrame({'date': dates, 'rm': rms})
# 将data_rm转换成季度数据
# data_rm['date'] = pd.to_datetime(data_rm['date'])
# data_rm['date'] = data_rm['date'].dt.to_period('M')
# data_rm = data_rm.groupby('date').mean().reset_index()
# data_rm['date'] = data_rm['date'].astype(str)
# 把q1, q2, q3, q4转换成月份
# data_rm['date'] = data_rm['date'].map(lambda x: x[:4] + '-' + str(int(x[-1]) * 3).zfill(2))
print(data_rm)

data_rm['date'] = data_rm['date'].map(lambda x: x[:7])
data = pd.merge(data, data_rm, on='date')
# 对于无风险利率，如果某个月没有数据，那么用前一个月的数据填充
data['rf'] = data['rf'].fillna(method='ffill')
# 对于每一个code，删除前4个月的数据
data = data.groupby('code').apply(lambda x: x.iloc[4:])
data = data.reset_index(drop=True)
print(data.head())
print(data.shape)
data = data.dropna()
print(data.shape)
data.to_csv('../02data/result/data.csv', index=False, encoding='utf-8-sig')



















