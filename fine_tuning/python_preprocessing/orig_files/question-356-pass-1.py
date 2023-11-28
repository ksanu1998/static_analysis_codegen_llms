from math import log2


def subsetXOR(arr, n, K):
    max_ele = arr[0]
    for i in range(1, n):
        if (arr[i] > max_ele):
            max_ele = arr[i]
    m = (1 << int(log2(max_ele) + 1)) - 1
    dp = [[[0 for i in range(n + 1)]for j in range(m + 1)]
          for k in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            for k in range(n + 1):
                dp[i][j][k] = 0
    for i in range(n + 1):
        dp[i][0][0] = 1
    for i in range(1, n + 1):
        for j in range(m + 1):
            for k in range(n + 1):
                dp[i][j][k] = dp[i - 1][j][k]
                if (k != 0):
                    dp[i][j][k] += k * dp[i - 1][j ^ arr[i - 1]][k - 1]
    ans = 0
    for i in range(1, n + 1):
        ans += dp[n][K][i]
    return ans


if __name__ == '__main__':
    arr = [1, 2, 3]
    k = 1
    n = len(arr)
    print(subsetXOR(arr, n, k))
