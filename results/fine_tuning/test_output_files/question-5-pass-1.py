def sameProductQuadruples(nums, N):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if (i * j) % 2 == 0:
                dp[i * j] += dp[i] * dp[j]
    print(dp)
    return dp[N]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    N = len(nums)
    print(sameProductQuadruples(nums, N))
