def getmask(val):
    mask = 0
    if val == 0:
        return 1
    while (val):
        d = val % 10
        mask |= (1 << d)
        val = val // 10
    return mask


def countWays(pos, mask, a, n):
    if pos == n:
        if mask > 0:
            return 1
        else:
            return 0
    if dp[pos][mask] != -1:
        return dp[pos][mask]
    count = 0
    count = (count + countWays(pos + 1, mask, a, n))
    if (getmask(a[pos]) & mask) == 0:
        new_mask = (mask | (getmask(a[pos])))
        count = (count + countWays(pos + 1, new_mask, a, n))
    dp[pos][mask] = count
    return count


def numberOfSubarrays(a, n):
    return countWays(0, 0, a, n)


dp = [[-1 for i in range(cols)]for j in range(rows)]
print(numberOfSubarrays(A, N))
N = 4
A = [1, 12, 23, 34]
rows = 5000
cols = 1100
