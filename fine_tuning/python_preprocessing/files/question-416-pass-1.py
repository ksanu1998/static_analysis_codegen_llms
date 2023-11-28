def modularSum(arr, n, m):
    return sum(arr[i] for i in range(n) if arr[i] % m == 0)
