def summ(arr, N, K):
    result = 0
    for i in range(N):
        if arr[i] % K == 0:
            result += arr[i]
    return result * K
