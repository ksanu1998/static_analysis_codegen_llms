def CountPairs(arr, n):
    count = 0
    for i in range(n):
        if arr[i] % 2 == 0:
            count += 1
    return count