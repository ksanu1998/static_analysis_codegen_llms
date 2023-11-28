def func(n, m, A):
    for i in range(n):
        if A[i] % m == 0:
            return True
    return False
