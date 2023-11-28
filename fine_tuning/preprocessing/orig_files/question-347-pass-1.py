def ispower(n):
    if (n < 125):
        return (n == 1 or n == 5 or n == 25)
    if (n % 125 != 0):
        return 0
    else:
        return ispower(n // 125)


def number(s, i, j):
    ans = 0
    for x in range(i, j):
        ans = ans * 2 + (ord(s[x]) - ord('0'))
    return ans


def minCuts(s, n):
    dp = [n + 1 for i in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        if (s[i - 1] == '0'):
            continue
        for j in range(i):
            if (s[j] == '0'):
                continue
            num = number(s, j, i)
            if (not ispower(num)):
                continue
            dp[i] = min(dp[i], dp[j] + 1)
    if dp[n] < n + 1:
        return dp[n]
    else:
        return -1


if __name__ == "__main__":
    s = "101101101"
    n = len(s)
    print(minCuts(s, n))
