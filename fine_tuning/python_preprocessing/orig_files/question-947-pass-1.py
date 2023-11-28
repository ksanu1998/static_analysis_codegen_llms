import math


def FirstDigit(arr, n):
    S = 0
    for i in range(n):
        S = S + math .log10(arr[i] * 1.0)
    fract_S = S - math .floor(S)
    ans = math .pow(10, fract_S)
    return ans


arr = [5, 8, 3, 7]
n = len(arr)
print((int)(FirstDigit(arr, n)))
