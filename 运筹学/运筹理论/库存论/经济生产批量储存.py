import numpy as np
from scipy.optimize import fmin

def EPVSM(D0, cd, cp, cs, P, D):
    # D0为预估市场需求量
    # cd为准不变成本
    # cp为单位产品存贮费用
    # cs为单位产品因短缺而导致的费用
    # P为年产量
    # D为需求速度
    def C(x):
        T, t2 = x
        return 1/T * (D/2/P*cp*(P-D0)*(T-t2)**2 + (P-D)/2/D*cs*t2**2*D + cd)

    x0 = np.array([0, 0])
    x_min = fmin(C, x0)
    Cmin = C(x_min)

    return np.array([x_min[0], x_min[1], Cmin])


