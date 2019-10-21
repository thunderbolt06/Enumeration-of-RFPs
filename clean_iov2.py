import networkx as nx
from itertools import combinations
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism import GraphMatcher
from itertools import cycle
import os
import collections


def wmatch(e1, e2):
    return e1['id'] == e2['id']

# edges calculator ---------------------------


def edge_remover(num_nodes, edgeval, x, y):
    """Removes Edges Helper Function"""
    for i1 in num_nodes():
        # print("x in ",i1,"is",x[i1])
        # print("y is ",i1,"is",y[i1])
        if x[i1] > y[i1]:
            edgeval -= y[i1]
        else:
            edgeval -= x[i1]
    print("edges remaining", edgeval)



# Assumes it contains all nodes from 0 to len(g.nodes) to keep x, y consistent


def edge_calc(g):
    edgeval = 3*(len(g)+4)-7-4-g.size()
    # print(g.nodes)
    y = []
    x = []
    for i in range(len(g.nodes())):
        a = g.copy()
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

        edge_remover(g.nodes, edgeval, x, y)

    # edge_adder ----------------------------
    garr = []
    # nodelist = list of possible nodes
    nodelist = []
    for xi in range(len(x)):
        for i in range(x[xi] - y[xi]):
            nodelist.append(xi)
    nodestoadd = [len(g.nodes()) + i for i in range(4)]
    # print(nodelist, nodestoadd)
    n = len(g.nodes())

    if edgeval == 0:
        p = n
        g.add_edges_from([(n+i, n+i+1) for i in range(3)], id=2)
        g.add_edges_from([(n, n+3)], id=2)
        for r in range(n):
            while y[r] > 0:
                g.add_edges_from([(r, p)], id=2)
                y[r] -= 1
                p += 1
                if p is n+4 and y[r] > 0:
                    p = n
            p -= 1
        garr.append(g)

    graph2 = g.clone()
    graph2.add_nodes_from(nodestoadd)
    add_graph = True
    for combination in combinations(nodelist, edgeval):
        if check_combinations(combination, graph2, y, garr):
            garr.append(graph2)

def check_combinations(combo, new_graph, z, graph_list):
        # Increase Y value for every node
        for i, nod in enumerate(combo):
            z[nod] += 1
        zx = []
        for i in range(len(z)):
            zx.append((i, z[i]))

        for known_graph in graph_list:
            if nx.is_isomorphic(known_graph, new_graph, edge_match=None):
                return False
        if not nx.check_planarity(new_graph)[0]:
            return False
        return True


edgeset3 = [

    [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 4), (4, 5)]
]
for ed in edgeset3:
    g = nx.Graph()
    g.add_edges_from(ed, id=1)
    n = len(g.nodes())
    # print('G is ', g.edges())
    glist = edge_calc(g)
    i = 0
    cpp = True
    for gb in glist:
        gb.add_edges_from([(n+i, n+i+1) for i in range(3)])
        gb.add_edge(n, n+3)
        r5 = []

        print(gb.edges())
        i += 1
    # for gn in glist:
    # print(gn.edges())
    print('the final no.: {}'.format(i))
    print('\n\n')

