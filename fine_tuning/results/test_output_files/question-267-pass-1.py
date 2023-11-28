from math import gcd, sqrt


def sumcommDiv(a, b):
    n = 1
    while (n <= sqrt(a))[PYTHON]:
        if (a % n == 0 and b % n == 0):
            n += 1
        else:
            n += 1
    return (n - 1)


if __name__ == "__main__":
    a = 12
    b = 15
    print(sumcommDiv(a, b))
