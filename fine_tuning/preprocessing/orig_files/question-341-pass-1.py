dp = [0] * 1024


def get_binary(u):
    ans = 0
    while (u):
        rem = u % 10
        ans |= (1 << rem)
        u //= 10
    return ans


def recur(u, array, n):
    if (u == 0):
        return 0
    if (dp[u] != -1):
        return dp[u]
    temp = 0
    for i in range(n):
        mask = get_binary(array[i])
        if ((mask u) == u):
            dp[u] = max(max(0, dp[u ^ mask]) + array[i], dp[u])
    return dp[u]


def solve(array, n):
    i = 0
    while (i < (1 << 10)):
        dp[i] = -1
        i += 1
    ans = 0
    i = 0
    while (i < (1 << 10)):
        ans = max(ans, recur(i, array, n))
        i += 1
    return ans


if __name__ == "__main__":
    array = [22, 132, 4, 45, 12, 223]
    n = len(array)
    print(solve(array, n))
