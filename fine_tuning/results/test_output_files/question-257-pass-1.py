from math import ceil, floor


def sum(N, X, Y):
    if (X > Y):
        X, Y = Y, X
    if (X == 1):
        return (N * (N + 1)) // 2
    if (Y == 1):
        return (N * (N + 1)) // 2
    if (X > Y):
        N = ceil(N / X)
    else:
        N = floor(N / Y)
    return (N * (N + 1)) // 2


if __name__ == "__main__":
    N = 10
    X = 3
    Y = 4
    print(sum(N, X, Y))
