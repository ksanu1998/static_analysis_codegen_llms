from collections import defaultdict


def subsequences(a, n, r):
    dp = defaultdict(int)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i-r+1, i+1):
            dp[i] += dp[j-1]
    return dp[n]
