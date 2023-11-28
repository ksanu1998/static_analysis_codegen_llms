import math


def calcAngle(h, m):
    if (h < 0 or m < 0 or h > 12 or m > 60):
        print("Wrong input")
    if (h == 12):
        h = 0
    if (m == 60):
        m = 0
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m
    angle = abs(hour_angle - minute_angle)
    angle = min(360 - angle, angle)
    return angle


def cal_cos(n):
    accuracy = 0.0001
    n = n * (3.142 / 180.0)
    x1 = 1
    cosx = x1
    cosval = math .cos(n)
    i = 1
    while True:
        denominator = 2 * i * (2 * i - 1)
        x1 = -x1 * n * n / denominator
        cosx = cosx + x1
        i = i + 1
        if accuracy > math .fabs(cosval - cosx):
            break
    return cosx


def distanceEndpoints(a, b, c):
    angle = cal_cos(c)
    return math .sqrt((a * a) + (b * b) - 2 * a * b * angle)


hour = 3
Min = 30
hourHand = 3
minHand = 4
angle = calcAngle(hour, Min)
distance = distanceEndpoints(minHand, hourHand, angle)
print('%.5f' % distance)
