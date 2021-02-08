import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

"""
数据线性拟合 y = a + bx
"""
import matplotlib.pyplot as plt
import pandas as pd


def fitAndPredict(y, x, fig_path, ind, title, ylabel):
    '''
    create a model and fit it
    y = a + bx
    '''
    model = LinearRegression()
    model = model.fit(x, y)

    score = model.score(x, y)
    a = model.intercept_  # a
    b = model.coef_  # b

    # future
    x_append = x
    for j in range(2019, 2026):
        x_append = np.append(x_append, [[j]], axis=0)

    y_fit = model.predict(x_append)

    plt.plot(x, y, label='Actuality', linewidth=3, color='y', marker='o', markersize=12)
    plt.plot(x_append, y_fit, label='Prediction', linewidth=3, color='b', marker='o', markersize=12)

    plt.legend()  # display label
    plt.grid()
    plt.title(title[ind], fontsize='large', fontweight='bold')
    plt.xlabel('year')
    plt.ylabel(ylabel[ind])
    plt.savefig(fig_path[ind])
    plt.show()
    return a, b, score


path_data = '../dataset/各国升学率+支出占比+人数占比+论文数量+毕业率_2013-2018.xlsx'

df_data = pd.read_excel(path_data)
x = list(df_data.columns[2:])
x = np.array(x).reshape((-1, 1))
fig_path = [
    '../images/fit_school_enrollment.png',
    '../images/fit_government_expenditure.png',
    '../images/fit_educational_attainment.png',
    '../images/fit_journal_articles.png',
    '../images/fit_gross_graduation_ratio.png'
]
title = [
    'School enrollment fitting',
    'Government expenditure fitting',
    'Educational attainment fitting',
    'Scientific and technical journal articles fitting',
    'Gross graduation ratio fitting'
]
ylabel = [
    'School enrollment, tertiary (% gross)',
    'Government expenditure per student, tertiary (% of GDP per capita)',
    'Educational attainment, population 25+, total (%)',
    'Scientific and technical journal articles',
    'Gross graduation ratio for tertiary education',
]

linear_val = []
for ind in range(5):
    y = list(df_data.loc[ind + 15][2:])
    linear_val.append(fitAndPredict(y, x, fig_path, ind, title, ylabel))

for i in range(5):
    print(linear_val[i][2])


