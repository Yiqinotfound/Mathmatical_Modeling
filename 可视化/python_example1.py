# import numpy as np
# import matplotlib.pyplot as plt

# N = 100

# # 随机生成两种性别
# np.random.seed(3)
# sex = [np.random.choice(['Male','Female']) for _ in range(N)]

# # 随机生成身高150-200cm
# height = [np.random.uniform(150,200) for _ in range(N)]

# # 随机生成18-30岁
# age = [np.random.randint(18,30) for _ in range(N)]

# m_height = [height[i] for i in range(N) if sex[i] == 'Male']
# w_height = [height[i] for i in range(N) if sex[i] == 'Female']
# m_age = [age[i] for i in range(N) if sex[i] == 'Male']
# w_age = [age[i] for i in range(N) if sex[i] == 'Female']

# plt.scatter(m_age,m_height,color='b')
# plt.scatter(w_age,w_height,color='r')

# plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 导入数据
df = pd.read_csv("scatter_data.csv")

# 拆分不同性别
mdf = df.query("sex=='m'")
fdf = df.query("sex=='f'")

# 绘制男性数据
ax = mdf.plot.scatter(x='ageYear',y='heightIn',c='b',s=10,label='male')

# 绘制女性数据

fdf.plot.scatter(x='ageYear',y='heightIn',c='r',s=30,label='female',ax=ax)
