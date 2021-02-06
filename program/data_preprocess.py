"""
数据预处理
"""
import pandas as pd

path_school_rank = '../dataset/世界排名前100高校占比.xlsx'


"""
国际留学生比例
"""
path_international_stu = '../dataset/入境学生统计.xlsx'
df_international_stu = pd.read_excel(path_international_stu)
for i in range(2013, 2019):
    df_international_stu[i] = df_international_stu[i] / (df_international_stu[str(i)+'_sum']) * 100
    df_international_stu.drop(columns=str(i)+'_sum', inplace=True)
df_international_stu.drop(columns=2019, inplace=True)
df_international_stu.drop(columns='2019_sum', inplace=True)
df_international_stu.drop(columns=2020, inplace=True)
df_international_stu.drop(columns='2020_sum', inplace=True)
path_international_stu_percentage = '../dataset/国际留学生比例.xlsx'
df_international_stu.to_excel(path_international_stu_percentage)



