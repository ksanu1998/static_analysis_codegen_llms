def canTakeDown(bishopX, bishopY, pawnX, pawnY):
    # Calculate the distance between the bishop and the pawn
    distance = abs(bishopX - pawnX) + abs(bishopY - pawnY)

    # Check if the distance is equal to 3
    if distance == 3:
        return True
    else:
        return False