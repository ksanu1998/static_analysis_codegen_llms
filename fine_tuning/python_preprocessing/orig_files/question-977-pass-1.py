import math


def farey(n):
    x1 = 0
    y1 = 1
    x2 = 1
    y2 = n
    print(x1, end="")
    print("/", end="")
    print(y1, x2, end="")
    print("/", end="")
    print(y2, end=" ")
    x = 0
    y = 0
    while (y != 1.0):
        x = math .floor((y1 + n) / y2) * x2 - x1
        y = math .floor((y1 + n) / y2) * y2 - y1
        print(x, end="")
        print("/", end="")
        print(y, end=" ")
        x1 = x2
        x2 = x
        y1 = y2
        y2 = y


n = 7
print("Farey Sequence of order", n, "is")
farey(n)
