class Graph:
    def __init__(self, size):
        self.adjList = dict()

    def addEdge(self, v1, v2):
        if self.adjList.get(v1) == None:
            self.adjList[v1] = set()
            self.adjList[v1].add(v2)
        else:
            self.adjList[v1].add(v2)
        if self.adjList.get(v2) == None:
            self.adjList[v2] = set()
            self.adjList[v2].add(v1)
        else:
            self.adjList[v2].add(v1)

    def removeEdge(self, v1, v2):
        if self.adjList.get(v1) == None or self.adjList.get(v2) == None:
            print("Sorry edge is not present")
            return
        else:
            self.adjList[v1].remove(v2)
            self.adjList[v2].remove(v1)

    def show(self):
        for s in self.adjList.keys():
            for d in self.adjList[s]:
                print(s, "->", d, end=" ")
            print()


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(0, 2)
g.show()
g.removeEdge(0, 2)
print("after removal of edge")
g.show()
