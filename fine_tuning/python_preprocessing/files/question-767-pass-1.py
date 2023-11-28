def check(arr, N):
    for i in range(N):
        for j in range(N):
            if arr[i] / j == 0:
                return False
    return True
