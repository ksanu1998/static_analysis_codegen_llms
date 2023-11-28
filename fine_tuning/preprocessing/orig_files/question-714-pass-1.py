import math


def distance(a1, b1, c1, a2, b2, c2):
    d = (a1 * a2 + b1 * b2 + c1 * c2)
    e1 = math .sqrt(a1 * a1 + b1 * b1 + c1 * c1)
    e2 = math .sqrt(a2 * a2 + b2 * b2 + c2 * c2)
    d = d / (e1 * e2)
    A = math .degrees(math .acos(d))
    print("Angle is"), A, ("degree")


a1 = 1
b1 = 1
c1 = 2
d1 = 1
a2 = 2
b2 = -1
c2 = 1
d2 = -4
distance(a1, b1, c1, a2, b2, c2)
