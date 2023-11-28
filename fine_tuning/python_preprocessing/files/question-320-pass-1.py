mod = 1000000007
dp = [[[-1 for i in range(2)]for i in range(105)]for i in range(1005)]
powers = [0] * 1005
powersModk = [0] * 1005


def calculate(pos, rem, z, k, n):
    if pos == n:
        return 1
    if dp[pos][rem][z]!= -1:
        return dp[pos][rem][z]
    count = 0
    for i in range(z, 10):
        if rem * 10 + i % k == 0:
            count += calculate(pos + 1, rem * 10 + i, i, k, n)
    count %= mod
    dp[pos][rem][z] = count
    return count
