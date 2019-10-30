import flask
import json
import networkx as nx
# import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
from networkx.algorithms.isomorphism import GraphMatcher
init=4
g = nx.Graph()
g.add_edges_from([(i, i + 1) for i in range(init)])
