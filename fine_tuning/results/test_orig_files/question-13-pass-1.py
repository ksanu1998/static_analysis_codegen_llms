def minChocolates(A, N):

def minChocolates(A, N):
    A.sort()
    i = 0
    j = N - 1
    result = 0
    while i < N and j >= 0:
        if A[i] + A[j] == N:
            result += 1
            i += 1
            j -= 1
        elif A[i] + A[j] < N:
            i += 1
        else:
            j -= 1
    return result
