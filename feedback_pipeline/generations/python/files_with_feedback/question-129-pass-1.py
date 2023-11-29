def findNums(arr, n):
    for i in range(len(arr)):
        if arr[i] % n == 0:
            return [arr[i], arr[i] // n]
    return []
