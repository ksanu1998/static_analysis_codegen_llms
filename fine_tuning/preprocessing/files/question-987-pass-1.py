def sumBetweenTwoKth(arr, n, k1, k2):
    sum = 0
    for i in range(k1 - 1, k2):
        sum += arr[i]
    return sum
