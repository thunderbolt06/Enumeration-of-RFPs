import networkx as nx
import matplotlib.pyplot as plt
g=nx.Graph()
g.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 4), (2, 3), (3, 4), (4, 5)])
nx.draw_planar(g,labels=None)
plt.show()
print(g.edges)