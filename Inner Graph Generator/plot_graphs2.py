import os
import matplotlib.pyplot as plt
import networkx as nx
def plot_graph(graph_list):
    init_len= len(graph_list[0])
    folder_path = f"./RFP_Graph_Plots/Len {init_len}"
    try:
        os.mkdirs("./RFP_Graph_Plots")
        os.mkdirs(folderpath,mode=0o777, exist_ok=False)
        file = open("output.txt","a")
    except:
        pass
    graph_no = 1
    for graph in graph_list:
        plt.figure(graph_no)
        nx.draw(graph,labels=None)
        plt.savefig(f'{folder_path}/edgelen_{graph.size()}_num{graph_no}.png')
        # plt.show()
        graph_no += 1
        file.writelines(graph.edges(),"\n")
        plt.clf()

g=nx.Graph()
g.add_edges_from([(0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 4)])
plot_graph([g])