def possibleToReach(x, y, z):
    if (z < abs(x) + abs(y) or (z - abs(x) - abs(y)) % 2):
        print("Not Possible")
    else:
        print("Possible")


if __name__ == '__main__':
    x = 5
    y = 5
    z = 11
    possibleToReach(x, y, z)
