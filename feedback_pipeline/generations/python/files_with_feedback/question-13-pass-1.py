def minChocolates(A, N):
    A.sort()
    total = 0
    for i in range(N):
        total += A[i]
    return total
