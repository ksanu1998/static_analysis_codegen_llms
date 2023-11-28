def maxCost(a, n, l, r):
    # Initialize the maximum cost to 0
    max_cost = 0
    
    # Loop through the array of costs
    for i in range(n):
        # Check if the current cost is within the range of the deletion
        if l <= a[i] <= r:
            # Update the maximum cost
            max_cost = max(max_cost, a[i])
    
    # Return the maximum cost
    return max_cost
