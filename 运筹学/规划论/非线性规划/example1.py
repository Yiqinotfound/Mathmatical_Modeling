# 使用的是顺序最小二乘规划算法

import numpy as np
from scipy.optimize import minimize
# 定义目标函数
def objective(x):
    return np.sqrt(180*x[0]**2+120*x[1]**2+140*x[2]**2+72*x[0]*x[1]+220*x[0]*x[2]-60*x[1]*x[2])
# 定义约束条件
def constraint1(x):
    return x[0]+x[1]+x[2]-1

def constraint2(x):
    return 0.92*x[0]+0.64*x[1]+0.41*x[2]-0.65

# 定义变量的取值范围,
b = (0,1)
bnds = (b,b,b)

# 定义初始值
x0 = np.array([0.1,0.1,0.1])

# 定义约束条件

con1 = {'type':'eq','fun':constraint1}
con2 = {'type':'ineq','fun':constraint2}

# 定义约束条件集合
cons = [con1,con2]

# 求解
sol = minimize(objective,x0,method='SLSQP',bounds=bnds,constraints=cons)

# 输出结果
print(sol)
print('x1=',sol.x[0])
print('x2=',sol.x[1])
print('x3=',sol.x[2])
print('目标函数的最小值为：',sol.fun)
