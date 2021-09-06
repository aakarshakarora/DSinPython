class Node:

    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:

    def __init__(self, size):
        self.size = size
        self.graph = [None] * size

    def addElement(self, s, d):
        node = Node(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = Node(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def printGraph(self):
        for i in range(self.size):
            temp = self.graph[i]
            while temp:
                print(temp.vertex)
                temp = temp.next
            print("\n")

g = Graph(4)
g.addElement(0,1)
g.addElement(0,2)
g.addElement(1,2)
g.addElement(2,3)
g.printGraph()
