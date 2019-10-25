import networkx as nx
import matplotlib.pyplot as plt
g =nx.Graph()
g.add_edges_from(  
[(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 4), (4, 5), (4, 4), (4, 6), (5, 5), (5, 6), (6, 7), (6, 9), (7, 8), (8, 9)] )
l=[1,2,3,4]
# print(g.has_edge(-1,-2))
x=[1,2,3]
for i in range(2,-1,-1):
    print(x[i])
# print(l[4])
# nx.draw(g, pos=None,labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
nx.draw_planar(g,labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
plt.savefig("fig.png")
plt.show()