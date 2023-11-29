import bisect



def printPosition(A, B, sizeOfA, sizeOfB):
    # Find the position of box which occupies the given ball
    position = bisect.bisect_left(A, B)
    if position < sizeOfA and A[position] == B:
        print(f"The ball is in the {position}th box.")
    else:
        print("The ball is not in any box.")
