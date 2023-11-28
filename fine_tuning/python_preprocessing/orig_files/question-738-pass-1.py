def maxPlanes(A, B, N):
    St = set()
    for i in range(N):
        t = 1 if (A[i] % B[i] > 0)else 0
        t += (A[i] // B[i]) + t
        St .add(t)
    return len(St)


A = [1, 3, 5, 4, 8]
B = [1, 2, 2, 1, 2]
N = len(A)
print(maxPlanes(A, B, N))
