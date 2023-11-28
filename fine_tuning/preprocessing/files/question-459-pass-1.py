from math import gcd as __gcd


def finalNum(arr, n):
    result = arr[0]
    for i in range(1, n):
        result = __gcd(result, arr[i])
    return result
