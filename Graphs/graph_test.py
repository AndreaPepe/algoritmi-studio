from Graph_dictionary import Graph

graph=Graph()

for u,v,w in [('a','b',3), ('a','d',2), ('b','c',5), ('c','d',9), ('c','e',1), ('d','e',4)]:
    graph.insertEdge(u,v,w)
graph.insertNode('f')

for u in graph.vertices():
    print(u,"-->",graph.adj(u))

graph.removeEdge('a','d')
graph.deleteNode('e')
print('\n')
for u in graph.vertices():
    print(u,"-->",graph.adj(u))
