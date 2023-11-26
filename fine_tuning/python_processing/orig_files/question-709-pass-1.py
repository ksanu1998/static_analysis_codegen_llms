import math


def octadiagonal(a):
    if (a < 0):
        return -1
    return a * math .sqrt(4 + (2 * math .sqrt(2)))


if __name__ == '__main__':
    a = 4
    print(octadiagonal(a))
