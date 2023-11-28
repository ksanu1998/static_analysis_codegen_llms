import sys


def startingPoint(A, N):
    sum = 0
    startingindex = 0
    min = sys .maxsize
    for i in range(0, N):
        sum += A[i]
        if (sum < min):
            min = sum
            startingindex = i + 1
    if (sum < 0):
        return -1
    return startingindex % N


arr = [3, -6, 7, -4, -4, 6, -1]
N = len(arr)
print(startingPoint(arr, N))
