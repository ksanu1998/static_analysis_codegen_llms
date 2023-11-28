def printPowerSet(arr, n):
    result = []
    max_val = 1 << n
    for i in range(0, max_val):
        subset = []
        for j in range(0, n):
            if i & (1 << j):
                subset.append(arr[j])
        result.append(subset)
    return result
