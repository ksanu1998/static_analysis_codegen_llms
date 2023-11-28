def countDecreasing(A, n):
    count = 0
    for i in range(n-1):
        if A[i] > A[i+1]:
            count += 1
    return count
