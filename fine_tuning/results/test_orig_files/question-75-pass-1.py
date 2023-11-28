import math



def istetradecagonal(N):
    n = int(math.sqrt(24*N+1))
    if n*(n+1) == 24*N+1:
        return True
    else:
        return False
