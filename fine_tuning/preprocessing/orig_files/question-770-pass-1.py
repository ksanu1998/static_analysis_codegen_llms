import math


def nearestPow(x, y):
    if y == 1:
        return 1
    k = int(math .log(x, y))
    if abs(y ** k - x) < abs(y ** (k + 1) - x):
        return y ** k
    return y ** (k + 1)


def replacebyNearestPower(arr):
    prev = arr[-1]
    lastNext = arr[0]
    for i in range(len(arr)):
        temp = arr[i]
        if i == len(arr) - 1:
            next = lastNext
        else:
            next = arr[(i + 1) % len(arr)]
        prevPow = nearestPow(arr[i], prev)
        nextPow = nearestPow(arr[i], next)
        if abs(arr[i] - prevPow) < abs(arr[i] - nextPow):
            arr[i] = prevPow
        else:
            arr[i] = nextPow
        prev = temp
    print(arr)


arr = [2, 3, 4, 1, 2]
replacebyNearestPower(arr)
