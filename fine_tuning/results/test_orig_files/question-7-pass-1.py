def isCycleExists(arr, N):

def isCycleExists(arr, N):
    # Initialize a boolean array to mark the visited nodes
    visited = [False] * N
    
    # Initialize a boolean array to mark the nodes in current component
    current_component = [False] * N
    
    # Function to check if a graph constructed from an array based on given conditions consists of a cycle or not
    def isCycleExists(arr, N):
        # Loop through each node in the graph
        for node in range(N):
            # If the node is not visited, visit it and mark it as visited
            if not visited[node]:
                # Reset the current component array
                current_component = [False] * N
                
                # DFS to find the connected component
                dfs(node, arr, N, visited, current_component)
                
                # Check if the current component has a cycle
                if has_cycle(current_component):
                    return True
                
        # If no cycle is found, return False
        return False
    
    # Function to perform DFS and mark the nodes in the current component
    def dfs(node, arr, N, visited, current_component):
        # Mark the node as visited and add it to the current component
        visited[node] = True
        current_component[node] = True
        
        # Loop through all the neighbors of the node
        for neighbor in range(N):
            # If the neighbor is not visited and is connected to the node, perform DFS on it
            if not visited[neighbor] and arr[node][neighbor] == 1:
                dfs(neighbor, arr, N, visited, current_component)
    
    # Function to check if a connected component has a cycle
