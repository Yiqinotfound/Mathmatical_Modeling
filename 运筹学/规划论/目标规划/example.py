from gurobipy import Model, GRB


model = Model()


# 定义变量，(测试定义为连续性变量)
x1 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='x1')
x2 = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='x2')
d1_ub = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='d1_ub')
d1_lb = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='d1_lb')
d2_ub = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='d2_ub')
d2_lb = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='d2_lb')
d3_ub = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='d3_ub')
d3_lb = model.addVar(lb=0, vtype=GRB.CONTINUOUS, name='d3_lb')


# 添加约束
model.addConstr(6*x1 + 8*x2 + d3_lb - d3_ub == 48)
model.addConstr(4*x1 + 4*x2 + d2_lb- d2_ub == 36)
model.addConstr(x1 - 2*x2 + d1_lb -d1_ub == 0)
model.addConstr(5*x1 + 10*x2 <= 60)


# 设置目标
model.setObjectiveN(d1_lb, index=0, priority=9)
model.setObjectiveN(d2_ub, index=1, priority=6)
model.setObjectiveN(d3_lb, index=2, priority=3)


model.optimize()


# 打印变量值及目标
for i in model.getVars():
    print(i.varName, '=', i.x)
print('obj = ', 6*x1.x + 8 * x2.x)