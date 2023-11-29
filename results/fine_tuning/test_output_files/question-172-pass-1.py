def NoofTriplets(N, K):
    ans = 0
    for i in range(1, N):
        for j in range(1, N):
            if (i * K) % j == 0:
                ans += 1
    print(ans)
