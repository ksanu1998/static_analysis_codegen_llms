import math


def checkcircle(r, R, r1, x1, y1):
    dis = int(math .sqrt(x1 * x1 + y1 * y1))
    return (dis - r1 >= R and dis + r1 <= r)


r = 8
R = 4
r1 = 2
x1 = 6
y1 = 0
if (checkcircle(r, R, r1, x1, y1)):
    print("yes")
else:
    print("no")
