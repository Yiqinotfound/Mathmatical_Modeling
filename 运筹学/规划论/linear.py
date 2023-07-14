from pulp import *
def getresult(c, con):
    '''
    该函数接受两个参数c和con，它们分别是一个列表和一个元组，用于存储线性规划问题的目标函数系数和约束条件。
    '''
    # 设置对象
    prob = LpProblem('myPro', LpMinimize)
    # 设置三个变量，并设置变量最小取值
    x1 = LpVariable("x1", lowBound=0)
    x2 = LpVariable("x2", lowBound=0)
    x3 = LpVariable("x3", lowBound=0)
    X = [x1, x2, x3]
    # 目标函数
    z = 0
    for i in range(len(X)):
        z += X[i]*c[i]
    prob += z
    # 载入约束变量
    prob += x1-2*x2+x3 <= con[0]# 约束条件1
    prob += -4*x1+x2+2*x3 >= con[1] # 约束条件2
    prob += -2*x1+x3 == con[2] # 约束条件3
    print('确认线性规划是否输入正确：',prob)
    # 求解
    status = prob.solve()
    print('\naim ending is ',value(prob.objective))  # 计算结果，prob.objective表示目标函数，value()函数将目标函数的值作为结果返回。
    for i in prob.variables():
        print('\nanswer is ',i.varValue)
if __name__ == '__main__':
    c = [-3,1,1]
    con = [11,3,1]
    getresult(c,con)