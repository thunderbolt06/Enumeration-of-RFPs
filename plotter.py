import networkx as nx
import matplotlib.pyplot as plt
g =nx.Graph()
g.add_edges_from(  [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 2), (1, 6), (1, 7), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (4, 7), (5, 6), (6, 7)]   )
l=[1,2,3,4]
# print(l[4])
nx.draw(g, pos=None,labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
# nx.draw_planar(g)
plt.show()