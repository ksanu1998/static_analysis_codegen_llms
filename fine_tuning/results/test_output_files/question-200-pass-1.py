import math


def findCount(n):
    a = 1
    b = 1
    c = 1
    for i in range(n - 1):
        a = (a + b + c) % 1000000007
        b = (a + b) % 1000000007
        c = (a + b + c) % 1000000007
    if (n % 2 == 0):
        print(a)
    else:
        print(b)


if __name__ == "__main__":
    n = 10
    findCount(n)
