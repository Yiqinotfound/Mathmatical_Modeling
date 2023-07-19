import numpy as np
from scipy.optimize import fmin_slsqp

def DAOSMC(WT, J, CD, D, K, CP, W, CS):
    # 最大库容量为WT
    # 可用资金上限为J
    # 准不变成本为CD
    # 物资年需求量为行向量D
    # 单价为行向量K
    # 存贮费为行向量CP
    # 占用库存行向量W
    # 缺货损失费用行向量CS
    '''
    该函数的返回值是一个包含Q1，Q2，...，Qn，S1，S2，...，Sn的向量，其中，Q1，Q2，...，Qn是对应于n种物资的生产批次大小，S1，S2，...，Sn是对应于n种物资的库存水平。这些值是带有约束的确定型允许缺货存贮模型的最优解。
    '''
    n = len(D)
    x0 = np.zeros(2*n)

    def f(x):
        Q = x[:n]
        S = x[n:]
        cost = 0
        for i in range(n):
            cost += (CP[i]*(Q[i]-S[i])**2/2/Q[i] + CD*D[i]/Q[i] + CS[i]*S[i]**2/2/Q[i])
        return cost

    def constraint(x):
        Q = x[:n]
        S = x[n:]
        G = -WT
        for i in range(n):
            G += W[i]*(Q[i]-S[i])
        return G

    def jacobian(x):
        Q = x[:n]
        S = x[n:]
        J = np.zeros(2*n)
        for i in range(n):
            J[i] = (CP[i]*(S[i]-Q[i])**2/2/Q[i]**2 - CD*D[i]/Q[i]**2)
            J[n+i] = (CP[i]*(S[i]-Q[i])/Q[i] + CS[i]*S[i]/Q[i]**2 - W[i])
        return J

    # 约束条件
    cons = {'type': 'ineq', 'fun': constraint, 'jac': jacobian}
    # 等式约束
    eq_cons = {'type': 'eq', 'fun': lambda x: np.array([]), 'jac': lambda x: np.array([])}
    # 边界条件
    bounds = [(0, None)]*n + [(None, None)]*n

    # 使用fmin_slsqp函数求解
    x, fval, _, _, _ = fmin_slsqp(f, x0, f_ieqcons=constraint, f_eqcons=lambda x: np.array([]), fprime=jacobian, bounds=bounds, iter=1000, acc=1e-06, full_output=True)

    return x

