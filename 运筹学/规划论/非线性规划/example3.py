# 使用模拟退火算法

from scipy.optimize import minimize, Bounds, shgo, differential_evolution, basinhopping, rosen, rosen_der, rosen_hess

# 定义目标函数
def objective(x):
    return x[0]**2 + x[1]**2

# 定义约束条件
def eq_constraint(x):
    return x[0] + x[1] + x[2]- 1

def ineq_constraint(x):
   return 0.92*x[0]+0.64*x[1]+0.41*x[2]-0.65 
# 定义优化变量的取值范围和约束条件
b = (0,1)
bounds = [b,b,b]
constraints = [{'type': 'eq', 'fun': eq_constraint},
               {'type': 'ineq', 'fun': ineq_constraint}]

# 使用模拟退火算法求解带有约束的非线性优化问题
result = minimize(objective, [0.3, 0.3,0.3], method='L-BFGS-B', bounds=bounds, constraints=constraints, options={'T0':10000,'maxiter': 10000})

# 输出结果
print(result)