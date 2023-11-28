MAX = 256


def numberofways(A, B, N, M):
    pos = [[]for _ in range(MAX)]
    for i in range(M):
        pos[ord(B[i])].append(i + 1)
    dpl = [[0] * (M + 2)for _ in range(N + 2)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i - 1] == B[j - 1]:
                dpl[i][j] = dpl[i - 1][j - 1] + 1
            else:
                dpl[i][j] = max(dpl[i - 1][j], dpl[i][j - 1])
    LCS = dpl[N][M]
    dpr = [[0] * (M + 2)for _ in range(N + 2)]
    for i in range(N, 0, -1):
        for j in range(M, 0, -1):
            if A[i - 1] == B[j - 1]:
                dpr[i][j] = dpr[i + 1][j + 1] + 1
            else:
                dpr[i][j] = max(dpr[i + 1][j], dpr[i][j + 1])
    ans = 0
    for i in range(N + 1):
        for j in range(MAX):
            for x in pos[j]:
                if dpl[i][x - 1] + dpr[i + 1][x + 1] == LCS:
                    ans += 1
                    break
    return ans


if __name__ == "__main__":
    A = "aa"
    B = "baaa"
    N = len(A)
    M = len(B)
    print(numberofways(A, B, N, M))
