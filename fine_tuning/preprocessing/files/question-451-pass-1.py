def possibleToReach(x, y, z):
    if x == y and x == 0:
        return True
    if x!= y and z == 0:
        return False
    if x > y:
        return possibleToReach(x-1, y, z-1)
    else:
        return possibleToReach(x, y-1, z-1)
