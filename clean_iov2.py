# import flask
# import json
import networkx as nx
from itertools import combinations
# import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism import GraphMatcher
from itertools import cycle
import os
import collections


def wmatch(e1, e2):
    return e1['id'] == e2['id']

# edges calculator ---------------------------
# Assumes it contains all nodes from 0 to len(g.nodes) to keep x, y consistent


def edge_calc(g):
    e = 3*(len(g)+4)-7-4-g.size()
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

    # edges remover ---------------------------
    for i1 in g.nodes():
        # print("x in ",i1,"is",x[i1])
        # print("y is ",i1,"is",y[i1])
        if x[i1] > y[i1]:
            e = e-y[i1]
        else:
            e = e-x[i1]
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
    n = len(g.nodes())
    if e == 0:
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
    for combo in combinations(nodl, e):
        ga = g.copy()
        ga.add_nodes_from(nodestoadd)
        # print(ga.edges())
        z = y.copy()
        for i, nod in enumerate(combo):
            z[nod] += 1
        zx = []
        o = z.copy()
        for i in range(len(z)):
            zx.append((i, z[i]))

        # p=n
            # pool =cycle([(n+i) for i in range(4)])
            # for i in range(len(z)):
            #     for j in range(i+1,len(z)):
            #         if z[i]<z[j]:
            #             buf=z[j]
            #             z[j]=z[i]
            #             z[i]=buf
            #             buf2=zx[j]
            #             zx[j]=zx[i]
            #             zx[i]=buf2
            # # print(zx,"hi")
            # v=nodestoadd.copy()
            # i=7
            # h=g.copy()
            # for (a,b) in zx:
            #     if b==3:
            #         g.add_edges_from([(i-1,a),(i,a),(i+1,a)])
            #         o[a]-=3
            #         j=i-1
            #         k=i+1

            #         try:
            #             while(h.neighbors(a)):
            #                 ne = list(h.neighbors(a))
            #                 h.remove_node(a)
            #                 ne.sort()
            #                 if len(ne)==1 and o[ne[0]]>=2:
            #                     g.add_edges_from([(j,ne[0]),(k,ne[0])])
            #                     o[ne[0]]-=2
            #                     a=ne[0]
            #                     # h.remove_node(ne[0])
            #                     break

            #                 elif len(ne)>1:
            #                     if o[ne[1]]>=1 and o[ne[0]]>=1:
            #                         g.add_edges_from([(ne[0],j),(ne[1],k)])
            #                         o[ne[0]]-=1
            #                         o[ne[1]]-=1
            #                         if o[ne[0]]!=0:
            #                             g.add_edges_from([(ne[0],i) for i in range(o[ne[0]])])
            #                             o[ne[0]]=0
            #                             # h.remove_node(o[ne[0]])
            #                             a=ne[0]
            #                             # h.remove_node(ne[0])
            #                             break
            #                         if o[ne[1]]!=0:
            #                             g.add_edges_from([(ne[1],i) for i in range(o[ne[1]])])
            #                             o[ne[1]]=0
            #                             # h.remove_node(o[ne[0]])
            #                             a=ne[1]
            #                             break
            #                 else:
            #                     break
            #         except:
            #             pass
            #     break

        # i=n+2
        # for t in range(n-1,-1,-1):
        #     if z[t]==3:
        #         ga.add_edges_from([(i-1,t),(i,t),(i+1,t)])
        #         g.add_edges_from([(i-1,t-1),(i+1,t-1)])
        #         i-=1
        #         for r in range(t-2,-1,-1):
        #             while z[r]>0:
        #                 ga.add_edges_from([(r,i)])
        #                 z[r]-=1
        #                 i-=1
        #                 if i is 0 and z[r]>0:
        #                     i=n+3

        #             i+=1

        # print(ga.edges())
        appen = True
        for el in garr:
            if nx.is_isomorphic(el, ga, edge_match=None):
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

        # plt.figure(i)
        # nx.draw_planar(gb,labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
        # os.mkdir('n={}'.format(n+4))
        # os.mkdir('n={}/export{}'.format(n+4,len(edgeset3[0])))
        # plt.savefig("n={}/export{}/fig{}.png".format(n+4,len(edgeset3[0]),i))
        # plt.savefig("export/fig{}.png".format(i))

        print(gb.edges())
        i += 1
    # for gn in glist:
    # print(gn.edges())
    print('the final no.: {}'.format(i))
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
