import networkx as nx # Networkx Library
import numpy as np
import matplotlib.pyplot as plt # Matplot lib

def civfinder(g):
    
    nx.draw_planar(g,labels=None)
    print(g.edges)
    corner_set = []
    for ver in g.nodes:
        if nx.degree(g,ver)==2:
            corner_set.append(ver)
        else:
            if nx.degree(g,ver)==1:
                corner_set.append(ver)
                corner_set.append(ver)
    print(corner_set)
    plt.show()
    return corner_set


# edgeset=[(0, 1), (1, 2), (1, 3), (2, 3), (3, 4),(0,2),(1,4)]
# g=nx.Graph()
# g.add_edges_from(edgeset)
# civfinder(g)
