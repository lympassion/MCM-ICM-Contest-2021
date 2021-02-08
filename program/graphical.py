"""
数据图形化
"""
import pandas as pd
import matplotlib as plt

path_school_rank = '../dataset/世界排名前100高校占比.xlsx'

"""
国际留学生比例
"""
path_international_stu = '../dataset/国际留学生比例_10.xlsx'
df_international_stu = pd.read_excel(path_international_stu)
print(df_international_stu)
print("columns:", df_international_stu.columns)
print("index:", df_international_stu.index)
# print('I:', df_international_stu[0:2])
# for i in df_international_stu[2:4]:
#     print('i:', i)
#
# plt.plot(df_international_stu["time"],df["money1"],label='money1',linewidth=3,color='r',marker='o',
# markerfacecolor='blue',markersize=12)
