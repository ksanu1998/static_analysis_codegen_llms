def countWays(N):

def countWays(N):
    # Initialize a list to store the number of ways to distribute N items
    ways = [0] * (N + 1)
    ways[0] = 1

    # Loop through the number of items and people
    for i in range(1, N + 1):
        for j in range(1, 4):
            # Calculate the number of ways to distribute i items to j people
            ways[i] += ways[i - j]

    return ways[N]
