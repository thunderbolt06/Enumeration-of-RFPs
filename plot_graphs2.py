import os
import random as ra
import matplotlib.pyplot as plt
import networkx as nx
def plot_graphs(graph_list):
    try:
        os.mkdirs("./RFP_Graph_Plots")
        os.mkdirs("./RFP_Graph_Plots/Len {}".format(init_len))
    except:
        pass
    graph_no = 4
    for graph in graph_list:
        plt.figure(graph_no)
        nx.draw(graph,labels=None, font_size=12, font_color='k',\
            font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
        # plt.savefig("./trash/Graph_edges_{} - {}.png".format(
        #             graph.size(), graph_no))
        plt.show()
        graph_no += 1
        