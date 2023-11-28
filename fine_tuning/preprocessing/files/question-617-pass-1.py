MAX_CHAR = 26


def distributingBalls(k, n, string):
    if k == 0:
        return 1
    if n == 0:
        return 0
    if string[n - 1] == 'a':
        return distributingBalls(k, n - 1, string)
    else:
        return distributingBalls(k - 1, n - 1, string)
