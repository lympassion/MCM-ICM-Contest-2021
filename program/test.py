"""
数据图形化
"""
import matplotlib.pyplot as plt
import pandas as pd

path_data = '../dataset/各国升学率+支出占比+人数占比+论文数量+毕业率_2013-2018.xlsx'
df_data = pd.read_excel(path_data)
print(df_data)
# print("columns:", df_data.columns)
# print("index:", df_data.index)
# print("第一行：", df_data.loc[0]['country'])

"""
School enrollment, tertiary (% gross)
"""

fig_path_school_enrollment_tertiary = '../images/school_enrollment_tertiary.png'


# x_inter_stu_year = list(df_inter_stu.columns[2:])
# us_inter_stu = df_inter_stu.loc[0][2:]
# uk_inter_stu = df_inter_stu.loc[1][2:]
# au_inter_stu = df_inter_stu.loc[2][2:]
# ca_inter_stu = df_inter_stu.loc[3][2:]
# in_inter_stu = df_inter_stu.loc[4][2:]
# print(x_inter_stu_year)
# print('us_inter_stu:', us_inter_stu)
#
# plt.plot(x_inter_stu_year, us_inter_stu, label='United States', linewidth=3, color='b', marker='o', markersize=12)
# plt.plot(x_inter_stu_year, uk_inter_stu, label='United Kingdom', linewidth=3, color='c', marker='o', markersize=12)
# plt.plot(x_inter_stu_year, au_inter_stu, label='Australia', linewidth=3, color='m', marker='o', markersize=12)
# plt.plot(x_inter_stu_year, ca_inter_stu, label='Canada', linewidth=3, color='y', marker='o', markersize=12)
# plt.plot(x_inter_stu_year, in_inter_stu, label='India', linewidth=3, color='g', marker='o', markersize=12)
#
# plt.legend()  # display label
# plt.grid()
# plt.savefig(fig_path_inter_stu)
# plt.show()
