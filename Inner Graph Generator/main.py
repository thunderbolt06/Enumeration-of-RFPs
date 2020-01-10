#!bin/python
import networkx as nx
# import warnings
from generate import run_generations
from plot_graphs import plot_graphs

# warnings.simplefilter("ignore")

init_len = int(input("Enter the number of vertices: "))

listofgraphs = run_generations(init_len)
plot_graphs(listofgraphs)
