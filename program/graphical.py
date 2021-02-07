"""
数据图形化
"""
import matplotlib.pyplot as plt
import pandas as pd


def graphical(df_data, x_year, fig_path, ind, title, ylabel):
    y_data = []
    for i in range(0, 16, 5):
        y_data.append(df_data.loc[ind + i][2:])

    plt.plot(x_year, y_data[0], label='United Kingdom', linewidth=3, color='b', marker='o', markersize=12)
    plt.plot(x_year, y_data[1], label='United States', linewidth=3, color='c', marker='o', markersize=12)
    plt.plot(x_year, y_data[2], label='Australia', linewidth=3, color='m', marker='o', markersize=12)
    plt.plot(x_year, y_data[3], label='Mexico', linewidth=3, color='y', marker='o', markersize=12)

    plt.legend()  # display label
    plt.grid()
    plt.title(title[ind], fontsize='large', fontweight='bold')
    plt.xlabel('year')
    plt.ylabel(ylabel[ind])
    plt.savefig(fig_path[ind])
    plt.show()


path_data = '../dataset/各国升学率+支出占比+人数占比+论文数量+毕业率_2013-2018.xlsx'

df_data = pd.read_excel(path_data)
x_year = list(df_data.columns[2:])
fig_path = [
    '../images/school_enrollment.png',
    '../images/government_expenditure.png',
    '../images/educational_attainment.png',
    '../images/journal_articles.png',
    '../images/gross_graduation_ratio.png'
]
title = [
    'School enrollment',
    'Government expenditure',
    'Educational attainment',
    'Scientific and technical journal articles',
    'Gross graduation ratio'
]
ylabel = [
    'School enrollment, tertiary (% gross)',
    'Government expenditure per student, tertiary (% of GDP per capita)',
    'Educational attainment, population 25+, total (%)',
    'Scientific and technical journal articles',
    'Gross graduation ratio for tertiary education',
]
for ind in range(5):
    graphical(df_data, x_year, fig_path, ind, title, ylabel)


