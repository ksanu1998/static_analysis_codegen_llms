def minChocolates(A, N):
    A.sort()
    i = 0
    j = N - 1
    while (i < j):
        if (A[i] + A[j] > 2 * A[N - 1]):
            i += 1
        else:
            j -= 1
    if (i == j):
        print("Yes")
    else:
        print("No")


A = [1, 2, 3, 4, 5]
N = 5
minChocolates(A, N)
