"""
研究生院质量评估
"""
import pandas as pd

from indictor_type import *
from topsis import topsis

data = pd.DataFrame(
    {'人均专著': [0.1, 0.2, 0.4, 0.9, 1.2], '生师比': [5, 6, 7, 10, 2], '科研经费': [5000, 6000, 7000, 10000, 400],
     '逾期毕业率': [4.7, 5.6, 6.7, 2.3, 1.8]}, index=['院校' + i for i in list('ABCDE')])

data['生师比'] = dataDirection_3(data['生师比'], 5, 6, 2, 12)  # 区间型
data['逾期毕业率'] = dataDirection_1(data['逾期毕业率'])  # 极小型

res = topsis(data, weight=[0.2, 0.3, 0.4, 0.1])
for i in res:
    print(i)

