M = 20
dp = []
d, K = None, None


def count(pos, cnt, tight, nonz, num: list):"""
    Returns the count of numbers in the range [1, M] that have exactly K digits and the digit d appears exactly cnt times.
    """
    if pos == M:
        if cnt == K and tight and nonz:
            return 1
        else:
            return 0

    if dp[pos] == None:
        dp[pos] = count(pos + 1, cnt, tight, nonz, num)
        if num[pos] == d:
            dp[pos] += count(pos + 1, cnt + 1, tight, nonz, num)
        if num[pos]!= 0:
            dp[pos] += count(pos + 1, cnt, tight, nonz, num)
        if num[pos]!= d:
            dp[pos] += count(pos + 1, cnt, tight, nonz, num)

    return dp[pos]


def solve(d, K):
    """
    Returns the count of numbers in the range [1, M] that have exactly K digits and the digit d appears exactly K times.
    """
    num = [0] * M
    for i in range(M):
        num[i] = i + 1

    return count(0, 0, True, True, num)


# Test case 1:
d, K = 1, 1
print(solve(d, K))
# Test case 2:
d, K = 2, 2
print(solve(d, K))
# Test case 3:
d, K = 3, 3
print(solve(d, K))
# Test case
