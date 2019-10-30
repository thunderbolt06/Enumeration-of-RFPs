import flask
import json
import networkx as nx
# import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism import GraphMatcher

g = nx.Graph()
# graph declaration --------
ed = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 4), (4, 5)]
g.add_edges_from(ed)

# nx.draw_planar(g)
# plt.show(g)
# initial edges -----------
e= 3*(len(g)+4)-7-4-g.size()
print("edges remaining",e)

print(g.nodes)
y= []
x= []
# x is for max number , y is for degree (min)
# edges calculator ---------------------------
for i in g.nodes():
    a=g.copy()
    a.remove_node(i)
    if g.degree(i) >= 4:
        f = g.subgraph([n for n in g.neighbors(i)])
        cyc = GraphMatcher(f, nx.cycle_graph(len(f)))
        if cyc.subgraph_is_isomorphic():
            x.append(0)
            y.append(4)
        else:
            x.append(4 - nx.number_connected_components(a))
            y.append(1)
    else:
        x.append(4 - nx.number_connected_components(a))
        y.append(4 - g.degree(i))
# edges remover ---------------------------
for i1 in g.nodes():
    print("x in",i1,g.degree(i1),"is",x[i1])
    print("y is",i1,"is",y[i1])
    if x[i1]>y[i1]:
        e=e-y[i1]
    else:
        e=e-x[i1]
    print("edges remaining", e)
g.add_nodes_from([6,7,8,9])
def edgeadder(glist):
    garr = []
    for gr in glist:
        for j1 in range(0,5):
            for j2 in range(6,9):
                ga= gr.copy()
                appen=True
                if not ga.has_edge(j1,j2):
                    if x[j1]>y[j1]:
                        ga.add_edge(j1,j2)
                        x[j1]=-1
                    else:
                        appen = False
                for el in garr:
                    if nx.is_isomorphic(el, ga):
                        appen = False
                if not nx.check_planarity(ga)[0]:
                    appen = False
                if appen:
                    garr.append(ga)
                    print(ga.edges())
    print(len(garr))
    return garr
arg = []
arg.append(edgeadder([g]))
sum=0
g2 = []
g2= [g]
for i2 in range(0,e-1):
    g1= edgeadder(g2)
    g2=g1.copy()
    sum=+len(g1)

print("sum=",sum)