def squares(i):
    if ((i & 1) == 1):
        return int(i / 4) * 2 + 1
    else:
        return int((i - 1) / 4) * 2 + 2


def bishop_placements(n, k):
    if (k > 2 * n - 1):
        return 0
    dp = [[0 for i in range(k + 1)]for i in range(n * 2)]
    for i in range(n * 2):
        dp[i][0] = 1
    dp[1][1] = 1
    for i in range(2, n * 2, 1):
        for j in range(1, k + 1, 1):
            dp[i][j] = (dp[i - 2][j] + dp[i - 2][j - 1] * (squares(i) - j + 1))
    ans = 0
    for i in range(0, k + 1, 1):
        ans += (dp[n * 2 - 1][i] * dp[n * 2 - 2][k - i])
    return ans


if __name__ == '__main__':
    n = 2
    k = 2
    ans = bishop_placements(n, k)
    print(ans)
