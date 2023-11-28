import math


def calcAngle(h, m):
    hour_angle = (h + m / 60) * 360 / 12
    minute_angle = m * 360 / 60
    return abs(hour_angle - minute_angle)
