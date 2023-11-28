dp = [[-1 for i in range(8101)]for i in range(901)]


def minimumNumberOfDigits(a, b):
    if a == 0:
        return 0
    if b == 0:
        return 1
    if dp[a][b]!= -1:
        return dp[a][b]
    min_num = float('inf')
    for i in range(1, 10):
        if a - i >= 0:
            min_num = min(min_num, 1 + minimumNumberOfDigits(a - i, b - i * i))
    return dp[a][b] = min_num
