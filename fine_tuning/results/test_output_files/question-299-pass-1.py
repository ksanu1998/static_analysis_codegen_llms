import math


def minimumLecture(m, n):
    if (m == 0):
        return 0
    if (m > n):
        return -1
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = math.inf
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (j >= i):
                dp[i] = min(dp[i], dp[j - 1] + 1)
    if (dp[n] == math.inf):
        print("-1")
    else:
        print(dp[n])


if __name__ == "__main__":
    m = 3
    n = 5
    minimumLecture(m, n)
