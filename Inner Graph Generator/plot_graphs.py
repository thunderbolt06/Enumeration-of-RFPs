import os
import matplotlib.pyplot as plt
import networkx as nx
# from generate import generation_next


def plot_graphs(init_len, graph_list):
    folder_path = f"RFP_Graph_Plots/Len {init_len}"
    os.makedirs(folder_path, exist_ok=True)
    graph_no = 1
    _fig, _ax = plt.subplots()
    for graph in graph_list:
        plt.figure(graph_no)
<<<<<<< HEAD
        nx.draw_planar(graph, with_labels=True, font_size=12)
        plt.show()
        # plt.savefig("Graph_edges_{1} - {2}.png".format(
        #             init_len, graph.size(), graph_no))
=======
        nx.draw_planar(graph, labels=None, font_size=12, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None)
        # Inner Graph IG_<Initial Vertices>_<Graph_Size>_<Graph No.>.png
        plt.savefig(f'{folder_path}/IG_{init_len}_{graph.size()}_{graph_no}.png')
>>>>>>> 8c4060d8ef3fe7f61d51a1ae1b7f0c84ca4eff58
        graph_no += 1
        plt.clf()
