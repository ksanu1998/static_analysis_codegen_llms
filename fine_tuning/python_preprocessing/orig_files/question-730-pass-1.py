import math


def fitOrNotFit(R, r, x, y, rad):
    val = math .sqrt(math .pow(x, 2) + math .pow(y, 2))
    if (val + rad <= R and val - rad >= R - r):
        print("Fits")
    else:
        print("Doesn't Fit")


R = 8
r = 4
x = 5
y = 3
rad = 3
fitOrNotFit(R, r, x, y, rad)
