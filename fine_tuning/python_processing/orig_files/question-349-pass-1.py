import sys


def MinOfCubedDP(k):
    DP = [0] * (k + 1)
    j = 1
    t = 1
    DP[0] = 0
    for i in range(1, k + 1):
        DP[i] = sys .maxsize
        while (j <= i):
            if (j == i):
                DP[i] = 1
            elif (DP[i] > DP[i - j]):
                DP[i] = DP[i - j] + 1
            t += 1
            j = t * t * t
        t = j = 1
    return DP[k]


num = 15
print(MinOfCubedDP(num))
