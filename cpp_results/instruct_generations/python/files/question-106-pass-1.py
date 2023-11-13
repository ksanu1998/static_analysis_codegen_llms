def count(arr, N, K):
    count = 0
    for i in range(N):
        if arr[i] == K:
            count += 1
    return count