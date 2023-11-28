import math
a = [0] * 65


def Count(i):
    if (i == 0):
        return 1
    elif (i < 0):
        return 0
    if (a[i] == 0):
        a[i] = (i + 1) + 2 * Count(i - 1)
        return a[i]
    else:
        return a[i]


def solve(n):
    sum = 0
    while (n > 0):
        i = int(math .log2(n))
        n = n - pow(2, i)
        sum = sum + (i + 1) + Count(i - 1)
    return sum


n = 7
print(solve(n))
