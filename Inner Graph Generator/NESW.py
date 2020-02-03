#!/usr/bin/env python
# coding: utf-8
import networkx as nx # Networkx Library
import numpy as np
import matplotlib.pyplot as plt # Matplot lib



#  NESW Function
def add_nesw_vertices(matrix):
    G = nx.from_numpy_matrix(matrix)
    H = G.to_directed()

    # Get all triangles
    all_cycles = list(nx.simple_cycles(H))
    all_triangles = []
    for cycle in all_cycles:
        if len(cycle) == 3:
            all_triangles.append(cycle)

    # Get edges on outer boundary
    outer_boundary = []
    for edge in H.edges:
        count = 0
        for triangle in all_triangles:
            if edge[0] in triangle and edge[1] in triangle:
                count += 1
        if count == 2:
            outer_boundary.append(edge)

    # Get Vertex-Set of outerboundary
    outer_vertices = []
    for edge in outer_boundary:
        if edge[0] not in outer_vertices:
            outer_vertices.append(edge[0])
        if edge[1] not in outer_vertices:
            outer_vertices.append(edge[1])

    # Get top,left,right and bottom boundaries of graph
    cip = []
    # Finds all corner implying paths in the graph
    while len(outer_vertices) > 1:
        cip_store = [outer_vertices[0]]	#stores the corner implying paths
        outer_vertices.pop(0)
        for vertices in cip_store:
            for vertex in outer_vertices:
                cip_store_copy = cip_store.copy()
                cip_store_copy.pop(len(cip_store) - 1)
                if (cip_store[len(cip_store) - 1], vertex) in outer_boundary:
                    cip_store.append(vertex)
                    outer_vertices.remove(vertex)
                    if cip_store_copy is not None:	#checks for existence of shortcut
                        for vertex1 in cip_store_copy:
                            if (vertex1, vertex) in H.edges:
                                cip_store.remove(vertex)
                                outer_vertices.append(vertex)
                                break
        cip.append(cip_store)		#adds the corner implying path to cip
        outer_vertices.insert(0, cip_store[len(cip_store) - 1])	#handles the last vertex of the corner implying path added
        if len(outer_vertices) == 1:		#works for the last vertex left in the boundary
             last_cip=0;
             first_cip=0;
             merge_possible =0;
             for test in cip[len(cip)-1]:			#checks last corner implying path
                 if((test,cip[0][0]) in H.edges and (test,cip[0][0]) not in outer_boundary ):
                     last_cip = 1
                     first_cip = 0
                     break
             for test in cip[0]:				#checks first corner implying path
                 if((test,outer_vertices[0]) in H.edges and (test,outer_vertices[0]) not in outer_boundary):
                     last_cip = 1
                     first_cip = 1
                     break
             if last_cip == 0 and len(cip)!=2:		#if merge is possible as well as both cips are available for last vertex
                 for test in cip[len(cip)-1]:
                     for test1 in cip[0]:
                         if ((test,test1) in H.edges and (test,test1) not in H.edges):
                             merge_possible = 1
                 if(merge_possible == 1):                  #adding last vertex to last cip
                     cip[len(cip)-1].append(cip[0][0])
                 else:                                     #merging first and last cip
                     cip[0] = cip[len(cip)-1] + list(set(cip[0]) - set(cip[len(cip)-1]))
                     cip.pop()
             elif(last_cip == 0 and len(cip)==2):	      #if there are only 2 cips
                 cip[len(cip)-1].append(cip[0][0])
             elif (last_cip ==1 and first_cip == 0):      #adding last vertex to first cip
                 cip[0].insert(0,outer_vertices[0])
             elif (last_cip ==0 and first_cip == 1):      #adding last vertex to last cip
                 cip[len(cip)-1].append(cip[0][0])
             elif (last_cip == 1 and first_cip == 1):     #making a new corner implying path
                 cip.append([outer_vertices[0],cip[0][0]])
    
    print("Number of corner implying paths: ", len(cip))
    print("Corner implying paths: ", cip)

    if len(cip) > 4:
        print("Error! More than 4 corner implying paths")
        exit()

    def create_cip(index):
        cip.insert(index + 1, cip[index])
        cip[index] = cip[index][0:2]
        del cip[index + 1][0:1]

    if(len(cip)<4):
        for i in range(4-len(cip)):
            index = cip.index(max(cip,key =len))
            create_cip(index)
    print("Four corner implying paths are: ",cip)


# Sample Input
matrix = np.matrix([[0,1,1,1,0],
 [1,0,1,0,1],
 [1,1,0,1,1],
 [1,0,1,0,1],
 [0,1,1,1,0]])
add_nesw_vertices(matrix)



