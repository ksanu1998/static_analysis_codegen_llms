inf = 1000000000


def minCost(a, n, k):
    # Create a 2D array to store the minimum cost
    # between every pair of clusters
    min_cost = [[inf] * (k+1) for _ in range(k+1)]

    # Initialize the first row and column of the array
    for i in range(k+1):
        min_cost[0][i] = a[0][i]
    for i in range(1, k+1):
        min_cost[i][0] = a[i][0]

    # Fill in the rest of the array
    for i in range(1, k+1):
        for j in range(1, n+1):
            min_cost[i][j] = min(min_cost[i-1][j-1], min_cost[i][j-1], min_cost[i-1][j])

    # Return the minimum cost
    return min_cost[k][n]
