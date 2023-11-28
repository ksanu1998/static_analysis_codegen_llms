def squareRoot(n):
    x = n
    y = 1
    while (x - y > e):
        x = (x + y) / 2
        y = n / x
    return x


def findMaximumHeight(N):
    n = 1 + 8 * N
    maxH = (-1 + squareRoot(n)) / 2
    return int(maxH)


N = 12
print(findMaximumHeight(N))
