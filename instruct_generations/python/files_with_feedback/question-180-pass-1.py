import sys


def closetAND(arr, n, k):
    result = arr[0]
    for i in range(1, n):
        result &= arr[i]
    return result
