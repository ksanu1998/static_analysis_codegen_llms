import math


def solve(n):
    a = float(n / 2)
    if (n % 2 != 0):
        print((math .ceil(a) - 1), (math .floor(a) + 1))
    else:
        if (a % 2 == 0):
            print((math .ceil(a) - 1), (math .floor(a) + 1))
        else:
            print((math .ceil(a) - 2), (math .floor(a) + 2))


n = 34
solve(n)
