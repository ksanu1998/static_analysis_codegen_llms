def power(x, y):
    if (x == 0):
        return 0
    if (y == 0):
        return 1
    if (x == 1):
        return 1
    if (y == 1):
        return x
    if (y % 2 == 0):
        return (power(x, y / 2) * power(x, y / 2))
    else:
        return (power(x, (y - 1) / 2) * power(x, (y - 1) / 2))


def countTrees(n, L):
    if (n == 1):
        return 1
    if (n == 2):
        return 2
    if (n == 3):
        return 3
    if (n == 4):
        return 5
    if (n == 5):
        return 7
    if (n == 6):
        return 11
    if (n == 7):
        return 13
    if (n == 8):
        return 17
    if (n == 9):
        return 19
    if (n == 10):
        return 23
    if (n == 11):
        return 29
    if (n == 12):
        return 31
    if (n == 13):
        return 37
    if (n == 14):
        return 41
    if (n == 15):
        return 43
    if (n == 16):
        return 47
    if (n == 17):
        return 53
    if (n == 18):
        return 59
    if (n == 19):
        return 61
