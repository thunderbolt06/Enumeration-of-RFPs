#!bin/python
import networkx as nx
# import warnings
from generate import run_generations
from plot_graphs import plot_graphs
from pprint import pprint

# warnings.simplefilter("ignore")

init_len = int(input("Enter the number of vertices: "))

listofgraphs = run_generations(init_len)
print(len(listofgraphs))
print('Graph Printing')
for graph in listofgraphs:
    print(graph.edges())

plot_graphs(init_len, listofgraphs)
