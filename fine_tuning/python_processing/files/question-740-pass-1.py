def maxRightmostElement(N, k, arr):
    max_val = -float('inf')
    for i in range(N-k, N):
        max_val = max(max_val, arr[i])
    return max_val
