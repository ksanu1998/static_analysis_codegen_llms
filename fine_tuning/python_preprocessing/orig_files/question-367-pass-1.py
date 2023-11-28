N = 100
n = 3
m = 4


def maxPlus(arr):
    ans = 0
    left = [[0 for x in range(N)]for y in range(N)]
    right = [[0 for x in range(N)]for y in range(N)]
    up = [[0 for x in range(N)]for y in range(N)]
    down = [[0 for x in range(N)]for y in range(N)]
    for i in range(n):
        for j in range(m):
            left[i][j] = (max(0, (left[i][j - 1]if j else 0)) + arr[i][j])
            up[i][j] = (max(0, (up[i - 1][j]if i else 0)) + arr[i][j])
    for i in range(n):
        for j in range(m):
            right[i][j] = max(
                0, (0 if (j + 1 == m)else right[i][j + 1])) + arr[i][j]
            down[i][j] = max(
                0, (0 if (i + 1 == n)else down[i + 1][j])) + arr[i][j]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            ans = max(ans, up[i - 1][j] + down[i + 1][j] +
                      left[i][j - 1] + right[i][j + 1] + arr[i][j])
    return ans


if __name__ == "__main__":
    arr = [[1, 1, 1, 1], [-6, 1, 1, -4], [1, 1, 1, 1]]
    print(maxPlus(arr))
