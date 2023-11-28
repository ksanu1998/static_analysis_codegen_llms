from math import log


def isPower(m, y):
    return m ** log(y, m) == y
