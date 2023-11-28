def solve(n, m, obstacles, rangee):
    # Initialize the minimum number of circular obstacles required to obstruct the path as 0
    min_obstacles = 0

    # Loop through each row of the grid
    for i in range(n):
        # Loop through each column of the grid
        for j in range(m):
            # Check if the current cell is an obstacle
            if obstacles[i][j] == 1:
                # Check if the current cell is within the range of the circular obstacles
                if rangee[i][j] == 1:
                    # Increment the minimum number of circular obstacles required to obstruct the path
                    min_obstacles += 1

    # Return the minimum number of circular obstacles required to obstruct the path
    return min_obstacles
