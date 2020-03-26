from generate import run_generations
from plot_graphs import plot_graphs
# from plot_graphs2 import plot_graph
from generate import check_test_graph
from componentcheck import complex_triangle_check
from componentcheck import cip_rule_check
from componentcheck import civ_rule_check
import networkx as nx
def RFPchecker(graph):
    check= True

    if not check_test_graph(graph):
        check = False
        
    if not cip_rule_check(graph):
        check = False
        print("cip rule failed")

    if  civ_rule_check(graph):
        check=False
        print("civ rule failed")
    
        print('FALSE cuz {x}')
    if not complex_triangle_check(graph):
        check = False
        print("contains complex triangle")
    
    if check:
        print("RFP exists")
        plot_graphs(len(graph),[graph])
        # plot_graph([graph])
    else:
        print("RFP doesn't exist")
        plot_graphs(len(graph),[graph])

g=nx.Graph()
# g.add_edges_from([(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 4), (4, 5)]) #wrapped vertex attached
# g.add_edges_from([(0, 1), (1, 2),  (2, 3), (0,3),(1,3),(0,2)]) #complex triangle
# g.add_edges_from([(0, 1), (1, 2),  (2, 3), (3,4),(1,3)]) #cip rule
# g.add_edges_from([(0, 1), (1, 2), (0,2),(3,4),(4,5),(5,3),(0,3),(0,4),(0,5),(2,4),(1,4),(2,5)]) #k4 subgraph

g.add_edges_from([(0, 1), (0, 9), (1, 2), (1, 3), (1, 9), (2, 3), (3, 4),(2,9)]) #5 cips



# g.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 4),
#  (1, 5), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)])#complex without K4

# g.add_edges_from([(0, 1), (1, 2), (2,0)])

RFPchecker(g)


    



