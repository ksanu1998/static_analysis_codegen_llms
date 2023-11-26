def predictTheWinner(K, N):
    if K == 1:
        return True
    if N == 1:
        return False
    if K == 2:
        return N % 2 == 0
    for i in range(1, K):
        if predictTheWinner(K - i, N - i):
            return True
    return False
