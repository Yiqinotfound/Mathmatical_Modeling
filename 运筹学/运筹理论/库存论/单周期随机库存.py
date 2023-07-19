import numpy as np
from scipy.special import erfinv

def SRIM(kind, U, K, V, x, y):
    # 销售价格U，成本价格K，折扣价格V
    # 作以下三种函数模板
    # kind——kind = 1 对应需求函数满足均匀分布函数， (x,y)为连续区间[x,y]的上下限;
    #         kind = 2 对应需求函数满足标准正态分布函数，x为数学期望，y为标准差；
    #         kind = 3 对应需求函数满足对数正态分布函数，x为数学期望，y为标准差；
    # 返回值为最优进货量
    tmp = (U-K) / (U-V)
    q = -1
    if kind == 1:
        q = x + (y - x) * tmp
    elif kind == 2:
        q = x + y * np.sqrt(2) * erfinv(2*tmp-1)
    elif kind == 3:
        q = x * np.exp(y * np.sqrt(2) * erfinv(2*tmp-1))
    if U < K:
        # 若售价小于成本，无法盈利，返回特殊值-1
        q = -1
    return q