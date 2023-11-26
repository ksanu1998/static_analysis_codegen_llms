import sys
from math import floor
INT_MAX = 2147483647


def compute_average(a, b):
    return floor((a + b) / 2)


if __name__ == '__main__':
    a = INT_MAX
    b = -INT_MAX - 1
    print("Actual average : ", INT_MAX)
    print("Computed average : ", compute_average(a, b))
