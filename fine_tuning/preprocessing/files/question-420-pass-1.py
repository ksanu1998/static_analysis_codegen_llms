N = 8
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def inside(x, y):
    return 0 <= x < N and 0 <= y < N
