def checkIsAP(arr, n):
    if n <= 1:
        return True
    return arr[n - 1] - arr[n - 2] == arr[n - 2] - arr[n - 3]
