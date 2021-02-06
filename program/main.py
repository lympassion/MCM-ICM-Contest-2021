"""
研究生院质量评估
"""
import pandas as pd

from program.indictor_type import *

data = pd.DataFrame(
    {'人均专著': [0.1, 0.2, 0.4, 0.9, 1.2], '生师比': [5, 6, 7, 10, 2], '科研经费': [5000, 6000, 7000, 10000, 400],
     '逾期毕业率': [4.7, 5.6, 6.7, 2.3, 1.8]}, index=['院校' + i for i in list('ABCDE')])


# 这里以美国为例（2013~2018）
path_international_stu = '../dataset/入境学生统计.xlsx'
path_school_rank = '../dataset/世界排名前100高校占比.xlsx'


df_international_stu = pd.read_excel(path_international_stu)
# 计算国际留学生比例
for i in range(2013, 2019):
    df_international_stu[i] = df_international_stu[i] / (
                df_international_stu[i] + df_international_stu[str(i)+'_sum'])
    df_international_stu.drop(columns=str(i)+'_sum', inplace=True)
df_international_stu.drop(columns=2019, inplace=True)
df_international_stu.drop(columns='2019_sum', inplace=True)
df_international_stu.drop(columns=2020, inplace=True)
df_international_stu.drop(columns='2020_sum', inplace=True)
path_international_stu_percentage = '../dataset/international_stu_percentage.xlsx'
df_international_stu.to_excel(path_international_stu_percentage)

# df_school_rank = pd.read_excel(path_school_rank)

# print(df_school_rank.columns)
print(df_international_stu.columns)

# print('data:', data)
data['生师比'] = dataDirection_3(data['生师比'], 5, 6, 2, 12)  # 区间型
data['逾期毕业率'] = dataDirection_1(data['逾期毕业率'])  # 极小型

# res = topsis(data, weight=[0.2, 0.3, 0.4, 0.1])
# for i in res:
#     print(i)
