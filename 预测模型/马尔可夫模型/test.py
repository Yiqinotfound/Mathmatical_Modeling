from pomegranate import * # type: ignore

# 定义状态和状态转移概率
states = ["Home", "Office"]
transitions = [[0.7, 0.3], [0.4, 0.6]]

# 创建马尔可夫链模型
from pomegranate import DiscreteMarkovChain

# 预测下一个状态的概率分布
probabilities = model.predict_proba(["Home"])
print(probabilities)