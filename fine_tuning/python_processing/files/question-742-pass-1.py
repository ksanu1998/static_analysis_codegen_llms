def findIfPossible(N, S, X):
    if N == 1:
        return S == X
    for i in range(1, N):
        if findIfPossible(i, S - i, X - i):
            return True
    return False
