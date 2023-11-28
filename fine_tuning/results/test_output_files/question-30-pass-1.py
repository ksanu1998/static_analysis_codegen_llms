def solve(X, Y):
    if (X == Y):
        return 0
    if (X > Y):
        return -1
    if (X == 1):
        return 1
    if (X % 2 == 0):
        if (Y % 2 == 0):
            return (solve(X / 2, Y / 2) + 1)
        else:
            return -1
    if (Y % 2 == 0):
        return -1
    if (X % 3 == 0):
        if (Y % 3 == 0):
            return (solve(X / 3, Y / 3) + 1)
        else:
            return -1
    if (Y % 3 == 0):
        return -1
    if (X % 5 == 0):
        if (Y % 5 == 0):
            return (solve(X / 5, Y / 5) + 1)
        else:
            return -1
    if (Y % 5 == 0):
        return -1
    return -1


if __name__ == "__main__":
    X = 10
    Y = 100
    print(solve(X, Y))
