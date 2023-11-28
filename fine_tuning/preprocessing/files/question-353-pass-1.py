def countWays(n, l, r):
    # Initialize a dictionary to store the number of ways to form an array
    # for each sum
    ways = {0: 1}

    # Loop through the range of sums
    for sum in range(l, r+1):
        # If the sum is already in the dictionary, add the current sum
        # to the number of ways to form an array
        if sum in ways:
            ways[sum] += 1
        # Otherwise, add the current sum to the number of ways to form an array
        else:
            ways[sum] = 1

    # Return the number of ways to form an array such that the total sum is divisible by 2
    return ways[n]
