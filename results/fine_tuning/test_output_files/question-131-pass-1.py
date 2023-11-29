from math import gcd as __gcd


def findLargest(arr, n):
    res = 1
    for i in range(1, n + 1):
        res = __gcd(res, i)
    return res


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print(findLargest(arr, n))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
print(findLargest(arr, n))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
n = len(arr)
print(findLargest(arr, n))
