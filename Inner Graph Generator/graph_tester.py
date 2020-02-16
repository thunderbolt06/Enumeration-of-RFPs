import networkx as nx
import matplotlib.pyplot as plt

gaf = nx.Graph()
for i in range(int(input())):
    gaf.add_edge(*map(int, input().strip().split(' ')))

print(gaf.edges())

nx.draw_planar(gaf, labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)

plt.show()
