N = 3


def maxPathSum(tri):
    ans = 0
    for i in range(N - 2, -1, -1):
        for j in range(0, N - i):
            if (j - 1 >= 0):
                tri[i][j] += max(tri[i + 1][j], tri[i + 1][j - 1])
            else:
                tri[i][j] += tri[i + 1][j]
            ans = max(ans, tri[i][j])
    return ans


tri = [[1, 5, 3], [4, 8, 0], [1, 0, 0]]
print(maxPathSum(tri))
