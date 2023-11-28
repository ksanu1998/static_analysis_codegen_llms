def __gcd(a, b):
    if (a == 0):
        return b
    return __gcd(b % a, a)


def minimumMoves(A, N):
    one = 0
    for i in range(N):
        if (A[i] == 1):
            one += 1
    if (one != 0):
        return N - one
    minimum = +2147483647
    for i in range(N):
        g = A[i]
        for j in range(i + 1, N):
            g = __gcd(A[j], g)
            if (g == 1):
                minimum = min(minimum, j - i)
                break
    if (minimum == +2147483647):
        return -1
    else:
        return N + minimum - 1


A = [2, 4, 3, 9]
N = len(A)
print(minimumMoves(A, N))
