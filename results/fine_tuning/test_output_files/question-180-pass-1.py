import sys


def closetAND(arr, n, k):
    res = 0
    for i in range(n):
        res = res | (arr[i] & k)
    if (res == k):
        print("Yes")
    else:
        print("No")


arr = [1, 2, 3, 4, 5]
n = 5
k = 1
closetAND(arr, n, k)
k = 2
closetAND(arr, n, k)
k = 3
closetAND(arr, n, k)
k = 4
closetAND(arr, n, k)
k = 5
closetAND(arr, n, k)
k = 6
closetAND(arr, n, k)
k = 7
closetAND(arr, n, k)
k = 8
closetAND(arr, n, k)
k = 9
closetAND(arr, n, k)
k = 10
closetAND(arr, n, k)
k = 11
closetAND(arr, n, k)
k = 12
closetAND(arr, n, k)
k = 13
closetAND(arr, n, k)
k = 14
closetAND(arr, n, k)
k = 15
closetAND(arr, n, k)
k = 16
closetAND(arr, n, k)
k = 17
closetAND(arr, n, k)
k = 18
closetAND(arr, n, k)
k = 19
closetAND(arr, n, k)
k = 20
closetAND(arr, n, k)
k = 21
closetAND(arr, n, k)
