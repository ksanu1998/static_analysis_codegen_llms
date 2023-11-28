def isCenteredcube(N):

def isCenteredCube(N):
    # Check if N is a perfect cube
    if N == 0 or N % 2 == 0:
        return False
    # Check if N is a centered cube
    for i in range(1, int(N**0.333)):
        if N - i**3 == i**2:
            return True
    return False
