import numpy as np

# 输入判断矩阵A
A = np.array(input('请输入判断矩阵A:'))
n,_=A.shape

class AHP:
    
    def __init__(self,A):
        self.A = A
        self.Max_eig = 0
        
    def weight_1(self): # 用算术平均法求权重
        sum_A = np.sum(A,axis = 0)
        sum_A = np.tile(sum_A,(n,1))
        stand_A = A/sum_A
        weight = np.mean(stand_A,axis = 1)
        return weight

    def weight_2(self): # 用集合平均法求权重
        product_A = np.prod(A,axis = 1)
        product_A = np.power(product_A,1/n)
        weight = product_A/np.sum(product_A)
        return weight

    def weight_3(self): # 用特征值法求权重
        V,D = np.linalg.eig(A)
        self.Max_eig = np.max(D)
        r, c = np.where(D == self.Max_eig)
        return V[:,c]/np.sum(V[:,c])

    def CI_CR(self):
        CI = (self.Max_eig-n)/(n-1)
        RI = np.array([0, 0.0001, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59])
        if n == 2:
            CR = 0
        else:
            CR = CI/RI[n-1]
        return CI,CR 