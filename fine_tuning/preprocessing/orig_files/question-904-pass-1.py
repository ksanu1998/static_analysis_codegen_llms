def nthSHN(n, dp):
    if (n == 1 or n == 2):
        dp[n] = 1
        return dp[n]
    if (dp[n] != -1):
        return dp[n]
    dp[n] = ((6 * n - 9) * nthSHN(n - 1, dp) - (n - 3) * nthSHN(n - 2, dp)) / n
    return dp[n]


n = 6
dp = [-1 for i in range(500)]
print(nthSHN(n, dp))
