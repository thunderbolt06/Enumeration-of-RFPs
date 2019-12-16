# Enumeration-of-RFPs
## Abstract.

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

## Introduction.

In architectural design, the first step is to build a floor plan as per the adjacency
constraints. Mathematically, the problem is to draw a rectangular floor plan(RPF)
corresponding to the planar graph satisfying all the adjacency constraints; in which each
rectangle corresponds to a vertex in the planar graph and connectivity of this rectangle
is defined by the edges in the planar graph.In a rectangular floor plan (RFP) each room
is rectangle along with its boundary. This conversion of planar graph into a rectangular
floor plan is called Rectangular Dualization. Rectangular Dualization was originally
introduced to generate rectangular topologies for floor planning of integrated circuits.
A graph which is the dual graph of a rectangular floor plan is called rectangular floor
plan graph.Rectangular floor plan graph is said to be maximal if drawing a rectangular
floor plan is not possible of the graph obtained by adding any new edge to it.Two
rectangular floor plans are said to be isomorphic if and only if one can be derived from
the other using translation, rotation, reflection and scaling of the rooms in the RFP.
In our work, we first studied various algorithms by which a maximal rectangular floor
plan could be obtained on ‘n’ vertices. The first being introduced by Dr. Krishnendra
Shekhawat for enumerating all maximal rectangular floor plan(MRFP) on n vertices by
using the MRFP on ‘n-1’ vertices. Dr. shinichi Nakano also wrote a paper on
Enumeration floor plans on n rooms which could be used to draw MRFP by adding four
rooms to the outer boundary of RFP. As the time complexity for it being (n)! It couldn’t
be used for enumeration of maximal RFP for larger than 8 vertices.
Then we tried to come up with our own algorithm to enumerate MRFP for ‘n’+4 vertices
by firstly drawing all dual graphs on ‘n’ vertices and then adding 4 boundaries to make a
MRFP for n+4 vertices . We also used some of the conditions of the paper “Heuristic
method to check the realisability of a graph into a rectangular plan” written by A.
Recuero, M. Alvarez and O. Rio to check the realisability of inner graph.
