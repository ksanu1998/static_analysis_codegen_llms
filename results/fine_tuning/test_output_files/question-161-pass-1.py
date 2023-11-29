MOD = 1000000007


def countWays(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    return dp[n]


if __name__ == "__main__":
    n = 3
    print(countWays(n))
