import networkx as nx
from NESW import num_cips


def cip_rule_filter(graph_list):
    """
    Given List of Graphs
    Returns filtered list that satisfy the CIP rule

    CIP Rule = 2 CIP on outer biconnected components and no CIP on
    inner biconnected components
    """
    filtered_graphs = []
    for graph in graph_list:
        cip_check = True
        outer_comps, inner_comps, single_component = component_break(graph)
        # CIP Rule for Outer Components
        for comp in outer_comps:
            if num_cips(comp) > 2:
                cip_check = False
        # CIP Rule for Outer Components
        for comp in inner_comps:
            if num_cips(comp) > 0:
                cip_check = False
        # CIP Rule for single_component Components
        if num_cips(single_component) > 4:
            cip_check = False
        if cip_check:
            filtered_graphs.append(graph)
    return filtered_graphs


def component_break(given_graph):
    """
    Given a graph,
    returns [list of the 2 outer components(1 articulation point) with 2cip],
    [list of other inner components(2 articulation points) with 0 cip]
    """
    test_graph = given_graph.copy()
    cutvertices = nx.articulation_points(test_graph)

    # O(biconnected_components * cutvertices)
    inner_components = []
    outer_components = []
    for peice in nx.biconnected_components(test_graph):
        # Find num cutvertices
        # num_cutverts = nx.intersection(peice, cutvertices)
        num_cutverts = 0
        for cutvert in cutvertices:
            if cutvert in peice:
                num_cutverts += 1

        if num_cutverts == 2:
            inner_components.append(peice)
        elif num_cutverts == 1:
            outer_components.append(peice)
        elif num_cutverts == 0:
            single_component = peice
        else:
            print("Illegal Case 1")
            print(test_graph.edges())

        if len(outer_components) > 2:
            print("Illegal Case 2")
            print(test_graph)

    return outer_components, inner_components, single_component
