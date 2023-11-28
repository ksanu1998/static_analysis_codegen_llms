from math import sqrt



def findAandB(N):
    for a in range(1, int(sqrt(N)) + 1):
        b = N - a
        if a * b == N:
            return (a, b)
    return None
