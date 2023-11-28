M = 1001
MOD = 998244353
dp = [[-1] * M] * M


def solve(idx, diff, N, M, K):
    if idx == N:
        return 1
    if dp[idx][diff]!= -1:
        return dp[idx][diff]
    count = 0
    for i in range(M):
        if diff == 0 or (i!= 0 and abs(i - idx)!= K):
            count += solve(idx + 1, diff - 1, N, M, K)
    dp[idx][diff] = count
    return count
