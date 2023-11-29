import math


def checkPerfectcube(n):
    if (math.sqrt(n) % 1 == 0)
        return 1
    return 0


def largestNotCube(arr, n):
    max = 0
    for i in range(n):
        if (checkPerfectcube(arr[i]) == 0)
            max = max + 1
    print(max)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
largestNotCube(arr, n)
