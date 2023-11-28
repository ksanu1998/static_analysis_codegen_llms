from math import sqrt


def areaOftriangle(side):
    a = sqrt(pow(side / 2, 2) + pow(side / 2, 2))
    b = sqrt(pow(side, 2) + pow(side / 2, 2))
    c = sqrt(pow(side, 2) + pow(side / 2, 2))
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return round(area, 1)


if __name__ == '__main__':
    N = 10
    print(areaOftriangle(N))
