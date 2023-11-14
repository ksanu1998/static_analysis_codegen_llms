from math import sqrt



def check(X, K):
    for i in range(2, int(sqrt(X)) + 1):
        if X % i == 0:
            count = 0
            while X % i == 0:
                count += 1
                X //= i
            if count == K:
                return True
    return False
