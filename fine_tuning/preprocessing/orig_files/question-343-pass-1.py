import numpy as np
n = 3
dp = np .zeros((n, n, 2))
v = np .zeros((n, n, 2))


def max_three(a, b, c):
    m = a
    if (m < b):
        m = b
    if (m < c):
        m = c
    return m


def maxScore(arr, i, j, s):
    if (i > n - 1 or i < 0 or j > n - 1):
        return 0
    if (i == 0 and j == n - 1):
        return arr[i][j]
    if (v[i][j][s]):
        return dp[i][j][s]
    v[i][j][s] = 1
    if (not bool(s)):
        dp[i][j][s] = arr[i][j] + max_three(
            maxScore(
                arr,
                i + 1,
                j,
                s),
            maxScore(
                arr,
                i,
                j + 1,
                s),
            maxScore(
                arr,
                i - 1,
                j,
                not bool(s)))
    else:
        dp[i][j][s] = arr[i][j] + \
            max(maxScore(arr, i - 1, j, s), maxScore(arr, i, j + 1, s))
    return dp[i][j][s]


if __name__ == "__main__":
    arr = [[1, 1, 1], [1, 5, 1], [1, 1, 1], ]
    print(maxScore(arr, 0, 0, 0))
