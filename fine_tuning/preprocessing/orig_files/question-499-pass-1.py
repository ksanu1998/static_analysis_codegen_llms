def Range_sum_query(S, Query):
    N = len(S)
    A = [0] * N
    A[0] = ord(S[0]) - ord('a') + 1
    for i in range(1, N):
        A[i] = ord(S[i]) - ord('a') + 1
        A[i] = A[i] + A[i - 1]
    for i in range(len(Query)):
        if (Query[i][0] == 1):
            print(A[Query[i][1] - 1])
        else:
            print(A[Query[i][1] - 1] - A[Query[i][0] - 2])


S = "abcd"
Query = []
Query .append([2, 4])
Query .append([1, 3])
Range_sum_query(S, Query)
