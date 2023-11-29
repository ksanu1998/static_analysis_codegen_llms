import bisect


def printPosition(A, B, sizeOfA, sizeOfB):
    # Find the position of box which occupies the given ball
    position = bisect.bisect_left(A, B)
    return position