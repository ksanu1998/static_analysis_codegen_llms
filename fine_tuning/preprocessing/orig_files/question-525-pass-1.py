def solve(X, Y, N, K):
    count = [0] * (N + 1)
    sol = 0
    count[0] = 0
    for i in range(1, N + 1):
        count[i] = (count[i - 1] + abs(ord(X[i - 1]) - ord(Y[i - 1])))
    j = 0
    for i in range(1, N + 1):
        while ((count[i] - count[j]) > K):
            j += 1
        sol = max(sol, i - j)
    return sol


if __name__ == '__main__':
    N = 4
    X = "abcd"
    Y = "bcde"
    K = 3
    print(solve(X, Y, N, K))
