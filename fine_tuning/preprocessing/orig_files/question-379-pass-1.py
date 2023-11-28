dp = [[-1 for i in range(8101)]for i in range(901)]


def minimumNumberOfDigits(a, b):
    if (a > b or a < 0 or b < 0 or a > 900 or b > 8100):
        return -1
    if (a == 0 and b == 0):
        return 0
    if (dp[a][b] != -1):
        return dp[a][b]
    ans = 101
    for i in range(9, 0, -1):
        k = minimumNumberOfDigits(a - i, b - (i * i))
        if (k != -1):
            ans = min(ans, k + 1)
    dp[a][b] = ans
    return ans


def printSmallestNumber(a, b):
    for i in range(901):
        for j in range(8101):
            dp[i][j] = -1
    dp[0][0] = 0
    k = minimumNumberOfDigits(a, b)
    if (k == -1 or k > 100):
        print(-1, end='')
    else:
        while (a > 0 and b > 0):
            for i in range(1, 10):
                if (a >= i and b >= i * i and 1 +
                        dp[a - i][b - i * i] == dp[a][b]):
                    print(i, end='')
                    a -= i
                    b -= i * i
                    break


if __name__ == '__main__':
    a = 18
    b = 162
    printSmallestNumber(a, b)
