# 输入:无项带权图G= (V, E) , 顶点w 输出:回路长度TSPLength
import networkx as nx 
import matplotlib.pyplot as plt

# 邻接矩阵
adj_matrix =[[0, 1, 2, 4, 5],
             [1, 0, 3, 7, 8],
             [2, 3, 0, 9, 6],
             [4, 7, 9, 0, 10],
             [5, 8, 6, 10, 0]]

from typing import List

def tsp(graph, start: int) :
    # 初始化
    n = len(graph)
    visited = [False] * n
    path = [start]
    length = 0

    # 从起点开始遍历
    current = start
    visited[current] = True
    while len(path) < n:
        # 查找与当前顶点邻接的最小代价边
        min_cost = float('inf')
        next_node = None
        for i in range(n):
            if not visited[i] and graph[current][i] < min_cost:
                min_cost = graph[current][i]
                next_node = i

        # 更新路线长度
        path.append(next_node)
        visited[next_node] = True
        length += min_cost

        # 更新
        current = next_node

    # 回到起点
    length += graph[path[-1]][start]
    path.append(start)

    return path

print(tsp(adj_matrix,1))
# 创建一个空的图
G = nx.Graph()

# 添加节点、边和权值
n = len(adj_matrix)
for i in range(n):
    G.add_node(i)

for i in range(n):
    for j in range(i+1,n):
        if adj_matrix[i][j] > 0:
            G.add_edge(i,j,weight=adj_matrix[i][j])            

# 绘制
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_color='r',node_size=500,alpha = 0.5)
nx.draw_networkx_edges(G,pos,edgelist=G.edges(),width=2,edge_color='gray')
nx.draw_networkx_edge_labels(G,pos,edge_labels=nx.get_edge_attributes(G,'weight'))
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif',font_color='white')
plt.axis('off')

# 绘制path

path = tsp(adj_matrix, 1)
path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
path_edges.append((path[-1], path[0])) # 回到起点
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

plt.show()