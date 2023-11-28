def generate_derangement(N):
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = i
    D = [0] * (N + 1)
    for i in range(1, N + 1, 2):
        if i == N:
            D[N] = S[N - 1]
            D[N - 1] = S[N]
        else:
            D[i] = i + 1
            D[i + 1] = i
    for i in range(1, N + 1):
        print(D[i], end=" ")
    print()


if __name__ == '__main__':
    generate_derangement(10)
