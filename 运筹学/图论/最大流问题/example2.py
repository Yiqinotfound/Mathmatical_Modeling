# Edmonds-Karp


import networkx as nx
import matplotlib.pyplot as plt
# 创建一个图
G = nx.DiGraph()

# 添加节点和边
G.add_edge('s', 'a', capacity=3)
G.add_edge('s', 'b', capacity=2)
G.add_edge('a', 'b', capacity=1)
G.add_edge('a', 'c', capacity=3)
G.add_edge('b', 'd', capacity=2)
G.add_edge('c', 'd', capacity=3)
G.add_edge('c', 't', capacity=2)
G.add_edge('d', 't', capacity=3)

# 求解最大流
flow_value, flow_dict = nx.maximum_flow(G,'s','t')

# 生成节点位置
pos = nx.shell_layout(G)

# 绘制有向图
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700)
nx.draw_networkx_nodes(G, pos, nodelist=['s'], node_color='blue', node_size=700)
nx.draw_networkx_nodes(G, pos, nodelist=['t'], node_color='purple', node_size=700)

# 在每条边上标出流量
flow_labels = {(u, v): f"{G[u][v]['capacity']}/{flow_dict[u][v]}" for u, v in G.edges()}
nx.draw_networkx_edge_labels(G,pos,edge_labels=flow_labels,font_size=12,font_color='black')
plt.show()


'''
在 networkx 中，可以使用不同的布局算法来生成节点的位置，以便更好地可视化图形。以下是一些常用的布局算法：
spring_layout：使用 Fruchterman-Reingold 弹簧模型算法布局节点。该算法模拟了一组带有弹簧和斥力的粒子，使得节点之间的距离趋于均匀。
circular_layout：将节点均匀分布在一个圆周上。
random_layout：将节点随机分布在一个矩形区域内。
shell_layout：将节点分布在多个同心圆上，每个圆代表一个层次。
'''