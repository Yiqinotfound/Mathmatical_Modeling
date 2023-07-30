import numpy as np
def zeroMean(dataMat):
    meanVal = np.mean(dataMat, axis=0)  # 按列求均值，即求各个特征的均值
    newData = dataMat - meanVal
    return newData, meanVal


def pca(dataMat, percentage=0.99):
    newData, meanVal = zeroMean(dataMat)
    covMat = np.cov(newData, rowvar=0)  # 求协方差矩阵
    eigVals, eigVects = np.linalg.eig(np.mat(covMat))  # 求特征值和特征向量,特征向量是按列放的，即一列代表一个特征向量
    eigValIndice = np.argsort(eigVals)  # 特征值从小到大排序
    n = percentage2n(eigVals, percentage)
    n_eigValIndice = eigValIndice[-1:-(n + 1):-1]  # 最大的n个特征值的下标
    n_eigVect = eigVects[:, n_eigValIndice]  # 最大的n个特征值对应的特征向量
    lowDDataMat = newData * n_eigVect  # 低维特征空间的数据
    reconMat = (lowDDataMat * n_eigVect.T) + meanVal  # 重构数据
    return n_eigVect, lowDDataMat
def percentage2n(eigVals, percentage):
    sortArray = np.sort(eigVals)  # 升序
    sortArray = sortArray[-1::-1]  # 逆转，即降序
    arraySum = sum(sortArray)
    tmpSum = 0
    num = 0
    for i in sortArray:
        tmpSum += i
        num += 1
        if tmpSum >= arraySum * percentage:
            return num
import openpyxl
import numpy
xls = openpyxl.load_workbook("Myfile.xlsx")  # "Myfile.xlsx"为xlsx文件名，可根据实际情况更改或加入路径
sheet = xls.worksheets[0]
datax = list(sheet['B2':'I320'])  # 为数据区域
for i in range(319):  # 319为数据行数，即采样点数
    datax[i] = list(datax[i])
    for j in range(8):  # 8为数据列数，即属性数
        datax[i][j] = datax[i][j].value
coeff, lowDDataMat = pca(datax)
print(coeff)
print(lowDDataMat)