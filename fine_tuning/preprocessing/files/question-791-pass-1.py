def calculateSpan(A, n, ans):
    for i in range(1, n):
        if A[i] > A[i-1]:
            ans[i] = ans[i-1] + 1
        else:
            ans[i] = 1
    return ans
