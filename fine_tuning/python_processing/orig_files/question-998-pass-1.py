def constructXORArray(A, n, K):
    B = [0] * n
    for i in range(n):
        B[i] = A[i] ^ K
    for i in range(n):
        print(B[i], end=" ")
    print()


if __name__ == '__main__':
    A = [2, 4, 1, 3, 5]
    K = 5
    n = len(A)
    constructXORArray(A, n, K)
    B = [4, 75, 45, 42]
    K = 2
    n = len(B)
    constructXORArray(B, n, K)
