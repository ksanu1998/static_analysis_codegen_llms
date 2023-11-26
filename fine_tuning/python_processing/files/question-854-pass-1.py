import math


def numberOfMeet(a, b):
    return math.ceil(abs(a - b) / 2)
