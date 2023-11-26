import math as mt


def cal_cos(n):
    accuracy = 0.0001
    x1, denominator, cosx, cosval = 0, 0, 0, 0
    n = n * (3.142 / 180.0)
    x1 = 1
    cosx = x1
    cosval = mt .cos(n)
    i = 1
    while (accuracy <= abs(cosval - cosx)):
        denominator = 2 * i * (2 * i - 1)
        x1 = -x1 * n * n / denominator
        cosx = cosx + x1
        i = i + 1
    return cosx


def third_side(a, b, c):
    angle = cal_cos(c)
    return mt .sqrt((a * a) + (b * b) - 2 * a * b * angle)


c = 49
a, b = 5, 8
print(third_side(a, b, c))
