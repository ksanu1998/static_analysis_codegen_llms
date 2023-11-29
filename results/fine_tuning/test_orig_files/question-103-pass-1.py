from math import sqrt



def check(X, K):
    if X < K or K < 1:
        return False
    if X == K:
        return True
    for i in range(2, int(sqrt(X)) + 1):
        if X % i == 0 and check(i, K - 1):
            return True
    return False
