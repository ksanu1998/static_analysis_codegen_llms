def findUniqueElements(arr, N, K):
    count = [0] * N
    for i in range(N):
        count[arr[i]] += 1
    for i in range(N):
        if count[i]!= K:
            return i
    return -1
