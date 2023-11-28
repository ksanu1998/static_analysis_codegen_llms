def findMaximumPieces(n):
    x = n // 2
    return ((x + 1) * (n - x + 1))


if __name__ == "__main__":
    n = 3
    print("Max number of pieces for n = " +
          str(n) + " is " + str(findMaximumPieces(3)))
