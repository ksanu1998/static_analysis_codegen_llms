def findEquation(a, b, c):
    n = 3
    x = [0] * n
    x[0] = a
    x[1] = b
    x[2] = c
    x.sort()
    print("The equation is:", x[0], "x^3 +", x[1], "x^2 +", x[2], "x + 1 = 0")


if __name__ == "__main__":
    a = 1
    b = 2
    c = 3
    findEquation(a, b, c)
