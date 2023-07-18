[matplotlib 文档](https://matplotlib.org/stable/plot_types/index.html)

## plot()函数

```python
x = np.linspace(0.5,3.5,300)
y = np.sin(x)

plt.plot(x,y,color="b",linewidth=2.0,linestyle="--",marker='o',markersize=4,label='Line') # 画图
plt.xlim(1,3) # 设置x轴的范围
plt.ylim(min(y),max(y)) # 设置y轴的范围

# 坐标轴坐标数标签
# 第一个参数为欲替换的x坐标,第二个参数为对应替换坐标的标签

plt.xticks([0,2,4,6,8],[1,2,'a',4,5])
plt.yticks(np.linspace(-1,1,20))

# 坐标轴标签

plt.xlabel('time',fontname='Times New Roman',fontsize=20)
plt.ylabel('value')

# 图片标题
plt.title('plot')

# 图例显示
plt.legend(loc=-1) # (1:右上，2:左上，3:左下，4:右下，-1:自动)

# 网格线显示

plt.grid(axis='x')
plt.grid(axis='y')

# 保存图片

plt.savefig('plot.png',dpi=800)

# 显示
plt.show()
```

- Firgure ： 图像窗口，可以理解为一张画布
- Axed: 子图，带有数据的图像区域，子图ax类似plt，但函数不同

```python
x = np.linspace(0.5,3.5,300)
y = np.sin(x)
z = np.cos(x)

fig,ax = plt.subplots(1,2,figsize=(14,7)) # 1行两列

# 画图
ax[0].plot(x,y)
ax[1].plot(x,z)

ax[0].set_title('sin(x)',fontsize=10)
ax[1].set_title('cos(x)',fontsize=10)

ax[0].set_xlabel('x',fontsize=18)
ax[0].set_ylabel('y',fontsize=18)

ax[1].set_xlabel('x',fontsize=18)
ax[1].set_ylabel('y',fontsize=18)

aax[0].set_xlim(0,16)
ax[0].grid(axis='both')

ax[1].xaxis.set_ticks_params(rotation=45,labelsize=12)  # 设置x轴上数据旋转角度
start,end = ax[1].get_xlim()
ax[1].xaxis.set_ticks(np.arange(start,end,1)) # 根据指定间隔生成x轴刻度 np.arrange(start,end,step)
ax[1].yaxis.tick_right() # 设置y轴显示在右侧
```

## scatter()函数

```python
scatter(x,y,s=10,c='b',marker='+',cmap=None,label='scatter')
```

x: x轴数据
y: y轴数据
s: 点的大小
c: 点的颜色
marker: 点的形状
cmap: 点的颜色映射
label: 点的标签

```python
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
```

## bar()函数

```python
bar(x,y,width=0.8,bottom=None,align='center',color=None,edgecolor=None,label=None,tick_label=['a','b','c'],log=False,orientation='vertical')
```

## hist(x)

在x轴上绘制定量数据的分布特征

x: 一维数组
bins: 直方图的柱数，默认为10

```python
import seaborn as sns
sns.set_palette('hls') # 设置所有图的颜色，使用hls色彩空间
sns.displot(x='heightIn',data=df,bins=20,kde=True) # kde: 是否显示核密度估计图
```

## pie()函数

```python
colors = ['r','y','g','b'] # 饼图颜色
soldNums = [0.05,0.45,0.15,0.35] # 饼图数据
kinds = ['A','B','C','D']  # 饼图标签
plt.pie(soldNums,labels=kinds,colors=colors,startangle=90,shadow=True,explode=(0,0.1,0,0),autopct='%1.1f%%') # explode: 每一块离开中心距离
```

## stackplot() 函数

```python
x = np.linspace(0,2*np.pi,100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.stackplot(x,y1,y2,colors=['r','g'],labels=['sin','cos'])
```

