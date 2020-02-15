#!/bin/python
# import networkx as nx
# import warnings
from generate import run_generations
# from plot_graphs import plot_graphs
from componentcheck import cip_rule_filter
# from pprint import pprint

# warnings.simplefilter("ignore")

# Get Initial no. of Vertices
init_len = int(input("Enter the number of vertices: "))

# Generate and store all generations of graphs
listofgraphs = run_generations(init_len)

# for g in listofgraphs:
# 	print(g.nodes)

# plot_graphs(init_len, listofgraphs)
print(f'Final No. of Graphs: {len(listofgraphs)}')

# Filter based on CIP rule
cip_graphs = cip_rule_filter(listofgraphs)
len(cip_graphs)

# plot_graphs(init_len, listofgraphs)
