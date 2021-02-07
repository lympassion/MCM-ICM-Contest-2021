"""
数据图形化
"""
import matplotlib.pyplot as plt
import pandas as pd

path_school_rank = '../dataset/世界排名前100高校占比.xlsx'

"""
国际留学生比例
"""
path_inter_stu = '../dataset/国际留学生比例_10.xlsx'
fig_path_inter_stu = '../images/proportion_of_international_students.png'
df_inter_stu = pd.read_excel(path_inter_stu)
print(df_inter_stu)
print("columns:", df_inter_stu.columns[2:])
print("index:", df_inter_stu.index)
print("第一行：", df_inter_stu.loc[0]['country'])
x_inter_stu_year = list(df_inter_stu.columns[2:])
us_inter_stu = df_inter_stu.loc[0][2:]
uk_inter_stu = df_inter_stu.loc[1][2:]
au_inter_stu = df_inter_stu.loc[2][2:]
ca_inter_stu = df_inter_stu.loc[3][2:]
in_inter_stu = df_inter_stu.loc[4][2:]
print(x_inter_stu_year)
print('us_inter_stu:', us_inter_stu)

plt.plot(x_inter_stu_year, us_inter_stu, label='United States', linewidth=3, color='b', marker='o', markersize=12)
plt.plot(x_inter_stu_year, uk_inter_stu, label='United Kingdom', linewidth=3, color='c', marker='o', markersize=12)
plt.plot(x_inter_stu_year, au_inter_stu, label='Australia', linewidth=3, color='m', marker='o', markersize=12)
plt.plot(x_inter_stu_year, ca_inter_stu, label='Canada', linewidth=3, color='y', marker='o', markersize=12)
plt.plot(x_inter_stu_year, in_inter_stu, label='India', linewidth=3, color='g', marker='o', markersize=12)

plt.legend()  # display label
plt.grid()
plt.savefig(fig_path_inter_stu)
plt.show()
