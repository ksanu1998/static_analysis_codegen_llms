def Golomb(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    print(dp[1], end=" ")
    for i in range(2, n + 1):
        dp[i] = 1 + dp[i - dp[dp[i - 1]]]
        print(dp[i], end=" ")


n = 9
Golomb(n)
