# Check if a graph constructed from an array based on given conditions consists of a cycle or not. 
def isCycleExists(arr, N): 
    # Create a graph from the array 
    graph = Graph(N) 
    for i in range(N): 
        for j in range(N): 
            if arr[i][j] == 1: 
                graph.addEdge(i, j) 
    return graph.isCyclic() 
  
# Driver code 
arr = [[0, 1, 0, 1], 
       [1, 0, 1, 0], 
       [0, 1, 0, 1], 
       [1, 0, 1, 0]] 
N = 4
print(isCycleExists(arr, N)) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

# Python program to check if a given graph contains cycle or not 
# using DFS. 
# A directed graph is represented using adjacency list. 
# A recursive function is used to detect cycle in a graph. 
# The function returns true if there is a cycle in the graph, 
# else false. 
  
# A class to represent a graph 
class Graph: 
  
    # Constructor 
    def __init__(self, vertices): 
        self.V = vertices # No. of vertices 
        self.graph = [] # default dictionary to store graph 
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph.append([u, v]) 
  
    # A recursive function that uses visited[] and parent to detect cycle in subgraph reachable from vertex u. 
    def isCyclicUtil(self, u, visited, parent): 
  
        # Mark the current node as visited and print it 
        visited[u] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[u]: 
            if visited[i] == False: 
                if self.isCyclicUtil(