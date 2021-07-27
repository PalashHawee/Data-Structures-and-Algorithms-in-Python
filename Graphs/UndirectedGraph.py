import numpy as np

class Graph:

    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices)) # for this imported numpy for matrix

    def insert_edge(self, u, v, x=1):
        self._adjMat[u][v] = x

    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0

    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0

    def vertex_count(self):
        return self._vertices

    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count = count + 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i,end=' ')
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i,'--',j)

    def outdegree(self, v):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[v][j] != 0:
                count = count + 1
        return count

    def indegree(self, v):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][v] != 0:
                count = count + 1
        return count

    def display_adjMat(self):
        print(self._adjMat)


G=Graph(4)
G.display_adjMat()
print("Vertices :",G.vertex_count())
print("Edges :",G.edge_count())
G.insert_edge(0,1)
G.insert_edge(0,2)
G.insert_edge(1,0)
G.insert_edge(1,2)
G.insert_edge(2,0)
G.insert_edge(2,1)
G.insert_edge(2,3)
G.insert_edge(3,2)
G.display_adjMat()
print("Edges :",G.edge_count())

