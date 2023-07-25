# Logistic 模型

# 人口预测模型
# 下面有某地区30年的人口数据，给出该地区人口增长的经典logistic模型

import numpy as np
import matplotlib.pyplot as plt

y = np.array([33815, 33981, 34004, 34165, 34212, 34327,
              34344, 34458, 34498, 34476, 34483, 34488,
              34513, 34497, 34511, 34520, 34507, 34509,
              34521, 34513, 34515, 34517, 34519, 34519,
              34521, 34521, 34523, 34525, 34525, 34527])  # 30 年人口数据

T = np.arange(1, 31)  # 年份-起始年份

# 对数据作线性处理
x = np.zeros(30)
Y = np.zeros(30)
for i in range(30):
    x[i] = np.exp(-i)
    Y[i] = 1 / y[i]

# 计算回归系数
c = np.zeros([30, 1]) + 1
X = np.column_stack((c, x))
b = np.linalg.inv(X.T @ X) @ X.T @ Y
print(b)

# 计算拟合值、离差和误差
z = np.zeros(30)
s = np.zeros(30)
w = np.zeros(30)
for i in range(30):
    z[i] = b[0] + b[1] * x[i]
    s[i] = Y[i] - np.sum(Y) / 30
    w[i] = z[i] - Y[i]

# 计算离差平方和、回归误差平方和和回归平方和
S = np.sum(s ** 2)
Q = np.sum(w ** 2)
U = S - Q

# 计算并输出F检验值
F = 28 * U / Q
print(F)

# 计算非线性回归模型的拟合值
p = np.zeros(30)
for j in range(30):
    p[j] = 1 / (b[0] + b[1] * np.exp(-j))

# 输出非线性回归模型的拟合曲线
plt.plot(T, y, '*', label='实际情况')
plt.plot(T, p, 'r-', label='预测情况')
plt.legend()
plt.show()