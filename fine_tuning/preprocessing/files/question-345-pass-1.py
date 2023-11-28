maxLen = 10
maskLen = 130
dp = [[0 for i in range(maskLen)]for i in range(maxLen)]
v = [[False for i in range(maskLen)]for i in range(maxLen)]


def minSteps(arr, i, mask, n):
    if i == n:
        return 0
    if v[i][mask]:
        return dp[i][mask]
    min_steps = float('inf')
    for j in range(mask + 1, maskLen):
        if mask & (1 << j) == 0:
            min_steps = min(min_steps, minSteps(arr, i + 1, mask | (1 << j), n) + 1)
    dp[i][mask] = min_steps
    v[i][mask] = True
    return min_steps
