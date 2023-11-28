N = 3
M = 3


def check(a, b):
    for i in range(1, N, 1):
        for j in range(1, M, 1):
            if (a[i][j] != b[i][j]):
                a[i][j] ^= 1
                a[0][0] ^= 1
                a[0][j] ^= 1
                a[i][0] ^= 1
    for i in range(N):
        for j in range(M):
            if (a[i][j] != b[i][j]):
                return False
    return True


if __name__ == '__main__':
    a = [[0, 1, 0], [0, 1, 0], [1, 0, 0]]
    b = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
    if (check(a, b)):
        print("Yes")
    else:
        print("No")
