def NoofTriplets(N, K):

def NoofTriplets(N, K):
    count = 0
    for i in range(1, N):
        for j in range(i + 1, N):
            if (i + j) % K == 0:
                count += 1
    return count
