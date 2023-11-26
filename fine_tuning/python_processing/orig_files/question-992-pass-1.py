def XorSum(A, B, N, M):
    ans1 = 0
    ans2 = 0
    for i in range(N):
        ans1 = ans1 ^ A[i]
    for i in range(M):
        ans2 = ans2 ^ B[i]
    return (ans1 & ans2)


if __name__ == '__main__':
    A = [3, 5]
    B = [2, 3]
    N = len(A)
    M = len(B)
    print(XorSum(A, B, N, M))
