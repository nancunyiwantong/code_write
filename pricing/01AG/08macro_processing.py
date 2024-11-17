# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/11/11 11:55
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 08macro_processing.py
# @Software: PyCharm

import pandas as pd
import numpy as np

# 情绪指标
data1 = pd.read_csv('../02data/used/macro/emtion_QX_CICSI.csv')
print(data1)
data1 = data1[['SgnMonth', 'CICSI']].rename(columns={'SgnMonth': 'date', 'CICSI': 'CICSI'})
data1.to_csv('../02data/result/macro_emotion.csv', index=False, encoding='utf-8-sig')


# 金融指标
df1 = pd.read_csv('../02data/csmar/公司文件.csv')
df2 = pd.read_csv('../02data/csmar/月_资产负债表.csv')
print(df1.head())
# 将df1和df2按照时间和证券代码合并，取出资产负债表中的资产总计和负债总计
df1 = df1[['证券代码', '行业代码A','行业名称A','行业代码B','行业名称B','行业代码C','行业名称C']]
df2 = df2[['证券代码', '会计期间', '资产总计', '负债合计']]
df1['证券代码'] = df1['证券代码'].astype(int)
df2['证券代码'] = df2['证券代码'].astype(int)
df1.rename(columns={'证券代码': 'code'}, inplace=True)
df2.rename(columns={'证券代码': 'code', '会计期间': 'date'}, inplace=True)
df = pd.merge(df2, df1, on=['code'], how='left')
print(df.head())
print(df['行业名称A'].value_counts())
df = df[df['行业名称A'] == '金融'][['date', '资产总计', '负债合计', '行业名称B']]
print(df['行业名称B'].value_counts())
df3 = df[df['行业名称B'] == '银行业'][['date', '资产总计', '负债合计']]
df4 = df[df['行业名称B'] == '证券、期货业'][['date', '资产总计', '负债合计']]
# 按时间分组，计算银行业和证券、期货业的资产总计和负债总计的总和
df = df.groupby('date').sum().reset_index()
df3 = df3.groupby('date').sum().reset_index()
df4 = df4.groupby('date').sum().reset_index()
df['leverage1'] = df['资产总计'] / (df['资产总计'] - df['负债合计'])
df3['leverage2'] = df3['资产总计'] / (df3['资产总计'] - df3['负债合计'])
df4['leverage3'] = df4['资产总计'] / (df4['资产总计'] - df4['负债合计'])
df = df[['date', 'leverage1']]
df3 = df3[['date', 'leverage2']]
df4 = df4[['date', 'leverage3']]
# 合并
data2 = pd.merge(df, df3, on='date', how='left')
data2 = pd.merge(data2, df4, on='date', how='left')
data2['date'] = pd.to_datetime(data2['date'])
data2['date'] = data2['date'].dt.to_period('M').astype(str)
data2.to_csv('../02data/result/macro_financial.csv', index=False, encoding='utf-8-sig')


# 生产指标
data3 = pd.read_excel('../02data/used/macro/production_TFP.xlsx')
data3 = data3[['年份', 'TFP_OP']].rename(columns={'年份': 'date', 'TFP_OP': 'TFP'})
# 按照年份分组求平均
data3 = data3.groupby('date').mean().reset_index()
# 扩展到月份
data3['date'] = data3['date'].astype(str)
data3['date'] = data3['date'].map(lambda x: x + '-01')
data3['date'] = pd.to_datetime(data3['date'])
data3['date'] = data3['date'].dt.to_period('M').astype(str)
data3.to_csv('../02data/result/macro_production.csv', index=False, encoding='utf-8-sig')


# 消费指标
# 读取数据
df1 = pd.read_excel('../02data/used/macro/consume1_population.xlsx')
df2 = pd.read_csv('../02data/used/macro/consume2_CPI.csv')
df3 = pd.read_csv('../02data/used/macro/consume3_Retailsale.csv')
print(df3.head())
# 选择并重命名列
df1 = df1[['年份', '总人口（万人）']].rename(columns={'年份': 'date', '总人口（万人）': 'population'})
# 将日期转换为datetime格式，并设置为年度频率
df1['date'] = pd.to_datetime(df1['date'], format='%Y')
# 计算每年的增长率（这里使用相邻两年的差值作为增长率，并加1得到增长率因子）
df1['growth_factor'] = (df1['population'].pct_change() + 1).fillna(1)  # 第一个年份的增长率设为1（即无增长）
# 创建一个空的DataFrame来存储月度数据
start_date = df1['date'].iloc[0].replace(month=1, day=1)
end_date = df1['date'].iloc[-1].replace(month=12, day=31)
monthly_dates = pd.date_range(start=start_date, end=end_date, freq='MS')  # 'MS'表示每月的第一天
monthly_df = pd.DataFrame({'date': monthly_dates})
# 初始化人口数为第一个年度的人口数，并设置索引以便后续计算
monthly_df.set_index('date', inplace=True)
monthly_df['population'] = np.nan
years = df1['date'].dt.to_period('Y').astype(str).tolist()
print(years)
monthly_df.loc[years, 'population'] = df1['population'].values  # 将年度数据复制到对应的年度月份上（这里只设置了每年的第一个月，但后续会通过增长率填充）

# 使用增长率来填充每个月的人口数（这里假设增长率在年内是恒定的）
for i in range(1, len(df1)):
    start_year = df1['date'].iloc[i - 1].year
    end_year = df1['date'].iloc[i].year
    growth_factor = df1['growth_factor'].iloc[i]
    # 对上一年剩余的月份应用增长率（从第二个月开始，因为第一个月已经被直接设置了）
    for month in range(2, 13):
        prev_month_date = pd.to_datetime(f'{start_year}-{month:02d}-01')
        monthly_df.loc[prev_month_date, 'population'] = monthly_df.loc[
                                                            pd.to_datetime(f'{start_year}-01-01'), 'population'] * (
                                                                    growth_factor ** ((prev_month_date - pd.to_datetime(
                                                                f'{start_year}-01-01')).days / 365.25))
    # 对下一年所有的月份应用增长率（从第一个月开始）
    for month in range(1, 13):
        next_month_date = pd.to_datetime(f'{end_year}-{month:02d}-01')
        # 注意：这里我们使用上一年最后已知的人口数和增长率来计算下一年的人口数
        # 这可能不是最准确的方法，因为它没有考虑到年内可能的增长率变化
        # 但由于我们没有更详细的数据，所以这是一个合理的近似
        monthly_df.loc[next_month_date, 'population'] = monthly_df.loc[pd.to_datetime(
            f'{start_year}-12-01') if start_year != end_year else pd.to_datetime(f'{end_year}-01-01') - pd.Timedelta(
            days=1), 'population'] * growth_factor ** ((next_month_date - (
            pd.to_datetime(f'{start_year}-12-01') if start_year != end_year else pd.to_datetime(
                f'{end_year}-01-01') - pd.Timedelta(days=1))).days / 365.25)
# 清理和输出（将索引转换回普通列，并可能进行其他格式化）
monthly_df.reset_index(inplace=True)
monthly_df['date'] = monthly_df['date'].dt.to_period('M').astype(str)
print(monthly_df)  # 打印前几行以查看结果（可能需要根据实际情况调整打印的行数）
monthly_df.to_csv('../02data/result/consume1_population.csv', index=False, encoding='utf-8-sig')
monthly_df = monthly_df.dropna()

df2 = df2[['Staper', 'Epim0101']].rename(columns={'Staper': 'date', 'Epim0101': 'CPI'}).dropna()
df2 = df2.groupby('date').mean().reset_index()

df3 = df3[['Month', 'Retailsale']].rename(columns={'Month': 'date', 'Retailsale': 'retailsale'}).dropna()
# census方法处理季节性调整（待做）
# df3['retailsale'] = df3['retailsale'].apply(lambda x: census(x))
# ### 1. 数据预处理
# # 将 Date 列设置为索引
# df3.set_index('date', inplace=True)
# ### 2. X12 季节调整
# from statsmodels.tsa.x13 import x13_arima_analysis
# # 运行 X12 季节调整
# result = x13_arima_analysis(df3['retailsale'])
# # 获取调整后的季度数据
# adjusted_df3 = result.seasadj
# print(adjusted_df3)

df1['date'] = pd.to_datetime(df1['date'])
df2['date'] = pd.to_datetime(df2['date'])
df3['date'] = pd.to_datetime(df3['date'])
df1['date'] = df1['date'].dt.to_period('M').astype(str)
df2['date'] = df2['date'].dt.to_period('M').astype(str)
df3['date'] = df3['date'].dt.to_period('M').astype(str)
data4 = pd.merge(df3, df2, on='date', how='left')
data4 = pd.merge(data4, df1, on='date', how='left').dropna()
# 计算retailsale的增长率
data4['retailsale'] = data4['retailsale'].fillna(method='bfill')
data4['retailsale'] = data4['retailsale'].astype(float)
data4['retailsale'] = data4['retailsale'].pct_change()
data4 = data4.fillna(method='bfill')
print(data4)
data4 = data4.dropna()
data4['consume'] = data4['retailsale'] / data4['CPI'] / data4['population']
data4 = data4[['date', 'consume']]
# 删除0值
data4 = data4[data4['consume'] != 0]
data4['date'] = pd.to_datetime(data4['date'])
data4['date'] = data4['date'].dt.to_period('M').astype(str)
print(data4)
data4.to_csv('../02data/result/macro_consume.csv', index=False, encoding='utf-8-sig')

# 所有指标合并
data2['date'] = pd.to_datetime(data2['date'])
data2['date'] = data2['date'].dt.to_period('M')
data1['date'] = data1['date'].astype(str)
data2['date'] = data2['date'].astype(str)
data3['date'] = data3['date'].astype(str)
data4['date'] = data4['date'].astype(str)
data = pd.merge(data1, data2, on='date', how='left')
data = pd.merge(data, data3, on='date', how='left')
data = pd.merge(data, data4, on='date', how='left')
# 对每一列进行插值，用后一个非nan值填充
data = data.groupby('date').apply(lambda x: x.fillna(method='bfill'))
print(data)
data.to_csv('../02data/result/macro.csv', index=False, encoding='utf-8-sig')
