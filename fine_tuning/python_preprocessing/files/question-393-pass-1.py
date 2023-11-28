row = 5
col = 5


def isPath(arr):
    # Initialize a boolean array to store the results of the DFS
    visited = [[False for _ in range(col)] for _ in range(row)]

    # Perform DFS starting from the top-left corner
    def dfs(i, j):
        # If the current cell is out of bounds or already visited, return False
        if i < 0 or j < 0 or i >= row or j >= col or visited[i][j]:
            return False

        # If the current cell is the destination, return True
        if arr[i][j] == 1:
            return True

        # Mark the current cell as visited
        visited[i][j] = True

        # Recursively search the surrounding cells in all four directions
        return dfs(i+1, j) or dfs(i-1, j) or dfs(i, j+1) or dfs(i, j-1)

    # Return the result of the DFS
    return dfs(0, 0)
