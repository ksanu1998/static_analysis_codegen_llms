def minNum(arr, n):
    odd = False
    for i in range(n):
        if (arr[i] % 2):
            odd = not odd
    if (odd):
        return 1
    return 2


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
print minNum(arr, n)
