import pandas as pd
import numpy as np
dataList = pd.read_excel("..//dataset//data.xlsx", sheet_name="Sheet1").values
data = np.array(dataList)
data = data.astype(np.float64) #Int to Float

def maxtrixNormalize(data):
    K = np.power(np.sum(pow(data,2),axis =1),0.5)
    for i in range(0,K.size):
        for j in range(0,data[i].size):
            data[i,j] = data[i,j] / K[i]      #套用矩阵标准化的公式
    return data

def topsis(data):
    listMax = np.array(
        [np.max(data[0, :]), np.max(data[1, :]), np.max(data[2, :]), np.max(data[3, :]), np.max(data[4, :])])  # 获取每一列的最大值
    listMin = np.array(
        [np.min(data[0, :]), np.min(data[1, :]), np.min(data[2, :]), np.min(data[3, :]), np.min(data[4, :])])  # 获取每一列的最小值
    maxList = []  # 存放第i个评价对象与最大值的距离
    minList = []  # 存放第i个评价对象与最小值的距离
    scoreList = []  # 存放评价对象的未归一化得分
    for k in range(0, np.size(data, axis=1)):  # 遍历每一列数据
        maxSum = 0
        minSum = 0
        for q in range(0, 5):  # 有四个指标
            # TODO
            # 权重模型实现后 在此乘对应的权重
            maxSum += np.power(data[q, k] - listMax[q], 2)  # 按每一列计算Di+
            minSum += np.power(data[q, k] - listMin[q], 2)  # 按每一列计算Di-
        maxList.append(pow(maxSum, 0.5))
        minList.append(pow(minSum, 0.5))
        scoreList.append(minList[k] / (minList[k] + maxList[k]))  # 套用计算得分的公式 Si = (Di-) / ((Di+) +(Di-))
    answer = np.array(scoreList)  # 得分归一化
    return (answer / np.sum(answer))
print(maxtrixNormalize(data))
print("归一化后得分如下：")
print(topsis(maxtrixNormalize(data)))
