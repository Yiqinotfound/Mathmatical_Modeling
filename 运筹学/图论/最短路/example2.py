import networkx as nx
import matplotlib.pyplot as plt

def bellman_ford(graph, src):
    dist = {node: float('inf') for node in graph.nodes()}
    dist[src] = 0

    for _ in range(len(graph.nodes()) - 1):
        for u, v, w in graph.edges(data=True):
            if dist[u] != float('inf') and dist[u] + w['weight'] < dist[v]:
                dist[v] = dist[u] + w['weight']

    for u, v, w in graph.edges(data=True):
        if dist[u] != float('inf') and dist[u] + w['weight'] < dist[v]:
            print("Graph contains negative weight cycle")
            return

    print("Vertex Distance from Source")
    for node in graph.nodes():
        print("{0}\t\t{1}".format(node, dist[node]))

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=500)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, width=1)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

G = nx.DiGraph()
G.add_weighted_edges_from([(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)])

bellman_ford(G, 0)
