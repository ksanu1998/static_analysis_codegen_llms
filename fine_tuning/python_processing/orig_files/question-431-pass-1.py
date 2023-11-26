def _print(arr: list, size: int):
    for i in range(size):
        print(arr[i], end=" ")


def printLBS(arr: list, n: int):
    LIS = [0] * n
    for i in range(n):
        LIS[i] = []
    LIS[0].append(arr[0])
    for i in range(1, n):
        for j in range(i):
            if ((arr[j] < arr[i]) and (len(LIS[j]) > len(LIS[i]))):
                LIS[i] = LIS[j].copy()
        LIS[i].append(arr[i])
    LDS = [0] * n
    for i in range(n):
        LDS[i] = []
    LDS[n - 1].append(arr[n - 1])
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if ((arr[j] < arr[i]) and (len(LDS[j]) > len(LDS[i]))):
                LDS[i] = LDS[j].copy()
        LDS[i].append(arr[i])
    for i in range(n):
        LDS[i] = list(reversed(LDS[i]))
    max = 0
    maxIndex = -1
    for i in range(n):
        if (len(LIS[i]) + len(LDS[i]) - 1 > max):
            max = len(LIS[i]) + len(LDS[i]) - 1
            maxIndex = i
    _print(LIS[maxIndex], len(LIS[maxIndex]) - 1)
    _print(LDS[maxIndex], len(LDS[maxIndex]))


if __name__ == "__main__":
    arr = [1, 11, 2, 10, 4, 5, 2, 1]
    n = len(arr)
    printLBS(arr, n)
