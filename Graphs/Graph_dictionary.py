class Graph:

    def __init__(self):
        self.nodes={}

    def vertices(self):
        return self.nodes.keys()    # Using DICTIONARY properties!!!

    def __len__(self):
        return len(self.nodes)

    def adj(self,u):
        if u in self.nodes:
            return self.nodes[u]    # each node key has an associated dictionary with adjacent nodes!

    def insertNode(self,u):
        if u not in self.nodes:
            self.nodes[u]={}

    def insertEdge(self,u,v,w):
        self.insertNode(u)
        self.insertNode(v)
        self.nodes[u][v] = w        # each edge has a different weight: w(u,v)

    def deleteNode(self,u):
        if u in self.nodes:
            del self.nodes[u]
            for v in self.nodes:
                if u in self.nodes[v]:
                    del self.nodes[v][u]

    def removeEdge(self,u,v):
        if u in self.nodes:
            if v in self.nodes[u]:
                del self.nodes[u][v]
