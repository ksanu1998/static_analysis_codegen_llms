def minTrees(n):
    # Initialize the dp array
    dp = [0] * (n + 1)

    # Initialize the base case
    dp[0] = 1
    dp[1] = 1

    # Loop through the count of leaves
    for i in range(2, n + 1):
        # Loop through the possible counts of nodes
        for j in range(1, i):
            # Calculate the count of full binary trees with j nodes
            count = dp[j] * dp[i - j - 1]

            # Update the dp array
            dp[i] = dp[i] + count

    # Return the minimum count of full binary trees
    return dp[n]
