# 使用遗传算法 但是效果很烂
import numpy as np
from scipy.optimize import milp
from scipy.optimize import differential_evolution

# 定义目标函数
def objective(x):
    value = 180*x[0]**2+120*x[1]**2+140*x[2]**2+72*x[0]*x[1]+220*x[0]*x[2]-60*x[1]*x[2]
    if value < 0:
        return 1e5  # return a large value to indicate infeasibility
    else:
        return np.sqrt(value)

# 定义约束条件
def eq_constraint1(x):
    return x[0]+x[1]+x[2]-1

def ineq_constraint2(x):
    return 0.92*x[0]+0.64*x[1]+0.41*x[2]-0.65 

#定义取值范围

b = (0,1)
bounds=[b,b,b]

# 定义适应度函数，将不满足约束条件的解的适应度设为一个较大的值
def fitness(x):
    if eq_constraint1(x)!=0 or ineq_constraint2(x) < 0:
        return 1e10+ objective(x)
    else:
        return objective(x)
    
result = differential_evolution(fitness,bounds,seed=1)

# 输出结果

print(result)
print('x1=',result.x[0])
print('x2=',result.x[1])
print('x3=',result.x[2])
print('目标函数的最小值为：',result.fun)

