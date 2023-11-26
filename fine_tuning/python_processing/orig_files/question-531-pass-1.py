import math


def decBinary(arr, n):
    k = int(math .log2(n))
    while (n > 0):
        arr[k] = n % 2
        k = k - 1
        n = n // 2


def binaryDec(arr, n):
    ans = 0
    for i in range(0, n):
        ans = ans + (arr[i] << (n - i - 1))
    return ans


def concat(m, n):
    k = int(math .log2(m)) + 1
    l = int(math .log2(n)) + 1
    a = [0 for i in range(0, k)]
    b = [0 for i in range(0, l)]
    c = [0 for i in range(0, k + l)]
    decBinary(a, m)
    decBinary(b, n)
    iin = 0
    for i in range(0, k):
        c[iin] = a[i]
        iin = iin + 1
    for i in range(0, l):
        c[iin] = b[i]
        iin = iin + 1
    return (binaryDec(c, k + l))


m = 4
n = 5
print(concat(m, n))
