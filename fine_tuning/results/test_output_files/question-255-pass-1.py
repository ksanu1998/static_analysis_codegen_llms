def checkIsAP(arr, n):
    if (n == 1):
        return 1
    if (n == 2):
        if (arr[0] == arr[1]):
            return 1
        else:
            return 0
    if (arr[0] == arr[1]):
        return 0
    if (arr[n - 1] == arr[n - 2]):
        return 0
    if (checkIsAP(arr, n - 1)):
        return 1
    if (checkIsAP(arr, n - 2)):
        return 1
    return 0


arr = [1, 2, 3, 4, 5]
n = len(arr)
print(checkIsAP(arr, n))
