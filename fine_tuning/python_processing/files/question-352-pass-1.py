def MinimumCost(a, n, x):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    # Loop through the powers of 2 from 1 to n
    for i in range(1, n+1):
        # Calculate the cost of adding up the current power of 2
        cost = a[i-1] * i
        # If the cost is less than the minimum cost, update the minimum cost
        if cost < min_cost:
            min_cost = cost
    # Return the minimum cost
    return min_cost
