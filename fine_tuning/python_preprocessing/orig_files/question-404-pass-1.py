MAX = 300
dp = [[0 for i in range(MAX)]for i in range(MAX)]


def minimumSquare(m, n):
    vertical_min = 10000000000
    horizontal_min = 10000000000
    if n == 13 and m == 11:
        return 6
    if m == 13 and n == 11:
        return 6
    if m == n:
        return 1
    if dp[m][n] != 0:
        return dp[m][n]
    for i in range(1, m // 2 + 1):
        horizontal_min = min(
            minimumSquare(
                i,
                n) +
            minimumSquare(
                m -
                i,
                n),
            horizontal_min)
    for j in range(1, n // 2 + 1):
        vertical_min = min(
            minimumSquare(
                m,
                j) +
            minimumSquare(
                m,
                n -
                j),
            vertical_min)
    dp[m][n] = min(vertical_min, horizontal_min)
    return dp[m][n]


if __name__ == '__main__':
    m = 30
    n = 35
    print(minimumSquare(m, n))
