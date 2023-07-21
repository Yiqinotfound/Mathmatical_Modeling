# 简单移动平均只适合作短期预测
# 加权移动平均法，考虑到了信息量不一样
# 趋势移动平均：作二次移动平均（当出现直线增加/减少时）


import numpy as np

def SMA(data, n):
    """
    简单移动平均
    :param data: 数据
    :param n: 移动平均的长度
    :param number: 预测的数据索引
    :return: 预测值
    """
    length = len(data)
    yhat = np.zeros(length - n + 1)
    for i in range(length-n+1):
        yhat[i] = np.sum(data[i:i+n])/n
    
    prediction = yhat[-1]
    s = np.sqrt(np.mean((data[n:] - yhat[:-1]) ** 2))
    return prediction,s

def WMA(data, n, weight):
    """
    加权移动平均
    :param data: 数据
    :param n: 移动平均的长度
    :param weight: 权值
    :return: 预测值和标准差
    """
    factor = weight / np.sum(weight)
    length = len(data)
    yhat = np.zeros(length - n + 1)
    for i in range(length-n+1):
        yhat[i] = np.sum(data[i:i+n]*factor)
    
    err = np.abs(data[n:length] - yhat[:-1] / data[n:length])
    T_err = 1 - np.sum(yhat[:-1]) / np.sum(data[n:length])  # 计算总的平均相对误差
    prediction = yhat[-1]/(1-T_err)
    return prediction, T_err

def 
y1 = np.array([533.8, 574.6, 606.9, 649.8, 705.1, 722.0, 816.4, 892.7, 963.9, 1015.1, 1102.7])
# print(SMA(y1,4))

y2 = np.array([6.35, 6.20, 6.22, 6.66, 7.15, 7.89, 8.72, 8.94, 9.28, 9.8])
w = np.array([1,2,3])
# print(WMA(y2,3,w))
