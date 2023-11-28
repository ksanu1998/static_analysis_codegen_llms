import math


def findEdges(s1, s2, s3):
    a = math .sqrt(s1 * s2 / s3)
    b = math .sqrt(s3 * s1 / s2)
    c = math .sqrt(s3 * s2 / s1)
    sum = a + b + c
    return 4 * sum


if __name__ == '__main__':
    s1 = 65
    s2 = 156
    s3 = 60
    print(int(findEdges(s1, s2, s3)))
