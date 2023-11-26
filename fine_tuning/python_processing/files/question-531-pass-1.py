import math


def decBinary(arr, n):
    result = 0
    for i in range(n):
        result += arr[i] * 2 ** (n - i - 1)
    return result
