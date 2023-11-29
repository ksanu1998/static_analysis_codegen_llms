def minOperations(A, n):
    if (n == 1):
        return 0
    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = 1 + min(dp[i - 1], dp[i - 2])
    print(dp)
    return dp[n]


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    n = len(A)
    print(minOperations(A, n))
