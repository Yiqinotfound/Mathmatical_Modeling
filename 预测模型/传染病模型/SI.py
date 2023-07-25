# 1. 在疾病传播期内所考察地区的总人数$N$不变。人群分为**易感染者**和**已感染者**两类，以下简称**健康人**和**病人**。时刻$t$这两类人在总人数所占的比例分别记作$s(t)$和$i(t)$。
# 2. 每个病人每天有效接触的平均人数为$\lambda$，$\lambda$称为**日接触率**，当病人与健康人有效接触时，健康人就会变为病人。

import scipy.integrate as spi
import numpy as np
from matplotlib import pyplot as plt
import brewer2mpl

plt.rcParams['font.sans-serif'] = ['SimHei']  
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False    
# 解决Matplotlib坐标轴负号'-'显示为方块的问题


beta=1.4247 # 疾病从感染者传播到易感染者的可能性，单位时间内

gamma=0 #gamma是康复率，在SI模型中，gamma等于零

I0=1e-6 #I0是感染个体的初始比例

ND=70 #ND是总时间步数

TS=1.0 # TS是时间步长
INPUT = (1.0-I0, I0)

def diff_eqs(INP,t): 
    '''
    主要方程组
    parameters:
         INP:易感染者和感染者的比例
            t:时间
    return:
            Y[0]:易感染者的变化率
            Y[1]:感染者的变化率
    '''
    Y=np.zeros((2))
    V = INP
    Y[0] = - beta * V[0] * V[1] + gamma * V[1]
    Y[1] = beta * V[0] * V[1] - gamma * V[1]
    return Y 

t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)
"""RES是每个时间步骤中易感染者和感染者的比例结果"""
print(RES)

#绘图
# Define a color map using the brewer2mpl library

plt.style.use('ggplot') # 
plt.plot(RES[:,0], color='deepskyblue',label='易感染者')
plt.plot(RES[:,1], color='deeppink',label='感染者')
plt.legend(loc=0)
plt.title('SI传染病模型（无出生或死亡）',fontproperties='SimHei',fontsize=14)

plt.xlabel('时间',fontproperties='SimHei',fontsize=10)
plt.ylabel('易感染者和感染者',fontproperties='SimHei',fontsize=10)
plt.show()