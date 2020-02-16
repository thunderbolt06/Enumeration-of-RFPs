from generate import run_generations
from plot_graphs import plot_graphs
# from plot_graphs2 import plot_graph
from generate import check_test_graph
from componentcheck import complex_triangle_check
from componentcheck import cip_rule_check
import networkx as nx
def RFPchecker(graph):
    check= True
    if not check_test_graph(graph):
        check = False
        print("main check failed")
    if not cip_rule_check(graph):
        check = False
        print("cip rule failed")
    if not complex_triangle_check(graph):
        check = False
        print("contains complex triangle")
    if check:
        print("RFP exists")
        plot_graphs(len(graph),[graph])
        # plot_graph([graph])
    else:
        print("RFP doesn't exist")

g=nx.Graph()
# g.add_edges_from([(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5)])
# g.add_edges_from([(0, 1), (1, 2),  (2, 3), (0,3),(1,3),(0,2)])
g.add_edges_from([(0, 1), (1, 2),  (2, 3), (3,4),(1,3)])


RFPchecker(g)


    



