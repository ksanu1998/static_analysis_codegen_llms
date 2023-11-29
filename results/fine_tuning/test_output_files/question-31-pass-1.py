from collections import defaultdict


def countQuadraples(N):
    d = defaultdict(int)
    for i in range(1, N):
        d[i * i] += 1
    c = 0
    for i in range(1, N):
        for j in range(i, N):
            if (d[i * i] > 0 and d[j * j] > 0):
                c += 1
    print(c)
