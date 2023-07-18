# 最大匹配问题，Hungary 算法

# 导入必要的库
import numpy as np             # 用于生成随机权值矩阵
from scipy.optimize import linear_sum_assignment   # 用于求解最大权匹配问题

# 构造一个10x10的随机权值矩阵，分别表示男孩和女孩的吸引力评分
boy_values = np.random.randint(1, 10, size=(10, 10))
girl_values = np.random.randint(1, 10, size=(10, 10))

# 使用linear_sum_assignment函数求解最大权匹配问题
row_ind, col_ind = linear_sum_assignment(-boy_values - girl_values)

# 输出最大权匹配结果
for i in range(len(row_ind)):
    print("男孩{}和女孩{}配对，吸引力评分之和为{}".format(row_ind[i]+1, col_ind[i]+1, -boy_values[row_ind[i], col_ind[i]] - girl_values[row_ind[i], col_ind[i]]))
print("最大匹配吸引力之和为：", boy_values[row_ind, col_ind].sum() + girl_values[row_ind, col_ind].sum())