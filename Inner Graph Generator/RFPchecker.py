from generate import run_generations
from plot_graphs import plot_graphs
from componentcheck import cip_rule_filter
from generate import check_test_graph
from componentcheck import cip_rule_filter
from componentcheck import complex_triangle_check
def RFPchecker(graph):
    check= False
    if check_test_graph(graph):
        check = True
    if cip_rule_filter(graph):
        check = True
    if complex_triangle_check(graph):
        check = True
    if check:
        print("RFP exists")
        plot_graphs(len(graph),[graph])
    else:
        print("RFP doesn't exist")
    

    



