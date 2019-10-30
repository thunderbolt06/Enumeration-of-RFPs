# import flask
# import json
import networkx as nx
# import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
g = nx.Graph()


# graph declaration --------
ed = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)]

g.add_edges_from(ed)
# nx.draw_planar(g)
# plt.show(g)

# initial edges -----------
e= 3*(len(g)+4)-7-4-g.size()


# edges removal ---------------------------
for i in g.nodes():
    a= g.copy()
    a.remove_node(i)
    if nx.number_connected_components(a)>1:
        e= e- 2
    else:
        if g.degree(i)<4:
            e = e - (4-g.degree(i))
        else:
            f = g.subgraph([n for n in g.neighbors(i)])
            app=0
            for n2 in f.nodes():
                if f.degree(n2) is not 2:
                    app=1
            if app==1:
                e= e-1
print("edges remaining ",e)


# combinations ----------------------
x = []
if e==0:
    print("unique soultion")
    x=1
else:
    for i in g.nodes():
        if g.degree(i)<4:
            x.append(g.degree(i)-1)
                 




