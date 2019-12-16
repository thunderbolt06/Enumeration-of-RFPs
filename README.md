# Enumeration-of-RFPs
Abstract.

First, the task is to generate all inner graphs on ‘n’ vertices for which Rectangular floor
plan is possible. The idea is to first construct a path graph and then to add edges
between two vertices if the length of the shortest path between them is found to be two.
This way we will obtain different triangulated graphs and then we have to check various
conditions on it to make sure if there exists a corresponding floor plan for it.
Given a dual graph of an RFP, the second task is to add 4 more vertices to it so that it
forms a maximal dual graph. This method is called “IO” where ‘I’ refers to the inner
vertices and ‘O’ refers to the outer ones.The initial graph is referred to as the inner
graph with n vertices and the final result as the outer graph with n+4 vetices. This
method gives all possible non-isomorphic maximal graph for n+4 vertices for a given
inner graph of n vertices.
