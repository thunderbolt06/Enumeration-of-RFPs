import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()
g.add_edges_from([(0, 1), (0, 9), (1, 2), (1, 3), (1, 9), (2, 3), (3, 4), (3, 5), (3, 9), (4, 5), (5, 6), (5, 7), (5, 9), (6, 7), (7, 8), (7, 9), (8, 9)])
nx.draw_planar(g,labels=None)
plt.show()
print(g.edges)