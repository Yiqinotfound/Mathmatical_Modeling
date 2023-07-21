马尔可夫转移矩阵是描述马尔可夫过程中状态转移概率的矩阵。
在马尔可夫模型中，状态的转移只和当前状态有关，没有记忆性

$$
P = \begin{bmatrix}
p_{11} & p_{12} & \cdots & p_{1n} \\
p_{21} & p_{22} & \cdots & p_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
p_{n1} & p_{n2} & \cdots & p_{nn} \\
\end{bmatrix}
$$

其中，$p_{ij}$表示从状态$i$转移到状态$j$的概率，且满足：

$$
\sum_{j=1}^n p_{ij} = 1, i = 1,2,\cdots,n
$$

