def XorSum(A, B, N, M):
    result = 0
    for i in range(N):
        for j in range(M):
            result ^= (A[i] & B[j])
    return result
