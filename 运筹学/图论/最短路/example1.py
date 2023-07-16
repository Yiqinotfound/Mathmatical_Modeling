# 用djkstra算法求解最短路径

import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=5)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=7)
G.add_edge('C', 'D', weight=2)

# 画出图形
pos = nx.spring_layout(G) # 使用spring_layout()函数生成节点的位置
nx.draw(G, pos, with_labels=True) # 使用draw()函数绘制图形
labels = nx.get_edge_attributes(G, 'weight') # 使用get_edge_attributes()函数获取边的权重
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) # 使用draw_networkx_edge_labels()函数在边上显示权重


# 使用Dijkstra算法求解最短路径
path = nx.dijkstra_path(G, 'A', 'D')
print('最短路径为：', path)
length = nx.dijkstra_path_length(G, 'A', 'D')
print('最短路径长度为：', length)

# 画出红色的最短路径
path_edges = list(zip(path, path[1:])) # type: ignore
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

plt.show()



