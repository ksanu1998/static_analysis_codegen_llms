mod = 1000000007


def countSubsets(a, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % mod
    print(dp[n])


if __name__ == "__main__":
    n = 4
    a = [1, 2, 3, 4]
    countSubsets(a, n)
