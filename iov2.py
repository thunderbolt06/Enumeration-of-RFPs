# import flask
# import json
import networkx as nx
from itertools import combinations
# import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
# import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism import GraphMatcher
from itertools import cycle
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
    nodestoadd = [len(g.nodes()) + i for i in range(4)]
    # print(nodl, nodestoadd)
    n=len(g.nodes())


    for combo in combinations(nodl, e):
        ga = g.copy()
        ga.add_nodes_from(nodestoadd)
        # print(ga.edges())
        z=y.copy()
        for i,nod in enumerate(combo):
            z[nod]+=1
        zx=z.copy()
        p=n
        pool =cycle([(n+i) for i in range(4)])
        
        for r in range(n):
            while zx[r]>0:
                ga.add_edges_from([(r,p)])
                zx[r]-=1
                p+=1
                if p is n+4 and zx[r]>0:
                    p=n+1
            
            p-=1
        
        ga.add_edges_from([(n+i,n+i+1)  for i in range(3)])
        ga.add_edge(n,n+3)
        # print(ga.edges())
        appen = True
        for el in garr:
            if nx.is_isomorphic(el, ga):
                # print(ga)
                appen = False
                break
        if not nx.check_planarity(ga)[0]:
            appen = False
        if appen:
            garr.append(ga)
            # print(ga.edges())
            # print(combo)
    # print(len(garr))
    return garr
edgeset3 = [

                [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]

             ]
for ed in edgeset3:
    g = nx.Graph()
    g.add_edges_from(ed, id=1)
    n= len(g.nodes())
    # print('G is ', g.edges())
    glist = edge_calc(g)
    for gb in glist:
        gb.add_edges_from([(n+i,n+i+1)  for i in range(3)])
        gb.add_edge(n,n+3)
        print(gb.edges())
    # for gn in glist:
    # print(gn.edges())
    print('the final no.: {}'.format(len(glist)))
    print('\n\n')













    # z=y.copy()
        
                                                                                                # pool =cycle([(n-i) for i in range(4)])
                                                                                                # for i,nod in enumerate(combo):
                                                                                                #     z[nod]+=1
                                                                                                #     m =[(n-i) for i in range(4)]
                                                                                                #     o=4
                                                                                                # # for ix in range(n-3):
                                                                                                # #     if y[ix]>0:
                                                                                                # #         ga.add_edges_from([(m[o-v],ix)  for v in range(y[ix])  ])
                                                                                                # #         o=o-y[ix]+2
                                                                                                #     for asd in range(z[0]):
                                                                                                #         ga.add_edges_from([(next(pool),0)])
                                                                                                #     # ga.add_edges_from([(m[o-v],0)  for v in range(z[0])  ])
                                                                                                #         o=o-z[0]+2
                                                                                                #     print(o)
                                                                                                # print(z)