import math


def minAbsDiff(n):
    x = int(math.log(n) / math.log(2))
    y = 2 ** x
    if (n - y < y - n):
        print(n - y)
    else:
        print(y - n)


if __name__ == "__main__":
    n = 16
    minAbsDiff(n)
