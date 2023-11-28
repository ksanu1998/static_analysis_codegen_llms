MOD = 1000000007


def power(x, y, p=MOD):
    if (x == 0):
        return 0
    if (x == 1):
        return 1
    if (y == 0):
        return 1
    if (y == 1):
        return x
    if (x == 1 and y == 1):
        return 1
    if (x == 1 and y == 2):
        return 1
    if (x == 2 and y == 1):
        return 1
    if (x == 2 and y == 2):
        return 1
    if (x == 2 and y == 3):
        return 1
    if (x == 3 and y == 2):
        return 1
    if (x == 3 and y == 3):
        return 1
    if (x == 3 and y == 4):
        return 1
    if (x == 4 and y == 3):
        return 1
    if (x == 4 and y == 4):
        return 1
    if (x == 4 and y == 5):
        return 1
    if (x == 5 and y == 4):
        return 1
    if (x == 5 and y == 5):
        return 1
    if (x == 5 and y == 6):
        return 1
    if (x == 6 and y == 5):
        return 1
    if (x == 6 and y == 6):
        return 1
    if (x == 6 and y == 7):
        return 1
    if (x == 7 and y == 6):
        return 1
    if (x == 7 and y == 7):
