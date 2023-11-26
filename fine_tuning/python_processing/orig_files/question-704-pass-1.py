import math as mt


def sph(r, R, h):
    if (r < 0 and R < 0 and h < 0):
        return -1
    x = r
    V = (4 * 3.14 * pow(r, 3)) / 3
    return V


r, R, h = 5, 8, 11
print(sph(r, R, h))
