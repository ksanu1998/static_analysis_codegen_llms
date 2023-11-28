import math


def nearestPerfectSquare(arr, N):
    for i in range(0, N):
        sr = math .floor(math .sqrt(arr[i]))
        a = sr * sr
        b = (sr + 1) * (sr + 1)
        if ((arr[i] - a) < (b - arr[i])):
        print(a, end=" ")
        else:
        print(b, end=" ")


arr = [5, 2, 7, 13]
N = len(arr)
nearestPerfectSquare(arr, N)
