import flask
import json
import networkx as nx
# import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
from networkx.algorithms.isomorphism import GraphMatcher

g = nx.Graph()
g.add_edges_from([(i, i+1) for i in range(5)])


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
    print('Isomorphics: ', isomorphics)
    print('Non-Planar: ', nonplanar)
    print('K4 as Subgraph: ', k4subgraph)
    return garr


arg = []
arg.append(makeBig([g]))
nex = arg[0]
for i in range(8):
    g2 = makeBig(nex)
    print('Inner Graphs for n = {}: '.format(i+6), len(nex))
    for g in nex:
        print(g.edges())
    arg.append(nex)
    nex = g2




# nx.draw(g)
# plt.subplot(122)
# plt.show()


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
