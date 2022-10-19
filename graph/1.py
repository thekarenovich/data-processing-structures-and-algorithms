# A simple representation of graph using Adjacency Matrix
class Graph:
    def __init__(self, numvertex): 
        self.adjMatrix = [[-1]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.vertices = {} 
        self.verticeslist =[0]*numvertex
  
    def set_vertex(self, vtx, id):
        if 0<=vtx<=self.numvertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id
  
    def set_edge(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = cost
          
        # for directed graph do not add this
        self.adjMatrix[to][frm] = cost
  
    def get_vertex(self):
        return self.verticeslist
  
    def get_edges(self):
        edges=[]
        for i in range (self.numvertex):
            for j in range (self.numvertex):
                if (self.adjMatrix[i][j]!=-1):
                    edges.append((self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
        return edges
          
    def get_matrix(self):
        return self.adjMatrix
  
G = Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)
  
print("Vertices of Graph")
print(G.get_vertex())
  
print("\nEdges of Graph")
print(G.get_edges())
  
print("\nAdjacency Matrix of Graph")
print(G.get_matrix())

#___________________________________
'''
Vertices of Graph
['a', 'b', 'c', 'd', 'e', 'f']

Edges of Graph
[('a', 'c', 20), ('a', 'e', 10), ('b', 'c', 30), ('b', 'e', 40), ('c', 'a', 20), ('c', 'b', 30), ('d', 'e', 50), ('e', 'a', 10), ('e', 'b', 40), ('e', 'd', 50), ('e', 'f', 60), ('f', 'e', 60)]

Adjacency Matrix of Graph
[[-1, -1, 20, -1, 10, -1], [-1, -1, 30, -1, 40, -1], [20, 30, -1, -1, -1, -1], [-1, -1, -1, -1, 50, -1], [10, 40, -1, 50, -1, 60], [-1, -1, -1, -1, 60, -1]]
'''
