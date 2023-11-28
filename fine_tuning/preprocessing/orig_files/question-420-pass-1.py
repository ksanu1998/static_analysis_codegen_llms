N = 8
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def inside(x, y):
    return (x >= 0 and x < N and y >= 0 and y < N)


def findProb(start_x, start_y, steps):
    dp1 = [[[0 for i in range(N + 5)]for j in range(N + 5)]
           for k in range(steps + 5)]
    for i in range(N):
        for j in range(N):
            dp1[i][j][0] = 1
    for s in range(1, steps + 1):
        for x in range(N):
            for y in range(N):
                prob = 0.0
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (inside(nx, ny)):
                        prob += dp1[nx][ny][s - 1] / 8.0
                dp1[x][y][s] = prob
    return dp1[start_x][start_y][steps]


K = 3
print(findProb(0, 0, K))
