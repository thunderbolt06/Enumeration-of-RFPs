import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher


def dist2_nodepairs(given_graph):
    edge_list = []
    for nod in given_graph.nodes():
        for nod2 in given_graph.nodes():
            if nx.shortest_path_length(given_graph, nod, nod2) == 2:
                edge_list.append((nod, nod2))
    return edge_list


def graph_exists(given_graph, graph_list):
    exist = 0
    for existing_graph in graph_list:
        if nx.is_isomorphic(existing_graph, given_graph):
            exist = 1
            break
    return exist


def is_cycle_case(given)


def is_bridge_case(given_graph):
    cutvertices = list(nx.articulation_points(given_graph))
    for edge in given_graph.edges():
        # INSTEAD: check vertex_connectivity of nod1 + nod2 - 1?
        test_bridge_graph = given_graph.copy()
        nod1, nod2 = edge
        if (nod1 in cutvertices and nod2 in cutvertices) \
                or (nod1 not in cutvertices and nod2 not in cutvertices):
            if nx.number_connected_components(test_bridge_graph) > 2:
                return 1
    return 0


def filter_bridge_case(graph_list):
    return [graph for graph in graph_list if not is_bridge_case(graph)]


def check_test_graph(given_graph):
    # Planarity Check
    if not nx.check_planarity(given_graph)[0]:
        return 0
    # Subgraph is K4
    if GraphMatcher(given_graph,
                    nx.complete_graph(4)).subgraph_is_isomorphic():
        return 0
    # Some other random checks!
    return 1


def generation_next(prev_gen):
    """
    Make Big Reimplemented
    Input( iterable or list of graphs of certain generation 'i' )
    Returns ( List of Graphs of generation 'i+1' )
    """
    next_gen = []

    # Iter through list of graphs
    for original_graph in prev_gen:
        # Select edges to nodes which are at distance 2
        select_edges = dist2_nodepairs(original_graph)

        # Go through the list of possible selected edges and add one
        for test_edge in select_edges:
            test_graph = original_graph.copy()
            test_graph.add_edge(*test_edge)
            if (not graph_exists(test_graph, next_gen)) \
                    and check_test_graph(test_graph):
                next_gen.append(test_graph)

    return next_gen


def run_generations(init_len):
    """
    - Generates initial graph
    - Runs generations till 3*(edges) - 7
    - complete_graph_list is list of all graphs
    """
    num_graphs = 0
    current_gen = [nx.path_graph(init_len)]
    complete_graph_list = current_gen.copy()
    while len(current_gen) and current_gen[0].size() < (3*init_len - 7):
        current_gen = generation_next(current_gen)
        num_graphs += show_graph_list(current_gen)
        complete_graph_list.extend(filter_bridge_case(current_gen))
    print(num_graphs)
    return complete_graph_list


def show_graph_list(listg):
    for graph in listg:
        print(graph.edges)
    return len(listg)
