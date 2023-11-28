def findSet(N, K):
    a = []
    for i in range(1, N + 1):
        if (i != K):
            a .append(i)
    MaxDistinct = (N - K) + (K // 2)
    a = a[::-1]
    for i in range(MaxDistinct):
        print(a[i], end=" ")


if __name__ == '__main__':
    N = 5
    K = 3
    findSet(N, K)
