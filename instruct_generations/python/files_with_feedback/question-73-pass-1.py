from math import sqrt



def isoctagonal(N):
    # Check if N is a perfect square
    if int(sqrt(N)) ** 2 == N:
        # Check if the number of sides of the polygon is 8
        if len(str(N)) == 8:
            return True
    return False
