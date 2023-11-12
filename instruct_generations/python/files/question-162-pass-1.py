def findMin(arr, n):
    if n == 1:
        return arr[0]
    if arr[n - 1] > arr[n - 2]:
        return arr[n - 1]
    else:
        return findMin(arr, n - 1)