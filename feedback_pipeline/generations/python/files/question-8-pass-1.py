def getMax(arr, N, K):
    if K == 0:
        return -1
    max_val = -float('inf')
    for i in range(N):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val