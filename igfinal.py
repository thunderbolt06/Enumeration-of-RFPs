import json
import networkx as nx
import collections
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
from networkx.algorithms.isomorphism import GraphMatcher
from networkx.algorithms import tournament
import os
init=8
g = nx.Graph()
g= nx.path_graph(init)
print(g.edges)
def makeBig(glist):
    garr = []
    isomorphics = 0
    nonplanar = 0
    k4subgraph = 0
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
            gm_k4_check = GraphMatcher(ga, nx.complete_graph(4))
            if not nx.check_planarity(ga)[0]:
                nonplanar += 1
                appen = False
            elif gm_k4_check.subgraph_is_isomorphic():
                appen = False
                k4subgraph += 1
            else:
                for el in garr:
                    if nx.is_isomorphic(el, ga):
                        isomorphics += 1
                        appen = False
            if appen:
                garr.append(ga)
                # print(ga.edges())
    # print('Isomorphics: ', isomorphics)
    # print('Non-Planar: ', nonplanar)
    # print('K4 as Subgraph: ', k4subgraph)
    return garr


arg = []
print('Inner Graphs for n = {}: '.format(init-1), 1)
try:
    os.mkdir("RFP/Len={}".format(init))
except:
    pass
ra=1
plt.figure(ra)
nx.draw_planar(g,labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
plt.savefig("RFP/Len={}/{}.png".format(init,ra))
arg.append(makeBig([g]))
nex = arg[0]
for i in range(40):
    g2 = makeBig(nex)
    sum = 0
    for b in nex:
        app= True
        bpp = True
        cpp= True
        dpp= True
        d = b.copy()

        # bridge case -----------------------

        for a1 in b.nodes():
            for b1 in b.nodes():
                if a1<b1:
                    c = b.copy()
                    cut = list(nx.articulation_points(c))
                    if c.has_edge(a1, b1):
                        c.remove_node(a1)
                        c.remove_node(b1)
                        # print(nx.number_connected_components(c))
                        if a1 in cut and b1 in cut or a1 not in cut and b1 not in cut:
                            if nx.number_connected_components(c)>2:
                                app =False
                                # print("bridge")

        # # cut with cycle case --------------------------
        # cut2 = list(nx.articulation_points(d))
        # if len(cut2)==0:
        #     bpp=True
        # else:
        #     for c1 in cut2:
        #         # print("cut")
        #         # d.subgraph([n for n in d.neighbors(c1)])
        #         try:
        #             nx.find_cycle(d.subgraph([n for n in d.neighbors(c1)]))
        #             # print("try")
        #         except:
        #             bpp =True
        #             # print('except')


        # just cycle case , degree>2--------------------------------
        reg= []
        r5 = []
        for n1 in b.nodes():
            e = b.copy()
            if b.degree(n1)>=4:
                f = e.subgraph([n for n in e.neighbors(n1)])
                try:
                    r4 = (list(nx.find_cycle(f, orientation='ignore')))
                    # print(r4)
                    # if n1 in list(nx.articulation_points(e)):
                    #     bpp=False
                    if len(r4)!=len(f) and len(r4)>=4:
                        cpp= False
                    else:
                        r5.append(list(nx.find_cycle(f, orientation='ignore')))
                    # if nx.number_connected_components(e) > 1:
                        # cpp = False

                        reg.append(n1)
                        # print(n1)
                        # print(b.size(), "hi", n1)
                except:
                    pass
        j1=0
        for i1 in r5:
            j1=j1+1
            for i2 in r5[j1:]:
                if collections.Counter(i1)==collections.Counter(i2):
                    # print(i1)
                    cpp=False
                    
        # for r1 in reg:
        #     for r2 in reg:
        #         if len(list(nx.all_simple_paths(b, source=r1, target=r2, cutoff=2)))>3:
        #             cpp= False


# final---------
        if app and bpp and cpp and dpp:
            sum = sum +1
            ra+=1
            print (b.edges)
            plt.figure(ra)
            nx.draw_planar(b,labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
            plt.savefig('RFP/Len={}/{}.png'.format(init,ra))

    print("Inner Graphs for n = {}: ".format(i+init),sum)
    i=1
    # for g in nex:
        # i+=1
        # print(g.edges())
        
    arg.append(g2)
    nex = g2


"""
for i in range(3):
    # write json formatted data
    d = json_graph.node_link_data(g2[i+2])  # node-link format to serialize
    # write json
    fna = 'force/force{}.json'.format(i)
    json.dump(d, open(fna, 'w'))
    print('Wrote node-link JSON data to force/force{i}.json')

# Serve the file over http to allow for cross origin requests
app = flask.Flask(__name__, static_folder="force")

@app.route('/')
def static_proxy():
    return app.send_static_file('force.html')

print('\nGo to http://localhost:8000 to see the example\n')
app.run(port=8000)
"""
