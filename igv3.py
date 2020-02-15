import networkx as nx
import collections
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
from networkx.algorithms.isomorphism import GraphMatcher
from networkx.algorithms import tournament
import os
import warnings
warnings.simplefilter("ignore")

# from networkx.readwrite import json_graph
from networkx.algorithms.isomorphism import GraphMatcher
# from networkx.algorithms import tournament

init=int(input("enter the number of vertices"))
# init = 6

g = nx.Graph()
g = nx.path_graph(init)
# print(g.edges)


def makeBig(glist):
    garr = []
    # Iter through list of graphs
    for g in glist:

        # find possible edges for the graph g
        filtered = []
        for nod in g.nodes():
            for nod2 in g.nodes():
                if nx.shortest_path_length(g, nod, nod2) == 2:
                    filtered.append((nod, nod2))

        # Go through the list of possible filtered edges
        for tup in filtered:
            ga = g.copy()
            ga.add_edge(*tup)

            # Check if graph g is isomorphic to any of the previous graphs so far
            appen = True
            if not nx.check_planarity(ga)[0]:
                appen = False
            gm_k4_check = GraphMatcher(ga, nx.complete_graph(4))
            if gm_k4_check.subgraph_is_isomorphic():
                appen = False
            
            else:
                for el in garr:
                    if nx.is_isomorphic(el, ga):
                        appen = False
            # just cycle case --------------------------------
            r4 = []
            check_set = []
            r5 = []
            for n1 in ga.nodes():
                e = ga.copy()
                if ga.degree(n1)>=4:
                    f = e.subgraph([n for n in e.neighbors(n1)])
                    try:
                 mincut= min(cutset)
        maxcut= max(cutset)                   appen= False
                                break
                            else:
                                r5.append(r4cyc)

                    except:
                        pass
            j1=0
            for i1 in r5:
                j1=j1+1
                for i2 in r5[j1:]:
                    if collections.Counter(i1)==collections.Counter(i2):
                        appen=False

            # for n1 in ga.nodes():
            #     e = ga.copy()
            #     if ga.degree(n1)>=4:
            #         f = e.subgraph([n for n in e.neighbors(n1)])
            #         try:
            #             for r4 in nx.cycle_basis(f):
            #                 if len(r4)!=len(f):
            #                     appen= False
            #                 elif len(r4)>=4:
            #                     check_set.append(set(r4))
            #         except:
            #             pass
            # if len(check_set) > 2:
            #     print(check_set)

            # for it in range(len(check_set)):
            #     for jt in range(it+1, len(check_set)):
            #         if len(check_set[it].intersection(check_set[jt])) >= 2:
            #             appen = False
            #             print(check_set[it], check_set[jt])



            
                    
            # print(r5)
            # j=0
            # for cycles in r5:
            #     j+=1
            #     # print(cycles,"loop1     ")
            #     for cycles2 in r5[j:]:
            #         elemark=0
            #         elemark2=0
            #         print(cycles2,"loop2     ")
            #         for ele1 in cycles:
            #             elemark+=1
            #             for ele2 in cycles2:
            #                 elemark2+=1
            #                 if ele1==ele2:
            #                     for em in cycles[elemark:]:
            #                         for em2 in cycles2[elemark2:]:
            #                             if em==em2:
            #                                 appen=False
            if ga.size()>3*init-7:
                appen=False
            if appen:
                garr.append(ga)
    return garr
try:
    os.mkdir("RFP3")
except:
    pass
try:
    os.mkdir("RFP3/Len={}".format(init))
except:
    pass

print('Inner Graphs for n = {}: '.format(init - 1), 1)
nex=[]
nex.append(g)
ra=1
while(nex):
    g2 = makeBig(nex)
    sum = 0
    # Take listofgraphs at every iter and for each graph 'd' (a copy)
    for b in nex:
        app = True
        # bridge case -----------------------
        cut = list(nx.articulation_points(b))
        for a1 in b.nodes():
            for b1 in b.nodes():
                if a1 < b1:
                    c = b.copy()
                    if c.has_edge(a1, b1):
                        c.remove_node(a1)
                        c.remove_node(b1)
                        # print(nx.number_connected_components(c))
                        if a1 in cut and b1 in cut or a1 not in cut and b1 not in cut:
                            if nx.number_connected_components(c) > 2:
                                app = False
                                print("bridge")
            sum = sum + 1
            plt.figure(ra)
            nx.draw_planar(b,labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
            plt.savefig('RFP3/Len={}/new{}.png'.format(init,ra))
            # plt.show()
            print(b.edges)
            ra+=1
    print("Rectangular Dual Graphs for n = {}: ".format(b.size()), sum)
    # for g in nex:
    #     print(g.edges())1
    nex = g2

