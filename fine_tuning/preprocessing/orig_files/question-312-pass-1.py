def countSubsets(N):
    if (N <= 2):
        return N
    if (N == 3):
        return 2
    DP = [0] * (N + 1)
    DP[0] = 0
    DP[1] = 1
    DP[2] = 2
    DP[3] = 2
    for i in range(4, N + 1):
        DP[i] = DP[i - 2] + DP[i - 3]
    return DP[N]


if __name__ == '__main__':
    N = 20
    print(countSubsets(N))
