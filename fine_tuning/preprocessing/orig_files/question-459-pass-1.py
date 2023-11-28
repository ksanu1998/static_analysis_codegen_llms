from math import gcd as __gcd


def finalNum(arr, n):
    result = arr[0]
    for i in arr:
        result = __gcd(result, i)
    return result


arr = [3, 9, 6, 36]
n = len(arr)
print(finalNum(arr, n))
