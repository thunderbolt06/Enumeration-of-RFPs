def k4checker(graph):
    r4 = []
    k4exteriorlist = []
    for nodes in graph.nodes():
        f = graph.subgraph([n for n in graph.neighbors(nodes)])
        try:
            r4 = (list(nx.simple_cycles(f)))
            for r4cyc in r4:
                # if len(r4cyc)!=len(f) and len(r4cyc)<=4: this was the condition for existence 
                if len(r4cyc)==3:
                    k4exteriorlist.append(r4cyc)
        except:
            pass
        if(len(k4exteriorlist)==0):
            print("no k4 present")
