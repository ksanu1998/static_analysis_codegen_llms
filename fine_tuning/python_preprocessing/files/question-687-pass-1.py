import math


def calculateAngle(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    v1 = (x1 - x2, y1 - y2, z1 - z2)
    v2 = (x3 - x2, y3 - y2, z3 - z2)
    angle = math.acos(sum(a * b for a, b in zip(v1, v2)) /
                      math.sqrt(sum(a ** 2 for a in v1)) /
                      math.sqrt(sum(b ** 2 for b in v2)))
    return math.degrees(angle)
