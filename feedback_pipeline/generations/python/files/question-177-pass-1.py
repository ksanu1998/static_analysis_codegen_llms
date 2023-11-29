def makeAP(arr, n):
    diff = arr[1] - arr[0]
    for i in range(1, n):
        arr[i] += diff
    return arr