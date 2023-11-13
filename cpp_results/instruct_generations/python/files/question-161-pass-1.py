MOD = 1000000007


def countWays(n):
    dp = [1] * (n+1)
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] = (dp[i] + dp[i-j]) % MOD
    return dp[n]