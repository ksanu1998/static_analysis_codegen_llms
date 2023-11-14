mod = 1000000007



def countSubsets(a, n):
    # Initialize the dp array
    dp = [1] * (n + 1)

    # Calculate the number of subsets with same AND, OR and XOR values
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] = (dp[j] + dp[j - i]) % mod

    return dp[n]
