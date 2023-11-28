def checkSolution(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        return 2
    elif discriminant == 0:
        return 1
    else:
        return 0
