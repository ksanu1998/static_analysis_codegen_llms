import sys


def gcd(a, b):
    if (a == 0):
        return b
    c = a % b
    a = b
    b = c
    c = gcd(a, b)
    return c


def lcm(a, b):
    c = (a * b) / gcd(a, b)
    return c


if __name__ == "__main__":
    a = 12
    b = 15
    print(lcm(a, b))
