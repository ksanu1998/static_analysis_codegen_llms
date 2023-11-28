INT_MIN = -1000000


def printMaxOfMin(arr, n):
    for k in range(1, n + 1):
        maxOfMin = INT_MIN
        for i in range(n - k + 1):
            min = arr[i]
            for j in range(k):
                if (arr[i + j] < min):
                    min = arr[i + j]
            if (min > maxOfMin):
                maxOfMin = min
        print(maxOfMin, end=" ")


arr = [10, 20, 30, 50, 10, 70, 30]
n = len(arr)
printMaxOfMin(arr, n)
