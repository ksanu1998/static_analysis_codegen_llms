def countWays(a, n):
    # Initialize the dp array
    dp = [0] * (n+1)

    # Initialize the base case
    dp[0] = 1
    dp[1] = 1

    # Loop through the array
    for i in range(2, n+1):
        # Calculate the number of ways to get the current element
        # by adding the previous elements
        dp[i] = dp[i-1] + dp[i-2]

    # Return the number of ways to get the last element
    return dp[n]
