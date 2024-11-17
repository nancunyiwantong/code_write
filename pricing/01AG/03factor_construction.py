# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/8/21 19:53
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 03factor_construction.py
# @Software: PyCharm

# import pandas as pd
# import warnings
# warnings.filterwarnings('ignore')
#
# class Factors:
#     def __init__(self):
#         self.df = pd.DataFrame()
#         self.r_df = pd.DataFrame()
#
#         # 划分6个组合
#         self.df_SL = pd.DataFrame()
#         self.df_SN_BM = pd.DataFrame()
#         self.df_BH = pd.DataFrame()
#         self.df_BL = pd.DataFrame()
#         self.df_BN_BM = pd.DataFrame()
#         self.df_BH = pd.DataFrame()
#
#         # 划分12个组合
#         self.df_SR = pd.DataFrame()
#         self.df_SN_OP = pd.DataFrame()
#         self.df_SW = pd.DataFrame()
#         self.df_BR = pd.DataFrame()
#         self.df_BN_OP = pd.DataFrame()
#         self.df_BW = pd.DataFrame()
#
#         self.df_SC1 = pd.DataFrame()
#         self.df_SC2 = pd.DataFrame()
#         self.df_SC3 = pd.DataFrame()
#         self.df_SC4 = pd.DataFrame()
#         self.df_SC5 = pd.DataFrame()
#         self.df_SN_INV = pd.DataFrame()
#         self.df_SN_INV2 = pd.DataFrame()
#         self.df_SN_INV3 = pd.DataFrame()
#         self.df_SN_INV4 = pd.DataFrame()
#         self.df_SN_INV5 = pd.DataFrame()
#         self.df_SA1 = pd.DataFrame()
#         self.df_SA2 = pd.DataFrame()
#         self.df_SA3 = pd.DataFrame()
#         self.df_SA4 = pd.DataFrame()
#         self.df_SA5 = pd.DataFrame()
#         self.df_BC1 = pd.DataFrame()
#         self.df_BC2 = pd.DataFrame()
#         self.df_BC3 = pd.DataFrame()
#         self.df_BC4 = pd.DataFrame()
#         self.df_BC5 = pd.DataFrame()
#         self.df_BN_INV = pd.DataFrame()
#         self.df_BN_INV2 = pd.DataFrame()
#         self.df_BN_INV3 = pd.DataFrame()
#         self.df_BN_INV4 = pd.DataFrame()
#         self.df_BN_INV5 = pd.DataFrame()
#         self.df_BA1 = pd.DataFrame()
#         self.df_BA2 = pd.DataFrame()
#         self.df_BA3 = pd.DataFrame()
#         self.df_BA4 = pd.DataFrame()
#         self.df_BA5 = pd.DataFrame()
#
#         self.R_SL = 0
#         self.R_SN_BM = 0
#         self.R_SH = 0
#         self.R_BL = 0
#         self.R_BN_BM = 0
#         self.R_BH = 0
#
#         self.R_SR = 0
#         self.R_SN_OP = 0
#         self.R_SW = 0
#         self.R_BR = 0
#         self.R_BN_OP = 0
#         self.R_BW = 0
#
#         self.R_SC1 = 0
#         self.R_SC2 = 0
#         self.R_SC3 = 0
#         self.R_SC4 = 0
#         self.R_SC5 = 0
#         self.R_SN_INV = 0
#         self.R_SN_INV2 = 0
#         self.R_SN_INV3 = 0
#         self.R_SN_INV4 = 0
#         self.R_SN_INV5 = 0
#         self.R_SA1 = 0
#         self.R_SA2 = 0
#         self.R_SA3 = 0
#         self.R_SA4 = 0
#         self.R_SA5 = 0
#         self.R_BC1 = 0
#         self.R_BC2 = 0
#         self.R_BC3 = 0
#         self.R_BC4 = 0
#         self.R_BC5 = 0
#         self.R_BN_INV = 0
#         self.R_BN_INV2 = 0
#         self.R_BN_INV3 = 0
#         self.R_BN_INV4 = 0
#         self.R_BN_INV5 = 0
#         self.R_BA1 = 0
#         self.R_BA2 = 0
#         self.R_BA3 = 0
#         self.R_BA4 = 0
#         self.R_BA5 = 0
#
#         self.SMB1 = 0
#         self.SMB2 = 0
#         self.SMB3 = 0
#         self.SMB4 = 0
#         self.SMB5 = 0
#         self.HML = 0
#         self.RMW = 0
#         self.CMA1 = 0
#         self.CMA2 = 0
#         self.CMA3 = 0
#         self.CMA4 = 0
#         self.CMA5 = 0
#
#         self.date = 0
#         self.rf = 0
#         self.rmf = 0
#
#     def update_df(self, df1):
#         self.df = df1
#         self.df[['Size', 'rm-rf', 'rf', 'BM', 'OP', 'INV', 'INV2', 'INV3', 'INV4', 'INV5', 'r']] = \
#             df1[['Size', 'rm-rf', 'rf', 'BM', 'OP', 'INV','INV2', 'INV3', 'INV4', 'INV5', 'r']].values.astype(float)
#         self.df['date'] = df1['date']
#
#     def get_groups(self):
#         '''
#         df的字段为证券代码code、市值Size、账面市值比BM、营运利润率OP、投资风格INV、考虑现金红利再投资的月个股回报率r
#         '''
#
#         # 划分大小市值公司
#         self.df['Size_label'] = self.df['Size'].map(lambda x: 'B' if x >= self.df['Size'].median() else 'S')
#
#         # 划分高、中、低账面市值比公司
#         BM_border_down, BM_border_up = self.df['BM'].quantile([0.3, 0.7])
#         self.df['BM_label'] = self.df['BM'].map(
#             lambda x: 'H' if x >= BM_border_up else ('L' if x <= BM_border_down else 'N'))
#
#         # 划分高、中、低营运利润率
#         OP_border_down, OP_border_up = self.df['OP'].quantile([0.3, 0.7])
#         self.df['OP_label'] = self.df['OP'].map(
#             lambda x: 'R' if x >= OP_border_up else ('W' if x <= OP_border_down else 'N'))
#
#         # 划分投资风格
#         for inv in ['INV', 'INV2', 'INV3', 'INV4', 'INV5']:
#             INV_border_down, INV_border_up = self.df[inv].quantile([0.3, 0.7])
#             self.df['{}_label'.format(inv)] = self.df[inv].map(
#                 lambda x: 'A' if x >= INV_border_up else ('C' if x <= INV_border_down else 'N'))
#
#
#         # 划分6个组合
#         self.df_SL = self.df.query('(Size_label=="S") & (BM_label=="L")')
#         self.df_SN_BM = self.df.query('(Size_label=="S") & (BM_label=="N")')
#         self.df_SH = self.df.query('(Size_label=="S") & (BM_label=="H")')
#         self.df_BL = self.df.query('(Size_label=="B") & (BM_label=="L")')
#         self.df_BN_BM = self.df.query('(Size_label=="B") & (BM_label=="N")')
#         self.df_BH = self.df.query('(Size_label=="B") & (BM_label=="H")')
#
#         # 划分12个组合
#         self.df_SR = self.df.query('(Size_label=="S") & (OP_label=="R")')
#         self.df_SN_OP = self.df.query('(Size_label=="S") & (OP_label=="N")')
#         self.df_SW = self.df.query('(Size_label=="S") & (OP_label=="W")')
#         self.df_BR = self.df.query('(Size_label=="B") & (OP_label=="R")')
#         self.df_BN_OP = self.df.query('(Size_label=="B") & (OP_label=="N")')
#         self.df_BW = self.df.query('(Size_label=="B") & (OP_label=="W")')
#
#         self.df_SC1 = self.df.query('(Size_label=="S") & (INV_label=="C")')
#         self.df_SC2 = self.df.query('(Size_label=="S") & (INV2_label=="C")')
#         self.df_SC3 = self.df.query('(Size_label=="S") & (INV3_label=="C")')
#         self.df_SC4 = self.df.query('(Size_label=="S") & (INV4_label=="C")')
#         self.df_SC5 = self.df.query('(Size_label=="S") & (INV5_label=="C")')
#         self.df_SN_INV = self.df.query('(Size_label=="S") & (INV_label=="N")')
#         self.df_SN_INV2 = self.df.query('(Size_label=="S") & (INV2_label=="N")')
#         self.df_SN_INV3 = self.df.query('(Size_label=="S") & (INV3_label=="N")')
#         self.df_SN_INV4 = self.df.query('(Size_label=="S") & (INV4_label=="N")')
#         self.df_SN_INV5 = self.df.query('(Size_label=="S") & (INV5_label=="N")')
#         self.df_SA1 = self.df.query('(Size_label=="S") & (INV_label=="A")')
#         self.df_SA2 = self.df.query('(Size_label=="S") & (INV2_label=="A")')
#         self.df_SA3 = self.df.query('(Size_label=="S") & (INV3_label=="A")')
#         self.df_SA4 = self.df.query('(Size_label=="S") & (INV4_label=="A")')
#         self.df_SA5 = self.df.query('(Size_label=="S") & (INV5_label=="A")')
#         self.df_BC1 = self.df.query('(Size_label=="B") & (INV_label=="C")')
#         self.df_BC2 = self.df.query('(Size_label=="B") & (INV2_label=="C")')
#         self.df_BC3 = self.df.query('(Size_label=="B") & (INV3_label=="C")')
#         self.df_BC4 = self.df.query('(Size_label=="B") & (INV4_label=="C")')
#         self.df_BC5 = self.df.query('(Size_label=="B") & (INV5_label=="C")')
#         self.df_BN_INV = self.df.query('(Size_label=="B") & (INV_label=="N")')
#         self.df_BN_INV2 = self.df.query('(Size_label=="B") & (INV2_label=="N")')
#         self.df_BN_INV3 = self.df.query('(Size_label=="B") & (INV3_label=="N")')
#         self.df_BN_INV4 = self.df.query('(Size_label=="B") & (INV4_label=="N")')
#         self.df_BN_INV5 = self.df.query('(Size_label=="B") & (INV5_label=="N")')
#         self.df_BA1 = self.df.query('(Size_label=="B") & (INV_label=="A")')
#         self.df_BA2 = self.df.query('(Size_label=="B") & (INV2_label=="A")')
#         self.df_BA3 = self.df.query('(Size_label=="B") & (INV3_label=="A")')
#         self.df_BA4 = self.df.query('(Size_label=="B") & (INV4_label=="A")')
#         self.df_BA5 = self.df.query('(Size_label=="B") & (INV5_label=="A")')
#
#         # # 计算各组流通市值加权收益率
#         self.R_SL = (self.df_SL['r'] * (self.df_SL['Size'] / self.df_SL['Size'].sum()) ).sum()
#         self.R_SN_BM = (self.df_SN_BM['r'] * (self.df_SN_BM['Size'] / self.df_SN_BM['Size'].sum()) ).sum()
#         self.R_SH = (self.df_SH['r'] * (self.df_SH['Size'] / self.df_SH['Size'].sum()) ).sum()
#         self.R_BL = (self.df_BL['r'] * (self.df_BL['Size'] / self.df_BL['Size'].sum()) ).sum()
#         self.R_BN_BM = (self.df_BN_BM['r'] * (self.df_BN_BM['Size'] / self.df_BN_BM['Size'].sum()) ).sum()
#         self.R_BH = (self.df_BH['r'] * (self.df_BH['Size'] / self.df_BH['Size'].sum()) ).sum()
#
#         self.R_SR = (self.df_SR['r'] * (self.df_SR['Size'] / self.df_SR['Size'].sum()) ).sum()
#         self.R_SN_OP = (self.df_SN_OP['r'] * (self.df_SN_OP['Size'] / self.df_SN_OP['Size'].sum()) ).sum()
#         self.R_SW = (self.df_SW['r'] * (self.df_SW['Size'] / self.df_SW['Size'].sum()) ).sum()
#         self.R_BR = (self.df_BR['r'] * (self.df_BR['Size'] / self.df_BR['Size'].sum()) ).sum()
#         self.R_BN_OP = (self.df_BN_OP['r'] * (self.df_BN_OP['Size'] / self.df_BN_OP['Size'].sum()) ).sum()
#         self.R_BW = (self.df_BW['r'] * (self.df_BW['Size'] / self.df_BW['Size'].sum()) ).sum()
#
#         self.R_SC1 = (self.df_SC1['r'] * (self.df_SC1['Size'] / self.df_SC1['Size'].sum()) ).sum()
#         self.R_SC2 = (self.df_SC2['r'] * (self.df_SC2['Size'] / self.df_SC2['Size'].sum()) ).sum()
#         self.R_SC3 = (self.df_SC3['r'] * (self.df_SC3['Size'] / self.df_SC3['Size'].sum()) ).sum()
#         self.R_SC4 = (self.df_SC4['r'] * (self.df_SC4['Size'] / self.df_SC4['Size'].sum()) ).sum()
#         self.R_SC5 = (self.df_SC5['r'] * (self.df_SC5['Size'] / self.df_SC5['Size'].sum()) ).sum()
#         self.R_SN_INV = (self.df_SN_INV['r'] * (self.df_SN_INV['Size'] / self.df_SN_INV['Size'].sum()) ).sum()
#         self.R_SN_INV2 = (self.df_SN_INV2['r'] * (self.df_SN_INV2['Size'] / self.df_SN_INV2['Size'].sum()) ).sum()
#         self.R_SN_INV3 = (self.df_SN_INV3['r'] * (self.df_SN_INV3['Size'] / self.df_SN_INV3['Size'].sum()) ).sum()
#         self.R_SN_INV4 = (self.df_SN_INV4['r'] * (self.df_SN_INV4['Size'] / self.df_SN_INV4['Size'].sum()) ).sum()
#         self.R_SN_INV5 = (self.df_SN_INV5['r'] * (self.df_SN_INV5['Size'] / self.df_SN_INV5['Size'].sum()) ).sum()
#         self.R_SA1 = (self.df_SA1['r'] * (self.df_SA1['Size'] / self.df_SA1['Size'].sum()) ).sum()
#         self.R_SA2 = (self.df_SA2['r'] * (self.df_SA2['Size'] / self.df_SA2['Size'].sum()) ).sum()
#         self.R_SA3 = (self.df_SA3['r'] * (self.df_SA3['Size'] / self.df_SA3['Size'].sum()) ).sum()
#         self.R_SA4 = (self.df_SA4['r'] * (self.df_SA4['Size'] / self.df_SA4['Size'].sum()) ).sum()
#         self.R_SA5 = (self.df_SA5['r'] * (self.df_SA5['Size'] / self.df_SA5['Size'].sum()) ).sum()
#         self.R_BC1 = (self.df_BC1['r'] * (self.df_BC1['Size'] / self.df_BC1['Size'].sum()) ).sum()
#         self.R_BC2 = (self.df_BC2['r'] * (self.df_BC2['Size'] / self.df_BC2['Size'].sum()) ).sum()
#         self.R_BC3 = (self.df_BC3['r'] * (self.df_BC3['Size'] / self.df_BC3['Size'].sum()) ).sum()
#         self.R_BC4 = (self.df_BC4['r'] * (self.df_BC4['Size'] / self.df_BC4['Size'].sum()) ).sum()
#         self.R_BC5 = (self.df_BC5['r'] * (self.df_BC5['Size'] / self.df_BC5['Size'].sum()) ).sum()
#         self.R_BN_INV = (self.df_BN_INV['r'] * (self.df_BN_INV['Size'] / self.df_BN_INV['Size'].sum()) ).sum()
#         self.R_BN_INV2 = (self.df_BN_INV2['r'] * (self.df_BN_INV2['Size'] / self.df_BN_INV2['Size'].sum()) ).sum()
#         self.R_BN_INV3 = (self.df_BN_INV3['r'] * (self.df_BN_INV3['Size'] / self.df_BN_INV3['Size'].sum()) ).sum()
#         self.R_BN_INV4 = (self.df_BN_INV4['r'] * (self.df_BN_INV4['Size'] / self.df_BN_INV4['Size'].sum()) ).sum()
#         self.R_BN_INV5 = (self.df_BN_INV5['r'] * (self.df_BN_INV5['Size'] / self.df_BN_INV5['Size'].sum()) ).sum()
#         self.R_BA1 = (self.df_BA1['r'] * (self.df_BA1['Size'] / self.df_BA1['Size'].sum()) ).sum()
#         self.R_BA2 = (self.df_BA2['r'] * (self.df_BA2['Size'] / self.df_BA2['Size'].sum()) ).sum()
#         self.R_BA3 = (self.df_BA3['r'] * (self.df_BA3['Size'] / self.df_BA3['Size'].sum()) ).sum()
#         self.R_BA4 = (self.df_BA4['r'] * (self.df_BA4['Size'] / self.df_BA4['Size'].sum()) ).sum()
#         self.R_BA5 = (self.df_BA5['r'] * (self.df_BA5['Size'] / self.df_BA5['Size'].sum()) ).sum()
#
#         self.date = pd.DataFrame(self.df_SL['date'])
#         self.rf = pd.DataFrame(self.df_SL['rf'])
#         self.rmf = pd.DataFrame(self.df_SL['rm-rf'])
#
#         def get_portfolio_r(factor):
#             dict = {}
#             dict['SL'] = factor.R_SL
#             dict['SN_BM'] = factor.R_SN_BM
#             dict['SH'] = factor.R_SH
#             dict['BL'] = factor.R_BL
#             dict['BN_BM'] = factor.R_BN_BM
#             dict['BH'] = factor.R_BH
#             dict['SR'] = factor.R_SR
#             dict['SN_OP'] = factor.R_SN_OP
#             dict['SW'] = factor.R_SW
#             dict['BR'] = factor.R_BR
#             dict['BN_OP'] = factor.R_BN_OP
#             dict['BW'] = factor.R_BW
#             dict['SC1'] = factor.R_SC1
#             dict['SC2'] = factor.R_SC2
#             dict['SC3'] = factor.R_SC3
#             dict['SC4'] = factor.R_SC4
#             dict['SC5'] = factor.R_SC5
#             dict['SN_INV'] = factor.R_SN_INV
#             dict['SN_INV2'] = factor.R_SN_INV2
#             dict['SN_INV3'] = factor.R_SN_INV3
#             dict['SN_INV4'] = factor.R_SN_INV4
#             dict['SN_INV5'] = factor.R_SN_INV5
#             dict['SA1'] = factor.R_SA1
#             dict['SA2'] = factor.R_SA2
#             dict['SA3'] = factor.R_SA3
#             dict['SA4'] = factor.R_SA4
#             dict['SA5'] = factor.R_SA5
#             dict['BC1'] = factor.R_BC1
#             dict['BC2'] = factor.R_BC2
#             dict['BC3'] = factor.R_BC3
#             dict['BC4'] = factor.R_BC4
#             dict['BC5'] = factor.R_BC5
#             dict['BN_INV'] = factor.R_BN_INV
#             dict['BN_INV2'] = factor.R_BN_INV2
#             dict['BN_INV3'] = factor.R_BN_INV3
#             dict['BN_INV4'] = factor.R_BN_INV4
#             dict['BN_INV5'] = factor.R_BN_INV5
#             dict['BA1'] = factor.R_BA1
#             dict['BA2'] = factor.R_BA2
#             dict['BA3'] = factor.R_BA3
#             dict['BA4'] = factor.R_BA4
#             dict['BA5'] = factor.R_BA5
#             return dict
#
#         portfolio_r_dict = get_portfolio_r(factor)
#         factor.get_factors()  # 计算因子
#         df_for_regression = pd.DataFrame()
#         date = self.date['date'].tolist()
#         rf = self.rf['rf'].tolist()
#         rmf = self.rmf['rm-rf'].tolist()
#         for portfolio, r in portfolio_r_dict.items():
#             tmp = pd.DataFrame(
#                 {'Portfolio': portfolio,
#                  'SMB1': factor.SMB1,
#                 'SMB2': factor.SMB2,
#                 'SMB3': factor.SMB3,
#                 'SMB4': factor.SMB4,
#                 'SMB5': factor.SMB5,
#                  'HML': factor.HML,
#                  'RMW': factor.RMW,
#                  'CMA1': factor.CMA1,
#                 'CMA2': factor.CMA2,
#                 'CMA3': factor.CMA3,
#                 'CMA4': factor.CMA4,
#                 'CMA5': factor.CMA5,
#                  'r': r,}, index=[0])
#             # 'date': date[0],
#             # 'rf': rf[0],
#             # 'Rm-Rf': rmf[0],
#             df_for_regression = pd.concat([df_for_regression, tmp])
#         return df_for_regression
#
#     def get_factors(self):
#         # 计算SMB、HML、RMW、CMA
#         self.SMB_BM = (self.R_SH + self.R_SN_BM + self.R_SL - self.R_BH - self.R_BN_BM - self.R_BL) / 3
#         self.SMB_OP = (self.R_SR + self.R_SN_OP + self.R_SW - self.R_BR - self.R_BN_OP - self.R_BW) / 3
#         self.SMB_INV = (self.R_SC1 + self.R_SN_INV + self.R_SA1 - self.R_BC1 - self.R_BN_INV - self.R_BA1) / 3
#         self.SMB_INV2= (self.R_SC2 + self.R_SN_INV2 + self.R_SA2 - self.R_BC2 - self.R_BN_INV2 - self.R_BA2) / 3
#         self.SMB_INV3 = (self.R_SC3 + self.R_SN_INV3 + self.R_SA3 - self.R_BC3 - self.R_BN_INV3 - self.R_BA3) / 3
#         self.SMB_INV4 = (self.R_SC4 + self.R_SN_INV4 + self.R_SA4 - self.R_BC4 - self.R_BN_INV4 - self.R_BA4) / 3
#         self.SMB_INV5 = (self.R_SC5 + self.R_SN_INV5 + self.R_SA5 - self.R_BC5 - self.R_BN_INV5 - self.R_BA5) / 3
#         self.SMB1 = (self.SMB_BM + self.SMB_OP + self.SMB_INV) / 3
#         self.SMB2 = (self.SMB_BM + self.SMB_OP + self.SMB_INV2) / 3
#         self.SMB3 = (self.SMB_BM + self.SMB_OP + self.SMB_INV3) / 3
#         self.SMB4 = (self.SMB_BM + self.SMB_OP + self.SMB_INV4) / 3
#         self.SMB5 = (self.SMB_BM + self.SMB_OP + self.SMB_INV5) / 3
#
#         self.HML = (self.R_SH + self.R_BH - self.R_SL - self.R_BL) / 2
#
#         self.RMW = (self.R_SR + self.R_BR - self.R_SW - self.R_BW) / 2
#
#         self.CMA1 = (self.R_SC1 + self.R_BC1 - self.R_SA1 - self.R_BA1) / 2
#         self.CMA2 = (self.R_SC2 + self.R_BC2 - self.R_SA2 - self.R_BA2) / 2
#         self.CMA3 = (self.R_SC3 + self.R_BC3 - self.R_SA3 - self.R_BA3) / 2
#         self.CMA4 = (self.R_SC4 + self.R_BC4 - self.R_SA4 - self.R_BA4) / 2
#         self.CMA5 = (self.R_SC5 + self.R_BC5 - self.R_SA5 - self.R_BA5) / 2
#
#
# if __name__ == '__main__':
#     df = pd.read_csv('../02data/result/metrics.csv').dropna()
#     #删除零值
#     df = df[~df['Size'].isin([0, '0'])]
#     date = df['date'].unique()
#     df_for_regression = pd.DataFrame()
#     for i in range(len(date)):
#         tmp = df[df['date'] == date[i]]
#         factor = Factors()
#         factor.update_df(tmp)
#         tmp1 = factor.get_groups()
#         tmp1['date'] = date[i]
#         tmp1['rf'] = tmp['rf'].tolist()[0]
#         tmp1['rm-rf'] = tmp['rm-rf'].tolist()[0]
#         df_for_regression = pd.concat([df_for_regression, tmp1])
#
#     print(df_for_regression)
#     df_for_regression.dropna(inplace=True)  # 去除缺失值
#     df_for_regression.sort_values('date', inplace=True)
#     df_for_regression = df_for_regression[~df_for_regression['r'].isin([0, '0'])]
#     df_for_regression.to_csv('../02data/result/factors.csv', index=False, encoding='utf-8-sig')







import pandas as pd
import warnings
warnings.filterwarnings('ignore')

class Factors:
    def __init__(self):
        self.df = pd.DataFrame()
        self.r_df = pd.DataFrame()

        # 划分6个组合
        self.df_SL = pd.DataFrame()
        self.df_SN_BM = pd.DataFrame()
        self.df_BH = pd.DataFrame()
        self.df_BL = pd.DataFrame()
        self.df_BN_BM = pd.DataFrame()
        self.df_BH = pd.DataFrame()

        # 划分12个组合
        self.df_SR = pd.DataFrame()
        self.df_SN_OP = pd.DataFrame()
        self.df_SW = pd.DataFrame()
        self.df_BR = pd.DataFrame()
        self.df_BN_OP = pd.DataFrame()
        self.df_BW = pd.DataFrame()

        self.df_SC = pd.DataFrame()
        self.df_SN_INV = pd.DataFrame()
        self.df_SA = pd.DataFrame()
        self.df_BC = pd.DataFrame()
        self.df_BN_INV = pd.DataFrame()
        self.df_BA = pd.DataFrame()

        self.R_SL = 0
        self.R_SN_BM = 0
        self.R_SH = 0
        self.R_BL = 0
        self.R_BN_BM = 0
        self.R_BH = 0

        self.R_SR = 0
        self.R_SN_OP = 0
        self.R_SW = 0
        self.R_BR = 0
        self.R_BN_OP = 0
        self.R_BW = 0

        self.R_SC = 0
        self.R_SN_INV = 0
        self.R_SA = 0
        self.R_BC = 0
        self.R_BN_INV = 0
        self.R_BA = 0

        self.SMB = 0
        self.HML = 0
        self.RMW = 0
        self.CMA = 0

    def update_df(self, df1):
        self.df = df1
        self.df[['Size', 'rm-rf', 'rf', 'BM', 'OP', 'INV', 'r']] = df1[['Size', 'rm-rf', 'rf', 'BM', 'OP', 'INV', 'r']].values.astype(float)
        self.df['date'] = df1['date']

    def get_groups(self):
        '''
        df的字段为证券代码code、市值Size、账面市值比BM、营运利润率OP、投资风格INV、考虑现金红利再投资的月个股回报率r
        '''

        # 划分大小市值公司
        self.df['Size_label'] = self.df['Size'].map(lambda x: 'B' if x >= self.df['Size'].median() else 'S')

        # 划分高、中、低账面市值比公司
        BM_border_down, BM_border_up = self.df['BM'].quantile([0.3, 0.7])
        self.df['BM_label'] = self.df['BM'].map(
            lambda x: 'H' if x >= BM_border_up else ('L' if x <= BM_border_down else 'N'))

        # 划分高、中、低营运利润率
        OP_border_down, OP_border_up = self.df['OP'].quantile([0.3, 0.7])
        self.df['OP_label'] = self.df['OP'].map(
            lambda x: 'R' if x >= OP_border_up else ('W' if x <= OP_border_down else 'N'))

        # 划分投资风格
        INV_border_down, INV_border_up = self.df['INV'].quantile([0.3, 0.7])
        self.df['INV_label'] = self.df['INV'].map(
            lambda x: 'A' if x >= INV_border_up else ('C' if x <= INV_border_down else 'N'))

        # 划分6个组合
        self.df_SL = self.df.query('(Size_label=="S") & (BM_label=="L")')
        print(self.df_SL)
        self.df_SN_BM = self.df.query('(Size_label=="S") & (BM_label=="N")')
        self.df_SH = self.df.query('(Size_label=="S") & (BM_label=="H")')
        self.df_BL = self.df.query('(Size_label=="B") & (BM_label=="L")')
        self.df_BN_BM = self.df.query('(Size_label=="B") & (BM_label=="N")')
        self.df_BH = self.df.query('(Size_label=="B") & (BM_label=="H")')

        # 划分12个组合
        self.df_SR = self.df.query('(Size_label=="S") & (OP_label=="R")')
        self.df_SN_OP = self.df.query('(Size_label=="S") & (OP_label=="N")')
        self.df_SW = self.df.query('(Size_label=="S") & (OP_label=="W")')
        self.df_BR = self.df.query('(Size_label=="B") & (OP_label=="R")')
        self.df_BN_OP = self.df.query('(Size_label=="B") & (OP_label=="N")')
        self.df_BW = self.df.query('(Size_label=="B") & (OP_label=="W")')

        self.df_SC = self.df.query('(Size_label=="S") & (INV_label=="C")')
        self.df_SN_INV = self.df.query('(Size_label=="S") & (INV_label=="N")')
        self.df_SA = self.df.query('(Size_label=="S") & (INV_label=="A")')
        self.df_BC = self.df.query('(Size_label=="B") & (INV_label=="C")')
        self.df_BN_INV = self.df.query('(Size_label=="B") & (INV_label=="N")')
        self.df_BA = self.df.query('(Size_label=="B") & (INV_label=="A")')

        # # 计算各组流通市值加权收益率
        self.R_SL = (self.df_SL['r'] * (self.df_SL['Size'] / self.df_SL['Size'].sum()) ).sum()
        self.R_SN_BM = (self.df_SN_BM['r'] * (self.df_SN_BM['Size'] / self.df_SN_BM['Size'].sum()) ).sum()
        self.R_SH = (self.df_SH['r'] * (self.df_SH['Size'] / self.df_SH['Size'].sum()) ).sum()
        self.R_BL = (self.df_BL['r'] * (self.df_BL['Size'] / self.df_BL['Size'].sum()) ).sum()
        self.R_BN_BM = (self.df_BN_BM['r'] * (self.df_BN_BM['Size'] / self.df_BN_BM['Size'].sum()) ).sum()
        self.R_BH = (self.df_BH['r'] * (self.df_BH['Size'] / self.df_BH['Size'].sum()) ).sum()

        self.R_SR = (self.df_SR['r'] * (self.df_SR['Size'] / self.df_SR['Size'].sum()) ).sum()
        self.R_SN_OP = (self.df_SN_OP['r'] * (self.df_SN_OP['Size'] / self.df_SN_OP['Size'].sum()) ).sum()
        self.R_SW = (self.df_SW['r'] * (self.df_SW['Size'] / self.df_SW['Size'].sum()) ).sum()
        self.R_BR = (self.df_BR['r'] * (self.df_BR['Size'] / self.df_BR['Size'].sum()) ).sum()
        self.R_BN_OP = (self.df_BN_OP['r'] * (self.df_BN_OP['Size'] / self.df_BN_OP['Size'].sum()) ).sum()
        self.R_BW = (self.df_BW['r'] * (self.df_BW['Size'] / self.df_BW['Size'].sum()) ).sum()

        self.R_SC = (self.df_SC['r'] * (self.df_SC['Size'] / self.df_SC['Size'].sum()) ).sum()
        self.R_SN_INV = (self.df_SN_INV['r'] * (self.df_SN_INV['Size'] / self.df_SN_INV['Size'].sum()) ).sum()
        self.R_SA = (self.df_SA['r'] * (self.df_SA['Size'] / self.df_SA['Size'].sum()) ).sum()
        self.R_BC = (self.df_BC['r'] * (self.df_BC['Size'] / self.df_BC['Size'].sum()) ).sum()
        self.R_BN_INV = (self.df_BN_INV['r'] * (self.df_BN_INV['Size'] / self.df_BN_INV['Size'].sum()) ).sum()
        self.R_BA = (self.df_BA['r'] * (self.df_BA['Size'] / self.df_BA['Size'].sum()) ).sum()

        self.date = pd.DataFrame(self.df_SL['date'])
        self.rf = pd.DataFrame(self.df_SL['rf'])
        self.rmf = pd.DataFrame(self.df_SL['rm-rf'])
        print(len(self.date))

        def get_portfolio_r(factor):
            dict = {}
            dict['SL'] = factor.R_SL
            dict['SN_BM'] = factor.R_SN_BM
            dict['SH'] = factor.R_SH
            dict['BL'] = factor.R_BL
            dict['BN_BM'] = factor.R_BN_BM
            dict['BH'] = factor.R_BH
            dict['SR'] = factor.R_SR
            dict['SN_OP'] = factor.R_SN_OP
            dict['SW'] = factor.R_SW
            dict['BR'] = factor.R_BR
            dict['BN_OP'] = factor.R_BN_OP
            dict['BW'] = factor.R_BW
            dict['SC'] = factor.R_SC
            dict['SN_INV'] = factor.R_SN_INV
            dict['SA'] = factor.R_SA
            dict['BC'] = factor.R_BC
            dict['BN_INV'] = factor.R_BN_INV
            dict['BA'] = factor.R_BA
            return dict

        portfolio_r_dict = get_portfolio_r(factor)
        factor.get_factors()  # 计算因子
        df_for_regression = pd.DataFrame()
        for portfolio, r in portfolio_r_dict.items():
            tmp = pd.DataFrame(
                {'Portfolio': portfolio,
                 'SMB': factor.SMB,
                 'HML': factor.HML,
                 'RMW': factor.RMW,
                 'CMA': factor.CMA,
                 'r': r,}, index=[0])
            df_for_regression = pd.concat([df_for_regression, tmp])
        return df_for_regression

    def get_factors(self):
        # 计算SMB、HML、RMW、CMA
        self.SMB_BM = (self.R_SH + self.R_SN_BM + self.R_SL - self.R_BH - self.R_BN_BM - self.R_BL) / 3
        self.SMB_OP = (self.R_SR + self.R_SN_OP + self.R_SW - self.R_BR - self.R_BN_OP - self.R_BW) / 3
        self.SMB_INV = (self.R_SC + self.R_SN_INV + self.R_SA - self.R_BC - self.R_BN_INV - self.R_BA) / 3
        self.SMB = (self.SMB_BM + self.SMB_OP + self.SMB_INV) / 3

        self.HML = (self.R_SH + self.R_BH - self.R_SL - self.R_BL) / 2

        self.RMW = (self.R_SR + self.R_BR - self.R_SW - self.R_BW) / 2

        self.CMA = (self.R_SC + self.R_BC - self.R_SA - self.R_BA) / 2
        # self.df['SMB'] = self.SMB
        # self.df['HML'] = self.HML
        # self.df['RMW'] = self.RMW
        # self.df['CMA'] = self.CMA


if __name__ == '__main__':
    columns =['INV1','INV2','INV3','INV4','INV5','INV6','INV7','INV8','INV9','INV10','INV11']
    for inv in columns:
        df = pd.read_csv('../02data/result/metrics.csv').dropna()
        print(df.shape)
        df['INV'] = df[inv]
        df = df.drop(columns=columns)
        # df = df.groupby('code').apply(lambda x: x.replace(0, pd.NA).fillna(method='bfill'))
        df = df.dropna()
        #删除零值
        df = df[~df['Size'].isin([0, '0'])]
        date = df['date'].unique()
        df_for_regression = pd.DataFrame()
        for i in range(len(date)):
            tmp = df[df['date'] == date[i]]
            factor = Factors()
            factor.update_df(tmp)
            tmp1 = factor.get_groups()
            tmp1['date'] = date[i]
            tmp1['rf'] = tmp['rf'].tolist()[0]
            tmp1['rm-rf'] = tmp['rm-rf'].tolist()[0]
            df_for_regression = pd.concat([df_for_regression, tmp1])

        print(df_for_regression)
        df_for_regression.dropna(inplace=True)
        df_for_regression.sort_values('date', inplace=True)
        df_for_regression = df_for_regression[~df_for_regression['r'].isin([0, '0'])]
        df_for_regression.to_csv('../02data/result/factors_{}.csv'.format(inv), index=False, encoding='utf-8-sig')










