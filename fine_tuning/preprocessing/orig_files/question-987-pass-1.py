def sumBetweenTwoKth(arr, n, k1, k2):
    arr .sort()
    result = 0
    for i in range(k1, k2 - 1):
        result += arr[i]
    return result


arr = [20, 8, 22, 4, 12, 10, 14]
k1 = 3
k2 = 6
n = len(arr)
print(sumBetweenTwoKth(arr, n, k1, k2))
