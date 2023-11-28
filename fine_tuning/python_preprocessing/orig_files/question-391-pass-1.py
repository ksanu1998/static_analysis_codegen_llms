DP_s = 9


def getNumStrictMonotone(ln):
    DP = [[0] * DP_s for _ in range(ln)]
    for i in range(DP_s):
        DP[0][i] = i + 1
    for i in range(1, ln):
        for j in range(1, DP_s):
            DP[i][j] = DP[i - 1][j - 1] + DP[i][j - 1]
    return DP[ln - 1][DP_s - 1]


print(getNumStrictMonotone(2))
