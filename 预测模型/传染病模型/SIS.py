import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi
import brewer2mpl

plt.rcParams['font.sans-serif'] = ['SimHei']  
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False    
# 解决Matplotlib坐标轴负号'-'显示为方块的问题




import scipy.integrate as spi
import numpy as np
import pylab as pl

beta=1.4247 # 感染率
gamma=0.5 # 治愈率
I0=1e-6
ND=70
TS=1.0
INPUT = (1.0-I0, I0,0)


def diff_eqs(y,t):
    dy=np.zeros(3)
    dy[0] = -beta*y[0]*y[1]
    dy[1] = beta*y[0]*y[1] -gamma*y[1]
    dy[2] = gamma*y[1]
    return dy

t_start = 0.0; t_end = ND; t_inc = TS
t_range = np.arange(t_start, t_end+t_inc, t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)
t_start = 0
t_end = ND 
t_inc= TS 

t_range = np.arange(t_start,t_end+t_inc,t_inc)
RES = spi.odeint(diff_eqs,INPUT,t_range)

print(RES)

# 绘图
bmap = brewer2mpl.get_map('Set2', 'qualitative', 5)
colors = bmap.mpl_colors

plt.style.use('ggplot') # 
plt.plot(RES[:,0], color=colors[0],label='易感染者')
plt.plot(RES[:,1], color=colors[1],label='感染者')
plt.plot(RES[:,2], color=colors[2],label='获得免疫或死亡者')
plt.legend(loc=0)
plt.title('SIS传染病模型',fontproperties='SimHei',fontsize=14)

plt.xlabel('时间',fontproperties='SimHei',fontsize=10)
plt.ylabel('易感染者、感染者、获得免疫或死亡者',fontproperties='SimHei',fontsize=10)
plt.show()