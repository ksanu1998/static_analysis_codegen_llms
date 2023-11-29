def canTakeDown(bishopX, bishopY, pawnX, pawnY):
    if (abs(bishopX - pawnX) == abs(bishopY - pawnY)):
        return True
    return False


if __name__ == "__main__":
    bishopX = 1
    bishopY = 1
    pawnX = 2
    pawnY = 3
    if (canTakeDown(bishopX, bishopY, pawnX, pawnY)):
        print("Yes")
    else:
        print("No")
