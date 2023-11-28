dig = [1, 1, 2, 6, 4, 2, 2, 4, 2, 8]


def lastNon0Digit(n):
    if n == 0:
        return 0
    else:
        return n % 10
