def checkSolution(a, b, c):
    if ((b * b) - (4 * a * c)) > 0:
        print("2 solutions")
    elif ((b * b) - (4 * a * c)) == 0:
        print("1 solution")
    else:
        print("No solutions")


if __name__ == "__main__":
    a, b, c = 2, 5, 2
    checkSolution(a, b, c)
