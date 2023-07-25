import scipy.integrate as spi
import numpy as np
import brewer2mpl
from matplotlib import pyplot as plt
import matplotlib as mpl

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
        该函数接受两个参数：一个名为 y 的一维数组，
        表示微分方程组的解；一个标量 t，表示当前的时间步长。
        该函数返回一个一维数组，表示微分方程组在当前时间步长的变化率。
    '''
    Y=np.zeros(2)
    V = INP
    Y[0] = - beta * V[0] * V[1] + gamma * V[1]
    Y[1] = beta * V[0] * V[1] - gamma * V[1]
    return Y 

t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)

brewer2mpl.print_maps()
### 上面的都不用管
# 绘图




plt.rcParams['font.sans-serif'] = ['SimHei']  
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False    
# 解决Matplotlib坐标轴负号'-'显示为方块的问题

bmap = brewer2mpl.get_map('Set2', 'qualitative', 5)
colors = bmap.mpl_colors

plt.style.use('ggplot') 
plt.plot(RES[:,0], color=colors[0],label='易感染者')
plt.plot(RES[:,1], color=colors[1],label='感染者')
plt.legend(loc=0)
plt.title('SI传染病模型（无出生或死亡）',fontproperties='SimHei',fontsize=14)

plt.xlabel('时间',fontproperties='SimHei',fontsize=10)
plt.ylabel('易感染者和感染者',fontproperties='SimHei',fontsize=10)
plt.show()


