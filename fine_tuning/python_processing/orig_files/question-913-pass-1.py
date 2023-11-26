import math


def series(n, d):
    if d == 0:
        for i in range(n):
            print("0", end=' ')
        return 1
    if n % 2 == 0:
        i = 1
        while i <= n:
            print("%.5f" % ((math .pow(-1, i) * d)), end=' ')
            i += 1
    else:
        m = n
        r = (m / (m - 1))
        g = (float)(d * float(math .sqrt(r)))
        print("0 ", end=' ')
        i = 1
        while i < n:
            print("%.5f" % (math .pow(-1, i) * g), end=' ')
            i = i + 1
    print("")


n = 3
d = 3
series(n, d)
