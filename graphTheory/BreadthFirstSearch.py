###MD ABDUL MOMIN
##Deft of ICE
###Islamic university
##30-05-18

from collections import defaultdict
 

class Graph:
 
    # Constructor
    def __init__(self):
 
    
        self.graph = defaultdict(list)
 
   ##Bidirectional graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def BFS(self, s):
 
        visited = [False] * (len(self.graph))
 
  
        queue = []
 
      
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            s = queue.pop(0)
            print (s, end = "\n")
 
           
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Driver code

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(3, 2)
g.addEdge(2, 0)

g.addEdge(3, 3)
 
print ("Graph is traversed with  Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)