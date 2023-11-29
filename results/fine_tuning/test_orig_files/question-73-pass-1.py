from math import sqrt



def isoctagonal(N):
    a = int(sqrt(N))
    b = int(sqrt(2*N))
    if a**2 == N and b**2 == 2*N:
        return True
    else:
        return False
