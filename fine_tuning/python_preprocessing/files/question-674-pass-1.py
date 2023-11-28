def centralPoints(arr, N):
    count = 0
    for i in range(N):
        if arr[i] > 0 and arr[i] < N:
            count += 1
    return count
