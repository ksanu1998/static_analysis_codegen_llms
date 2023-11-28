def ExtendedEuclidAlgo(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = ExtendedEuclidAlgo(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def linearCongruence(A, B, N):
    A = A % N
    B = B % N
    u = 0
    v = 0
    d, u, v = ExtendedEuclidAlgo(A, N)
    if (B % d != 0):
        print(-1)
        return
    x0 = (u * (B // d)) % N
    if (x0 < 0):
        x0 += N
    for i in range(d):
        print((x0 + i * (N // d)) % N, end=" ")


A = 15
B = 9
N = 18
linearCongruence(A, B, N)
