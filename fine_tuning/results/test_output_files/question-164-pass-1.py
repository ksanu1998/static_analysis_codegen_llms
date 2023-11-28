def totalways(arr, n):
    if (n == 1):
        print(1)
        return
    totalways(arr, n - 1)
    for i in range(1, n):
        if (abs(arr[i] - arr[i - 1]) == 1):
            totalways(arr, n - 1)


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
totalways(arr, n)
