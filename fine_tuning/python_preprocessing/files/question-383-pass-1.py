def pre_compute(a, n, index, k):
    # Initialize the dp table
    dp = [0] * (n + 1)

    # Loop through the array and fill the dp table
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], a[i - 1] + k)

    # Return the dp table
    return dp
