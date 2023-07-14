# max f(x)=3x1+5x2
# s.t.  x1       <=4
#            2x2 <=12 
#      3x1 + 2x2 <=16    顶点不是整数
#       x1       >=0
#             x2 >=0
from pulp import *
def getresult(c,con):
    # 设置对象
    prob = LpProblem('Integer_Problem',LpMaximize)
    # 设置两个对象，并设置最小值，且是整数
    x1 =LpVariable("x1",lowBound=0,cat='Integer')
    x2 =LpVariable("x2",lowBound=0,cat='Integer')
    X = [x1,x2]
    
    # 目标函数
    z = 0
    for i in range(len(X)):
        z += X[i]*c[i]
    prob += z
    
    #载入约束变量
    prob += x1 <= con[0]
    prob += 2*x2 <= con[1]
    prob += 3*x1 + 2 * x2 <= con[2]
    
    print('确认整数规划是否输入正确：',prob)
    
    # 求解
    
    status = prob.solve()
    # 输出结果
    print("Status:", LpStatus[prob.status])
    print("Objective value:", value(prob.objective))
    print("x1:", value(x1))
    print("x2:", value(x2))
        
if __name__ == '__main__':
    c = [3,5]
    con = [4 ,12, 16]
    getresult(c,con)
    