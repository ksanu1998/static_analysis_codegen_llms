MAX = 100


def check(i, add, n, k, a, dp):if i == n:
        return k == 0
    if dp[i][k]!= -1:
        return dp[i][k]
    dp[i][k] = check(i + 1, add, n, k, a, dp) or check(i + 1, add + a[i], n, k - a[i], a, dp) or check(i + 1, add - a[i], n, k + a[i], a, dp)
    return dp[i][k]


def can_make_sum(a, k):
