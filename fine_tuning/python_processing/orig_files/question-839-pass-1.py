def printLargest(seq, N):
    res = [0] * N
    pq = []
    for i in range(N):
        pq .append(seq[i])
    for i in range(N):
        pq .sort()
        pq .reverse()
        d = pq[0]
        del pq[0]
        if (d != seq[i] or i == N - 1):
            res[i] = d
        else:
            res[i] = pq[0]
            del pq[0]
            pq .append(d)
    if (res[N - 1] == seq[N - 1]):
        res[N - 1] = res[N - 2]
        res[N - 2] = seq[N - 1]
    print("Largest Derangement")
    for i in range(N):
        print(res[i], end=" ")


seq = [92, 3, 52, 13, 2, 31, 1]
n = len(seq)
printLargest(seq, n)
