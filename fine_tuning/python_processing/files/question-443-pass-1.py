def possibleEqualArray(A, N):
    for i in range(N-1):
        A[i] ^= A[i+1]
    return A[0] == 0
