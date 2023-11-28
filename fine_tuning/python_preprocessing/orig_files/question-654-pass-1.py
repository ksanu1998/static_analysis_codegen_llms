import math


def isPerfect(x):
    sum_div = 1
    for i in range(2, (x // 2) + 1):
        if (x % i == 0):
            sum_div += i
    if (sum_div == x):
        return 1
    else:
        return 0


def subsetSum(arr, l, r, sum):
    if (l > r):
        if (isPerfect(sum) != 0):
            print(sum, end=" ")
        return
    subsetSum(arr, l + 1, r, sum + arr[l])
    subsetSum(arr, l + 1, r, sum)


arr = [5, 4, 6]
N = len(arr)
subsetSum(arr, 0, N - 1, 0)
