import flask
import json
import networkx as nx
from itertools import combinations
# import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism import GraphMatcher
def wmatch(e1, e2):
    return e1['id'] == e2['id']

# edges calculator ---------------------------
# Assumes it contains all nodes from 0 to len(g.nodes) to keep x, y consistent
def edge_calc(g):
    e= 3*(len(g)+4)-7-4-g.size()
    # print(g.nodes)
    y= []
    x= []
    for i in range(len(g.nodes())):
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
        if x[i] < 3:
            y[i] = x[i]

    # edges remover ---------------------------
    for i1 in g.nodes():
        # print("x in ",i1,"is",x[i1])
        # print("y is ",i1,"is",y[i1])
        if x[i1]>y[i1]:
            e=e-y[i1]
        else:
            e=e-x[i1]
    print("edges remaining", e)

    # edge_adder ----------------------------
    garr = []
    # nodl = list of possible nodes
    nodl = []
    for xi in range(len(x)):
        for i in range(x[xi] - y[xi]):
            nodl.append(xi)
    nodestoadd = [len(g.nodes()) + i for i in range(e)]
    # print(nodl, nodestoadd)
    for combo in combinations(nodl, e):
        ga = g.copy()
        ga.add_nodes_from(nodestoadd)
        ga.add_edges_from([(len(g.nodes()) + i, nod) for i, nod in enumerate(combo)], id=2)
        # print('My fav Garr el: ', ga.edges())
        appen = True
        for el in garr:
            if nx.is_isomorphic(el, ga, edge_match=wmatch):
                # print(ga)
                appen = False
                break
            elif not nx.check_planarity(ga)[0]:
                appen = False
        if appen:
            garr.append(ga)
            # print(ga.edges())
            # print(combo)
    # print(len(garr))
    return garr
edgeset = [
[(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 5)],[(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 4), (4, 5)],
[(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5)],
[(0, 1), (0, 3), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5)],
[(0, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)],
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4), (4, 5)],
[(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5)],
[(0, 1), (0, 2), (0, 4), (1, 2), (2, 3), (2, 4), (3, 4), (4, 5)],
[(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (2, 5), (3, 4), (4, 5)],
[(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (3, 4), (4, 5)],
[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 3), (3, 4), (4, 5)],
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4), (4, 5)],
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5)],
[(0, 1), (0, 2), (0, 4), (0, 5), (1, 2), (2, 3), (2, 4), (3, 4), (4, 5)],
[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 5), (2, 3), (3, 4), (4, 5)],
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (1, 5), (2, 3), (3, 4), (4, 5)],
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5)]
]
edgeset2 = [ [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)],
[(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 4)],
[(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4)],
[(0, 1), (0, 3), (1, 2), (1, 3), (2, 3), (3, 4)],
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 4)],
[(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)],
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4), (2, 3), (3, 4)],
             ]
for ed in edgeset2:
    g = nx.Graph()
    g.add_edges_from(ed, id=1)
    # print('G is ', g.edges())
    glist = edge_calc(g)
    # for gn in glist:
        # print(gn.edges())
    print(f'the final no.: {len(glist)}')
    print('\n\n')