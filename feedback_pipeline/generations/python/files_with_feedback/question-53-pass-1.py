def isPossible(A, B):
    if A == B:
        return True
    if A < B:
        return False
    for i in range(2, B):
        if A % i == 0 and B % i == 0:
            return True
    return False
