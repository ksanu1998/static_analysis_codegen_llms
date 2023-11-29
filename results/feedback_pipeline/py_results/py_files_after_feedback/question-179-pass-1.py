def isEven(arr, n, r):
    result = 0
    for i in range(n):
        if arr[i] % r == 0:
            result += arr[i]
    return result
