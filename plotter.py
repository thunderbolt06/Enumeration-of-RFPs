import networkx as nx
import matplotlib.pyplot as plt
g =nx.Graph()
g.add_edges_from(  [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4),
 (1, 5), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)])
l=[1,2,3,4]
# print(g.has_edge(-1,-2))
x=[1,2,3]
for i in range(2,-1,-1):
    print(x[i])
# print(l[4])
# nx.draw(g, labels=None)
nx.draw_planar(g,labels=None)
plt.savefig("fig.png")
plt.show()