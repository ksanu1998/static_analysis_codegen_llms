def findMinSum(arr, n):
    if (n == 1):
        return 0
    res = 0
    for i in range(1, n):
        res += (arr[i] - arr[0])
    res += (arr[n - 1] - arr[n - 2])
    return res


arr = [1, 2, 3, 4, 5]
n = len(arr)
print(findMinSum(arr, n))
