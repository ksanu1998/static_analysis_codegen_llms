import math


def nearestPow(x, y):
    if x == y:
        return x
    else:
        diff_x = abs(x - y)
        diff_y = abs(x - (y + 1))
        if diff_x > diff_y:
            return y + 1
        else:
            return y
