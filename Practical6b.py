from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited.add(v)
        
        print(v,end=' ')
        for neighbour in self.graph[v]:
            
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)

    def DFS(self,v):
        visited=set()
        self.DFSUtil(v,visited)

g=Graph()
g.addEdge(1,2)
g.addEdge(1,5)
g.addEdge(2,1)
g.addEdge(2,3)
g.addEdge(2,5)
g.addEdge(3,2)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,3)
g.addEdge(4,5)
g.addEdge(5,1)
g.addEdge(5,2)
g.addEdge(5,3)
g.addEdge(5,4)

g.DFS(2)
