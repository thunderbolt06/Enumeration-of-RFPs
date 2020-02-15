# import flask
# import json
import networkx as nx
from plot_graphs import plot_graphs
from itertools import combinations
# import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism import GraphMatcher
import warnings
warnings.simplefilter("ignore")
def wmatch(e1, e2):
    return e1['id'] == e2['id']

# edges calculator ---------------------------
# Assumes it contains all nodes from 0 to len(g.nodes) to keep x, y consistent
def edge_calc(g):
    e= 3*(len(g)+4)-7-4-g.size()
    n=len(g.nodes)
    # print(g.nodes)
    y= [] # is the min number of edges to be added
    x= [] # is the max number of edges 
    cutset= []
    cutset= list(nx.articulation_points(g))
    if cutset:
        mincut= min(cutset)
        maxcut= max(cutset)
    else:
        maxcut=-1
        mincut=n
    for i in range(len(g.nodes())):
        a=g.copy()
        a.remove_node(i)
        if i in cutset:
            x.append(2)
            y.append(2)
        else:
            if i>mincut and i<maxcut:
                if g.degree(i) >= 4:
                    f = g.subgraph([n for n in g.neighbors(i)])
                    cyc = GraphMatcher(f, nx.cycle_graph(len(f)))
                    if cyc.subgraph_is_isomorphic():
                        x.append(0)
                        y.append(0)
                    else:
                        x.append(1)
                        y.append(1)
                else:
                        x.append(1)
                        y.append(1)
            else:
                if g.degree(i) >= 4:
                    f = g.subgraph([n for n in g.neighbors(i)])
                    cyc = GraphMatcher(f, nx.cycle_graph(len(f)))
                    if cyc.subgraph_is_isomorphic():
                        x.append(0)
                        y.append(0)
                    else:
                        x.append(3)
                        y.append(max(4 - g.degree(i),1))
                else:
                        x.append(3)
                        y.append(4 - g.degree(i))
        # if x[i] < 3:
            # y[i] = x[i]
    

    # edges remover ---------------------------
    for i1 in g.nodes():
        # print("x in ",i1,"is",x[i1])
        # print("y is ",i1,"is",y[i1])
        if x[i1]>y[i1]:
            e=e-y[i1]
        else:
            e=e-x[i1]
    print("edges remaining", e)
    
    plot_graphs([g])
    # edge_adder ----------------------------
    nodestoadd = [n + i for i in range(4)]
    g.add_nodes_from(nodestoadd)
    g.add_edges_from([(n,n+1),(n+3,n),(n+1,n+2),(n+2,n+3)])
    garr = []
    # nodl = list of possible nodes
    nodl = []
    for xi in range(len(x)):
        for i in range(x[xi] - y[xi]):
            nodl.append(xi)
    print(y)
    for cut in cutset:
        g.add_edge(cut,n+1)
        g.add_edge(cut,n+3)
    plot_graphs([g])
    def midcompsadder(comp,cuts):

        # Get all triangles
        all_cycles = list(nx.simple_cycles(comp))
        all_triangles = []
        for cycle in all_cycles:
            if len(cycle) == 3:
                all_triangles.append(cycle)

        # Get edges on outer boundary
        outer_boundary = []
        for edge in comp.edges:
            count = 0
            for triangle in all_triangles:
                if edge[0] in triangle and edge[1] in triangle:
                    count += 1
            if count == 1:
                outer_boundary.append(edge)

        
        leftset = []
        rightset = []
        
        for edge in outer_boundary:
            if edge[0] is cuts[0]:
                leftset.append(edge[1])
            if edge[1] is cuts[0]:
                leftset.append(edge[0])
        rightset.append(leftset[1])
        leftset.pop(1)
        while findnext(leftset,outer_boundary):
            leftset.append(findnext(leftset,outer_boundary))

        while findnext(rightset):
            rightset.append(findnext(leftset,outer_boundary))



    def findnext(set,outer_boundary):
        for edge in outer_boundary:
            





    inter_graphs,exter_graphs = component_break(g)
    intgraph1=inter_graphs[0]

    def subedgeadder(inter_graph,outerlist,addlist):
        g= inter_graphs.copy()
        g.add_nodes_from(outerlist)

    if e==0:
        for abc in range(n):
            buf=y[abc]
            i=0
            while buf!=0:
                g.add_edge(abc,i)
                i+=1
                buf-=1
        plot_graphs([g])
    # print(nodl, nodestoadd)
    for combo in combinations(nodl, e):
        ga = g.copy()
        for i,node in enumerate(combo):
            y[node]+=1
        for abc in range(n):
            buf=y[abc]
            i=0
            while buf!=0:
                ga.add_edge(abc,i)
                i+=1
                buf-=1
        # ga.add_edges_from([(n + i, nod) for i, nod in enumerate(combo)], id=2)
        # print('My fav Garr el: ', ga.edges())
        appen = True
        for el in garr:
            if nx.is_isomorphic(el, ga, edge_match=wmatch):
                # print(ga)
                appen = False
                break
        if not nx.check_planarity(ga)[0]:
            appen = False
        if appen:
            garr.append(ga)
            # print(ga.edges())
            print(combo)
            plot_graphs([ga])
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
edgeset3 = [
    [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]
]
for ed in edgeset3:
    g = nx.Graph()
    g.add_edges_from(ed, id=1)
    # print('G is ', g.edges())
    glist = edge_calc(g)
    # for gn in glist:
        # print(gn.edges())
    print(f'the final no.: {len(glist)}')
    print('\n\n')
