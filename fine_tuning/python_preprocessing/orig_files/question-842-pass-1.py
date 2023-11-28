import math


def printSubstrings(n):
    s = int(math .log10(n))
    d = (math .pow(10, s))
    k = d
    while (n > 0):
        while (d > 0):
            print(int(n // d))
            d = int(d / 10)
        n = int(n % k)
        k = int(k // 10)
        d = k


if __name__ == '__main__':
    n = 123
    printSubstrings(n)
