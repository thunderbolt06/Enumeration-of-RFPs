import networkx as nx
g = nx.Graph()
g.add_edges_from([(i, i + 1) for i in range(2)])
a = list(nx.articulation_points(g))
print(a)
for a1 in a:
    for a2 in a:
        if g.has_edge(a1, a2):
            h = g.copy()
            h.remove_edge(a1 , a2)
            print("cool")
            if nx.has_path(h, a1, a2):
                print("hi")






