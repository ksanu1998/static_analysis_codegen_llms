def checkReachability(N, X, Y):
    if (X == 0 and Y == 0):
        return "YES"
    if (N % 2 == 0):
        return "YES"
    else:
        if (X % 2 != Y % 2):
            return "NO"
        else:
            return "YES"


if __name__ == '__main__':
    N = 2
    X = 5
    Y = 4
    print(checkReachability(N, X, Y))
