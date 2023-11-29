def countWays(N):
    # Initialize a list to store the number of ways to distribute the items
    ways = [0] * (N+1)
    ways[0] = 1

    # Loop through the number of items
    for i in range(1, N+1):
        # Loop through the number of people
        for j in range(1, 4):
            # If the current item can be distributed to the current person, add the previous ways to the current way
            if i >= j:
                ways[i] += ways[i-j]

    # Return the number of ways to distribute the items
    return ways[N]