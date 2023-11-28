def createPrefixArray(n, arr, prefSize, pref):
    for i in range(prefSize):
        pref[i] = 0
    for i in range(n):
        x = arr[i] + 1000000
        pref[x] += 1
    for i in range(1, prefSize):
        pref[i] += pref[i - 1]


def pointOfIntersection(m, segments, size, pref):
    ans = 0
    for i in range(m):
        x1 = segments[i][0]
        x2 = segments[i][2]
        x1 = x1 + 1000000
        x2 = x2 + 1000000
        if (x1 != x2):
            if (x1 > x2):
                x1, x2 = x2, x1
            Occ_Till_Right = pref[x2 - 1]
            Occ_Till_Left = pref[x1]
            ans += (Occ_Till_Right - Occ_Till_Left)
    return ans


N = 4
M = 8
size = 2000000 + 2
pref = [0] * size
lines = [-5, -3, 2, 3]
segments = [[-2, 5, 5, -6], [-5, -2, -3, -5], [-2, 3, -6, 1], [-1, -3,
                                                               4, 2], [2, 5, 2, 1], [4, 5, 4, -5], [-2, -4, 5, 3], [1, 2, -2, 1]]
createPrefixArray(N, lines, size, pref)
print(pointOfIntersection(M, segments, size, pref))
