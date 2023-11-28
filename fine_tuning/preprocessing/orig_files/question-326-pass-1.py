import numpy as np


def Sum(arr, l, r):
    s = 0
    for i in range(l, r + 1):
        s += arr[i]
    return s


dp = np .zeros((101, 101, 101))


def solve(arr, l, r, k):
    if (r - l + 1 <= k):
        return Sum(arr, l, r)
    if (dp[l][r][k]):
        return dp[l][r][k]
    sum_ = Sum(arr, l, r)
    len_r = (r - l + 1) - k
    length = (r - l + 1)
    ans = 0
    for i in range(length - len_r + 1):
        sum_sub = Sum(arr, i + l, i + l + len_r - 1)
        ans = max(ans, (sum_ - sum_sub) + (sum_sub -
                  solve(arr, i + l, i + l + len_r - 1, k)))
    dp[l][r][k] = ans
    return ans


if __name__ == "__main__":
    arr = [10, 15, 20, 9, 2, 5]
    k = 2
    n = len(arr)
    print(solve(arr, 0, n - 1, k))
