def NoofTriplets(N, K):
    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i + j <= N and i * K + j * K == i * j:
                count += 1
    return count