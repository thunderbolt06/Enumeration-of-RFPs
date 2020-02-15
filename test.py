import matplotlib.pyplot as plt
import networkx as nx 
graph = nx.random_internet_as_graph(8)
print(graph.edges)
graph_no = 1
plt.figure(graph_no)
nx.draw(graph,labels=None, font_size=12, font_color='k',\
    font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
plt.savefig("./trash/Graph_edges_{} - {}.png".format(
            graph.size(), graph_no))
graph_no += 1