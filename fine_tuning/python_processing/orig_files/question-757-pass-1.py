def maximumSubsequenceSum(A, N):
    ans = 0
    mp = {}
    for i in range(N):
        if (A[i] - i in mp):
            mp[A[i] - i] += A[i]
        else:
            mp[A[i] - i] = A[i]
        ans = max(ans, mp[A[i] - i])
    print(ans)


if __name__ == '__main__':
    A = [10, 7, 1, 9, 10, 1]
    N = len(A)
    maximumSubsequenceSum(A, N)
