# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/10/7 14:52
# @Author : python顽童--guolei
# @Email : 2508645971@qq.com
# @File : 00测试代码.py
# @Software: PyCharm

# import numpy as np
# import pandas as pd
#
# # 模拟数据设置
# np.random.seed(0)
# n_samples = 1000  # 样本数量
# factors = np.random.randn(n_samples, 6)  # 假设有6个因子，用于模拟不同的模型
# factors_df = pd.DataFrame(factors, columns=['mdate'] + ['factor_' + str(i) for i in range(1, 6)])
#
# # 模拟DOX_EXT变量（用于筛选）
# dox_ext = np.random.choice([0, 1], size=n_samples)
# factors_df['DOX_EXT'] = dox_ext
#
# # 模拟日期变量（用于筛选）
# start_date, end_date = '2020-01-01', '2021-01-01'  # 假设的日期范围
# factors_df['mdate'] = pd.date_range(start=start_date, periods=n_samples, freq='D')[:n_samples]
#
# # 假设的模型和投资组合因子
# ALL_Investment_models = ['modelA', 'modelB', 'modelC']  # 示例模型名称
# models_4_factors = [m + '_4' for m in ALL_Investment_models]
# models_5_factors = [m + '_5' for m in ALL_Investment_models]
# all_models = models_4_factors + models_5_factors
#
# # 假设的因子名称（用于筛选）
# factor_names_4 = ['factor_1', 'factor_2', 'factor_3', 'factor_4']  # 4因子模型
# factor_names_5 = ['factor_1', 'factor_2', 'factor_3', 'factor_4', 'factor_5']  # 5因子模型
#
# # 模拟数据目录和结果文件名
# table_dir = './tables'  # 假设的结果目录
#
# # 初始化结果列表
# results = []
#
# # 遍历doxvar（全样本、中位数以上、中位数以下）
# doxvars = ['full_sample', 'above_median', 'below_median']
# for doxvar in doxvars:
#     # 这里我们简单处理doxvar，不真正分割数据
#     # 假设我们总是使用全样本，并根据DOX_EXT筛选
#     if doxvar == 'full_sample':
#         filtered_df = factors_df
#     elif doxvar == 'above_median':
#         median_value = factors_df['factor_1'].median()  # 假设使用中位数筛选（这里只是示例）
#         filtered_df = factors_df[factors_df['factor_1'] > median_value]
#     elif doxvar == 'below_median':
#         median_value = factors_df['factor_1'].median()  # 假设使用中位数筛选（这里只是示例）
#         filtered_df = factors_df[factors_df['factor_1'] <= median_value]
#
#         # 遍历模型名称
#     for model_name in all_models:
#         # 确定因子数量（4或5）
#         if '_4' in model_name:
#             factors_to_use = factor_names_4
#         else:
#             factors_to_use = factor_names_5
#
#             # 筛选因子数据
#         selected_factors = filtered_df[factors_to_use + ['DOX_EXT', 'mdate']]
#
#         # 根据DOX_EXT和日期范围筛选数据
#         selected_factors = selected_factors[selected_factors['DOX_EXT'] == 1]
#         selected_factors = selected_factors[(selected_factors['mdate'] >= pd.to_datetime(start_date)) &
#                                             (selected_factors['mdate'] <= pd.to_datetime(end_date))]
#
#         # 计算均值向量和协方差矩阵
#         mean_vector = selected_factors[factors_to_use].mean()
#         cov_matrix = selected_factors[factors_to_use].cov()
#
#         # 计算逆协方差矩阵（如果可能）
#         try:
#             inv_cov_matrix = np.linalg.inv(cov_matrix.values)
#         except np.linalg.LinAlgError:
#             print(f"协方差矩阵对于模型{model_name}是奇异的，无法计算其逆。")
#             continue  # 跳过奇异矩阵的情况
#
#         # 计算最大平方夏普比率
#         sr2 = np.dot(np.dot(mean_vector.values.reshape(-1, 1), inv_cov_matrix), mean_vector.values).item()
#
#         # 存储结果
#         results.append({
#             'model_name': model_name,
#             'doxvar': doxvar,
#             'maxsqSR_HXZ': sr2 if '_4' in model_name else None,  # 这里假设HXZ对应4因子模型，实际情况可能不同
#             'maxsqSR_FF5F': sr2 if '_5' in model_name else None  # 假设FF5F对应5因子模型
#         })
#
#     # 将结果保存到DataFrame并导出到CSV文件（模拟Stata的postfile和postclose）
# results_df = pd.DataFrame(results)
# results_df.to_csv(f"{table_dir}/Max_Squared_SR_ALL_Investment_models_results.csv", index=False)
#
# print("结果已保存到CSV文件。")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# import pandas as pd
# import numpy as np
# from statsmodels.regression.linear_model import OLS
# import statsmodels.api as sm
#
#
# CASH = pd.read_csv('../02data/result/factors_INV2.csv')
# CASH = CASH[CASH['date']>'2007-06'][['date','CMA']].dropna()
# CASH = CASH.rename({'CMA': 'CASH'}, axis=1)
# RECEIVABLE = pd.read_csv('../02data/result/factors_INV3.csv')
# RECEIVABLE = RECEIVABLE[RECEIVABLE['date']>'2007-06'][['date','CMA']].dropna()
# RECEIVABLE = RECEIVABLE.rename({'CMA': 'RECEIVABLE'}, axis=1)
# INTANGIBLE_ASSET = pd.read_csv('../02data/result/factors_INV6.csv')
# INTANGIBLE_ASSET = INTANGIBLE_ASSET[INTANGIBLE_ASSET['date']>'2007-06'][['date','CMA']].dropna()
# INTANGIBLE_ASSET = INTANGIBLE_ASSET.rename({'CMA': 'INTANGIBLE_ASSET'}, axis=1)
#
# # columns =['INV1','INV4','INV5','INV6']
# # columnss =['AG','INVENTORY','PPE','INTANGIBLE_ASSET']
# columns =['INV1','INV4','INV5']
# columnss =['AG','INVENTORY','PPE']
#
# data_spanning = pd.DataFrame(columns = columnss,index = ['alpha','t_value','p_value','MKT','t_value_MKT','p_value_MKT','SMB','t_value_SMB','p_value_SMB',
#                                                          'HML','t_value_HML','p_value_HML','RMW','t_value_RMW','p_value_RMW','CASH','t_value_CASH','p_value_CASH',
#                                                          'RECEIVABLE','t_value_RECEIVABLE','p_value_RECEIVABLE',
#                                                          'INTANGIBLE_ASSET','t_value_INTANGIBLE_ASSET','p_value_INTANGIBLE_ASSET'])
#
# yvar = 'CMA'
# maxlags = 12
# xvars = ['rm-rf', 'SMB', 'HML', 'RMW', 'CASH', 'RECEIVABLE','INTANGIBLE_ASSET']
# for i in range(len(columns)):
#     data = pd.read_csv('../02data/result/factors_{}.csv'.format(columns[i])).dropna()
#     data = data[data['date'] > '2007-06']
#     xvars = ['rm-rf', 'SMB', 'HML', 'RMW', 'CASH', 'RECEIVABLE','INTANGIBLE_ASSET']
#     data1 = pd.merge(data, CASH, on='date', how='left').dropna()
#     data1 = pd.merge(data1, RECEIVABLE, on='date', how='left').dropna()
#     data1 = pd.merge(data1, INTANGIBLE_ASSET, on='date', how='left').dropna()
#     # 删除重复行
#     data1 = data1.drop(columns=['Portfolio','r'])
#     data1 = data1.drop_duplicates()
#     print(data1)
#     # 选择一个组合
#     # data1 = data1[data1['Portfolio'] == 'SA']
#     # data1 = data1.drop_duplicates()
#     # print(data1)
#     # 在自变量列表中添加常数项
#     xvars_with_const = sm.add_constant(data1[xvars])
#     model = OLS(data1[yvar], xvars_with_const).fit()
#     res_robust = model.get_robustcov_results(cov_type='HAC', maxlags=maxlags)
#     model.params.values[:] = res_robust.params
#     model.tvalues.values[:] = res_robust.tvalues
#     model.pvalues.values[:] = res_robust.pvalues
#     print(model.summary())
#     data_spanning.loc['alpha',columnss[i]] = model.params['const']
#     data_spanning.loc['t_value',columnss[i]] = model.tvalues['const']
#     data_spanning.loc['p_value',columnss[i]] = model.pvalues['const']
#     data_spanning.loc['MKT',columnss[i]] = model.params['rm-rf']
#     data_spanning.loc['t_value_MKT',columnss[i]] = model.tvalues['rm-rf']
#     data_spanning.loc['p_value_MKT',columnss[i]] = model.pvalues['rm-rf']
#     data_spanning.loc['SMB',columnss[i]] = model.params['SMB']
#     data_spanning.loc['t_value_SMB',columnss[i]] = model.tvalues['SMB']
#     data_spanning.loc['p_value_SMB',columnss[i]] = model.pvalues['SMB']
#     data_spanning.loc['HML',columnss[i]] = model.params['HML']
#     data_spanning.loc['t_value_HML',columnss[i]] = model.tvalues['HML']
#     data_spanning.loc['p_value_HML',columnss[i]] = model.pvalues['HML']
#     data_spanning.loc['RMW',columnss[i]] = model.params['RMW']
#     data_spanning.loc['t_value_RMW',columnss[i]] = model.tvalues['RMW']
#     data_spanning.loc['p_value_RMW',columnss[i]] = model.pvalues['RMW']
#     data_spanning.loc['CASH',columnss[i]] = model.params['CASH']
#     data_spanning.loc['t_value_CASH',columnss[i]] = model.tvalues['CASH']
#     data_spanning.loc['p_value_CASH',columnss[i]] = model.pvalues['CASH']
#     data_spanning.loc['RECEIVABLE',columnss[i]] = model.params['RECEIVABLE']
#     data_spanning.loc['t_value_RECEIVABLE',columnss[i]] = model.tvalues['RECEIVABLE']
#     data_spanning.loc['p_value_RECEIVABLE',columnss[i]] = model.pvalues['RECEIVABLE']
#     data_spanning.loc['INTANGIBLE_ASSET',columnss[i]] = model.params['INTANGIBLE_ASSET']
#     data_spanning.loc['t_value_INTANGIBLE_ASSET',columnss[i]] = model.tvalues['INTANGIBLE_ASSET']
#     data_spanning.loc['p_value_INTANGIBLE_ASSET',columnss[i]] = model.pvalues['INTANGIBLE_ASSET']
#
# print(data_spanning)
# data_spanning.to_csv('../02data/data_spanning.csv', index=False, encoding='utf-8-sig')

# import numpy as np
# import pandas as pd
# import warnings
# warnings.filterwarnings('ignore')
#
# from csmarapi.CsmarService import CsmarService
# from csmarapi.ReportUtil import ReportUtil
# csmar = CsmarService()
# # csmar.login('2020311334@email.cufe.edu.cn', '20021020liu')
# csmar.login('2022302051018@whu.edu.cn', '0246813579Gl')
# # csmar.login('yangyanglee@whu.edu.cn', 'Liyangyang8838')
# # csmar.login('2020311820@email.cufe.edu.cn', 'ZZFzzf1231')
# # csmar.login('1800011778@pku.edu.cn', 'yygwzzjsC1')
# # csmar.login('1900012943@pku.edu.cn', 'cyd0819')
#
# start = '1990-01-01'
# end = '2024-06-01'
#
# # 资产负债表 — 资产负债表
# # 本表数据总记录数：551703条，数据频率：季度，数据开始时间：1990-12-31，数据结束时间：2023-03-31
# # df_list = []
# # for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
# #     data1 = csmar.query(['Stkcd', 'ShortName', 'Accper', 'Typrep', 'IfCorrect', 'DeclareDate', 'A001101000', 'A0d1101101', 'A0d1102000', 'A0d1102101', 'A0b1103000', 'A0b1104000', 'A0b1105000', 'A0f1106000', 'A001107000', 'A0f1108000', 'A001109000', 'A001110000', 'A001111000', 'A001127000', 'A001112000', 'A0i1113000', 'A0i1114000', 'A0i1115000', 'A0i1116000', 'A0i1116101', 'A0i1116201', 'A0i1116301', 'A0i1116401', 'A001119000', 'A001120000', 'A001121000', 'A0f1122000', 'A001123000', 'A001128000', 'A001124000', 'A0d1126000', 'A001125000', 'A001100000', 'A0i1224000', 'A0i1225000', 'A0b1201000', 'A001226000', 'A001202000', 'A001227000', 'A001203000', 'A001204000', 'A001205000', 'A001228000', 'A001229000', 'A001206000', 'A001207000', 'A0i1209000', 'A0i1210000', 'A001211000', 'A001212000', 'A001213000', 'A001214000', 'A001215000', 'A001216000', 'A001217000', 'A001230000', 'A001218000', 'A0d1218101', 'A001219000', 'A001220000', 'A001221000', 'A001222000', 'A0F1224000', 'A001223000', 'A001200000', 'A0f1300000', 'A001000000', 'A002101000', 'A0d2101101', 'A0b2102000', 'A0b2103000', 'A0b2103101', 'A0b2103201', 'A0f2104000', 'A002105000', 'A0f2106000', 'A002107000', 'A002108000', 'A002109000', 'A002128000', 'A0f2110000', 'A0i2111000', 'A002112000', 'A002113000', 'A002114000', 'A002115000', 'A0i2116000', 'A0i2117000', 'A0i2118000', 'A0i2119000', 'A0i2119101', 'A0i2119201', 'A0i2119301', 'A0i2119401', 'A002120000', 'A0i2121000', 'A0d2122000', 'A0d2123000', 'A0i2124000', 'A002125000', 'A002126000', 'A002127000', 'A002100000', 'A002201000', 'A0d2202000', 'A002203000', 'A002211000', 'A002204000', 'A002205000', 'A002206000', 'A002207000', 'A0F2210000', 'A002208000', 'A002209000', 'A002210000', 'A002200000', 'A0f2300000', 'A002000000', 'A003101000', 'A003112000', 'A003112101', 'A003112201', 'A003112301', 'A003102000', 'A003102101', 'A003103000', 'A0f3104000', 'A003105000', 'A003106000', 'A003107000', 'A0F3108000', 'A0F3109000', 'A003111000', 'A003100000', 'A003200000', 'A003000000', 'A004000000'],
# #                         f'Accper LIKE \'%____-{month}-__%\' AND Typrep = \'A\'', 'FS_Combas', start, end)
# #     df1 = pd.DataFrame(data1)
# #     df1.rename({'Stkcd': '证券代码', 'ShortName': '证券简称', 'Accper': '会计期间', 'Typrep': '报表类型', 'IfCorrect': '是否发生差错更正', 'DeclareDate': '差错更正披露日期', 'A001101000': '货币资金', 'A0d1101101': '其中:客户资金存款', 'A0d1102000': '结算备付金', 'A0d1102101': '其中：客户备付金', 'A0b1103000': '现金及存放中央银行款项', 'A0b1104000': '存放同业款项', 'A0b1105000': '贵金属', 'A0f1106000': '拆出资金净额', 'A001107000': '交易性金融资产', 'A0f1108000': '衍生金融资产', 'A001109000': '短期投资净额', 'A001110000': '应收票据净额', 'A001111000': '应收账款净额', 'A001127000': '应收款项融资', 'A001112000': '预付款项净额', 'A0i1113000': '应收保费净额', 'A0i1114000': '应收分保账款净额', 'A0i1115000': '应收代位追偿款净额', 'A0i1116000': '应收分保合同准备金净额', 'A0i1116101': '其中:应收分保未到期责任准备金净额', 'A0i1116201': '其中:应收分保未决赔款准备金净额', 'A0i1116301': '其中:应收分保寿险责任准备金净额', 'A0i1116401': '其中:应收分保长期健康险责任准备金净额', 'A001119000': '应收利息净额', 'A001120000': '应收股利净额', 'A001121000': '其他应收款净额', 'A0f1122000': '买入返售金融资产净额', 'A001123000': '存货净额', 'A001128000': '合同资产', 'A001124000': '一年内到期的非流动资产', 'A0d1126000': '存出保证金', 'A001125000': '其他流动资产', 'A001100000': '流动资产合计', 'A0i1224000': '保户质押贷款净额', 'A0i1225000': '定期存款', 'A0b1201000': '发放贷款及垫款净额', 'A001226000': '债权投资', 'A001202000': '可供出售金融资产净额', 'A001227000': '其他债权投资', 'A001203000': '持有至到期投资净额', 'A001204000': '长期应收款净额', 'A001205000': '长期股权投资净额', 'A001228000': '其他权益工具投资', 'A001229000': '其他非流动金融资产', 'A001206000': '长期债权投资净额', 'A001207000': '长期投资净额', 'A0i1209000': '存出资本保证金', 'A0i1210000': '独立账户资产', 'A001211000': '投资性房地产净额', 'A001212000': '固定资产净额', 'A001213000': '在建工程净额', 'A001214000': '工程物资', 'A001215000': '固定资产清理', 'A001216000': '生产性生物资产净额', 'A001217000': '油气资产净额', 'A001230000': '使用权资产', 'A001218000': '无形资产净额', 'A0d1218101': '其中:交易席位费', 'A001219000': '开发支出', 'A001220000': '商誉净额', 'A001221000': '长期待摊费用', 'A001222000': '递延所得税资产', 'A0F1224000': '代理业务资产', 'A001223000': '其他非流动资产', 'A001200000': '非流动资产合计', 'A0f1300000': '其他资产', 'A001000000': '资产总计', 'A002101000': '短期借款', 'A0d2101101': '其中:质押借款', 'A0b2102000': '向中央银行借款', 'A0b2103000': '吸收存款及同业存放', 'A0b2103101': '其中：同业及其他金融机构存放款项', 'A0b2103201': '其中：吸收存款', 'A0f2104000': '拆入资金', 'A002105000': '交易性金融负债', 'A0f2106000': '衍生金融负债', 'A002107000': '应付票据', 'A002108000': '应付账款', 'A002109000': '预收款项', 'A002128000': '合同负债', 'A0f2110000': '卖出回购金融资产款', 'A0i2111000': '应付手续费及佣金', 'A002112000': '应付职工薪酬', 'A002113000': '应交税费', 'A002114000': '应付利息', 'A002115000': '应付股利', 'A0i2116000': '应付赔付款', 'A0i2117000': '应付保单红利', 'A0i2118000': '保户储金及投资款', 'A0i2119000': '保险合同准备金', 'A0i2119101': '其中:未到期责任准备金', 'A0i2119201': '其中:未决赔款准备金', 'A0i2119301': '其中:寿险责任准备金', 'A0i2119401': '其中:长期健康险责任准备金', 'A002120000': '其他应付款', 'A0i2121000': '应付分保账款', 'A0d2122000': '代理买卖证券款', 'A0d2123000': '代理承销证券款', 'A0i2124000': '预收保费', 'A002125000': '一年内到期的非流动负债', 'A002126000': '其他流动负债', 'A002127000': '递延收益-流动负债', 'A002100000': '流动负债合计', 'A002201000': '长期借款', 'A0d2202000': '独立账户负债', 'A002203000': '应付债券', 'A002211000': '租赁负债', 'A002204000': '长期应付款', 'A002205000': '专项应付款', 'A002206000': '长期负债合计', 'A002207000': '预计负债', 'A0F2210000': '代理业务负债', 'A002208000': '递延所得税负债', 'A002209000': '其他非流动负债', 'A002210000': '递延收益-非流动负债', 'A002200000': '非流动负债合计', 'A0f2300000': '其他负债', 'A002000000': '负债合计', 'A003101000': '实收资本(或股本)', 'A003112000': '其他权益工具', 'A003112101': '其中：优先股', 'A003112201': '其中：永续债', 'A003112301': '其中：其他', 'A003102000': '资本公积', 'A003102101': '其中：库存股', 'A003103000': '盈余公积', 'A0f3104000': '一般风险准备', 'A003105000': '未分配利润', 'A003106000': '外币报表折算差额', 'A003107000': '加：未确认的投资损失', 'A0F3108000': '交易风险准备', 'A0F3109000': '专项储备', 'A003111000': '其他综合收益', 'A003100000': '归属于母公司所有者权益合计', 'A003200000': '少数股东权益', 'A003000000': '所有者权益合计', 'A004000000': '负债与所有者权益总计'},
# #                axis='columns', inplace=True)
# #     df_list.append(df1)
# #
# # df2 = pd.concat(df_list)
# # df2['证券代码'] = df2['证券代码'].astype('int')
# # df2.to_csv('../02data/csmar/月_资产负债表.csv', index=False, encoding='utf-8-sig')
# # print(df2)
#
#
# # 利润表 — 利润表
# # 本表数据总记录数：553302条，数据频率：季度，数据开始时间：1990-12-31，数据结束时间：2023-03-31
# # 注意：该表为累积表，指标由当年1月至统计截止日期计算
# df_list = []
# for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
#     data1 = csmar.query(['Stkcd', 'ShortName', 'Accper', 'Typrep', 'IfCorrect', 'DeclareDate', 'B001100000', 'B001101000', 'Bbd1102000', 'Bbd1102101', 'Bbd1102203', 'B0i1103000', 'B0i1103101', 'B0i1103111', 'B0i1103203', 'B0i1103303', 'B0d1104000', 'B0d1104101', 'B0d1104201', 'B0d1104301', 'B0d1104401', 'B0d1104501', 'B0f1105000', 'B001200000', 'B001201000', 'B0i1202000', 'B0i1203000', 'B0i1203101', 'B0i1203203', 'B0i1204000', 'B0i1204101', 'B0i1204203', 'B0i1205000', 'B0i1206000', 'B001207000', 'B0f1208000', 'B0i1208103', 'B0I1214000', 'B001209000', 'B001210000', 'B001216000', 'B001211000', 'B001211101', 'B001211203', 'B001305000', 'B001302000', 'B001302101', 'B001302201', 'B001303000', 'B001306000', 'B001301000', 'B001212000', 'B001307000', 'B001308000', 'B0f1213000', 'B001304000', 'B001300000', 'B001400000', 'B001400101', 'B001500000', 'B001500101', 'B001500201', 'B001000000', 'B002100000', 'B002200000', 'B002300000', 'B002000000', 'B002000101', 'B002000301', 'B002000201', 'B003000000', 'B004000000', 'B005000000', 'B006000000', 'B006000101', 'B006000103', 'B006000102'],
#                         f'Accper LIKE \'%____-{month}-__%\' AND Typrep = \'A\'', 'FS_Comins', start, end)
#     df1 = pd.DataFrame(data1)
#     df1.rename({'Stkcd': '证券代码', 'ShortName': '证券简称', 'Accper': '会计期间', 'Typrep': '报表类型', 'IfCorrect': '是否发生差错更正', 'DeclareDate': '差错更正披露日期', 'B001100000': '营业总收入', 'B001101000': '营业收入', 'Bbd1102000': '利息净收入', 'Bbd1102101': '利息收入', 'Bbd1102203': '利息支出', 'B0i1103000': '已赚保费', 'B0i1103101': '保险业务收入', 'B0i1103111': '其中：分保费收入', 'B0i1103203': '减：分出保费', 'B0i1103303': '减：提取未到期责任准备金', 'B0d1104000': '手续费及佣金净收入', 'B0d1104101': '其中：代理买卖证券业务净收入', 'B0d1104201': '其中:证券承销业务净收入', 'B0d1104301': '其中：受托客户资产管理业务净收入', 'B0d1104401': '手续费及佣金收入', 'B0d1104501': '手续费及佣金支出', 'B0f1105000': '其他业务收入', 'B001200000': '营业总成本', 'B001201000': '营业成本', 'B0i1202000': '退保金', 'B0i1203000': '赔付支出净额', 'B0i1203101': '赔付支出', 'B0i1203203': '减：摊回赔付支出', 'B0i1204000': '提取保险责任准备金净额', 'B0i1204101': '提取保险责任准备金', 'B0i1204203': '减：摊回保险责任准备金', 'B0i1205000': '保单红利支出', 'B0i1206000': '分保费用', 'B001207000': '税金及附加', 'B0f1208000': '业务及管理费', 'B0i1208103': '减：摊回分保费用', 'B0I1214000': '保险业务手续费及佣金支出', 'B001209000': '销售费用', 'B001210000': '管理费用', 'B001216000': '研发费用', 'B001211000': '财务费用', 'B001211101': '其中：利息费用(财务费用)', 'B001211203': '其中：利息收入(财务费用)', 'B001305000': '其他收益', 'B001302000': '投资收益', 'B001302101': '其中：对联营企业和合营企业的投资收益', 'B001302201': '其中：以摊余成本计量的金融资产终止确认收益', 'B001303000': '汇兑收益', 'B001306000': '净敞口套期收益', 'B001301000': '公允价值变动收益', 'B001212000': '资产减值损失', 'B001307000': '信用减值损失', 'B001308000': '资产处置收益', 'B0f1213000': '其他业务成本', 'B001304000': '其他业务利润', 'B001300000': '营业利润', 'B001400000': '加：营业外收入', 'B001400101': '其中：非流动资产处置利得', 'B001500000': '减：营业外支出', 'B001500101': '其中：非流动资产处置净损益', 'B001500201': '其中：非流动资产处置损失', 'B001000000': '利润总额', 'B002100000': '减：所得税费用', 'B002200000': '未确认的投资损失', 'B002300000': '影响净利润的其他项目', 'B002000000': '净利润', 'B002000101': '归属于母公司所有者的净利润', 'B002000301': '归属于母公司其他权益工具持有者的净利润', 'B002000201': '少数股东损益', 'B003000000': '基本每股收益', 'B004000000': '稀释每股收益', 'B005000000': '其他综合收益(损失)', 'B006000000': '综合收益总额', 'B006000101': '归属于母公司所有者的综合收益', 'B006000103': '归属于母公司其他权益工具持有者的综合收益总额', 'B006000102': '归属少数股东的综合收益'},
#                axis='columns', inplace=True)
#     df_list.append(df1)
#
# df2 = pd.concat(df_list)
# df2['证券代码'] = df2['证券代码'].astype('int')
# df2.to_csv('../02data/csmar/月_利润表.csv', index=False, encoding='utf-8-sig')
# print(df2)

import pandas as pd
data4 = pd.read_csv('../02data/csmar/月_资产负债表.csv')
data4 = data4[['证券代码', '会计期间', '资产总计',  '所有者权益合计', '货币资金', '应收账款净额', '存货净额', '非流动资产合计', '无形资产净额', '流动负债合计',
               '非流动负债合计', '负债合计','实收资本(或股本)','盈余公积','未分配利润']]\
    .rename(columns={'证券代码': 'code', '会计期间': 'date', '资产总计': 'asset', '所有者权益合计': 'equity', '货币资金': 'cash', '应收账款净额': 'receivable', '存货净额': 'inventory', '非流动资产合计': 'ppe', '无形资产净额': 'intangible_asset',
                     '流动负债合计': 'current_liability', '非流动负债合计': 'non_current_liability', '负债合计': 'liability', '实收资本(或股本)': 'capital', '盈余公积': 'surplus', '未分配利润': 'undistributed_profit'})
print(data4.dropna())
data4 = data4.dropna()
date = data4['date'].unique()
# 按顺序排列
date.sort()
print(date)


