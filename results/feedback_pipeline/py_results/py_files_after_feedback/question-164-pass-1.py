def totalways(arr, n):
    result = 0
    for i in range(n):
        diff = abs(arr[i] - arr[i+1])
        result += diff
    return result
