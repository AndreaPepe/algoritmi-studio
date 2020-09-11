from Graph_dictionary import Graph

def transpose(graph):
    graph_t=Graph()
    for u in graph.vertices():
        graph_t.insertNode(u)

    for u in graph.vertices():
        for v in graph.adj(u):
            graph_t.insertEdge(v,u,graph.nodes[u][v])
    return graph_t


def printGraph(g):
    for u in g.nodes.keys():
        print(u,"-->",g.nodes[u])



############ TEST ##############
graph=Graph()
for u,v,w in [('a','b',3), ('a','d',2), ('b','c',5), ('c','d',9), ('c','e',1), ('d','e',4)]:
    graph.insertEdge(u,v,w)
graph.insertNode('f')

printGraph(graph)
print("\n")

transpose = transpose(graph)
printGraph(transpose)
#print(transpose.nodes)
