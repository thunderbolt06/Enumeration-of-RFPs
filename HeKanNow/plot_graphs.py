import os
import matplotlib.pyplot as plt
import networkx as nx
# from generate import generation_next


def plot_graphs(init_len, graph_list):
    os.makedirs("./RFP_Graph_Plots/Len {}".format(init_len), exist_ok=True)
    graph_no = 1
    for graph in graph_list:
        plt.figure(graph_no)
        nx.draw_planar(graph,
                       labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
        plt.savefig('Graph_edges_{1} - {2}.png'.format(
                    init_len, graph.size(), graph_no))
        graph_no += 1
