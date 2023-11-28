def checkRightAngled(X1, Y1, X2, Y2, X3, Y3):
    A = (int(pow((X2 - X1), 2)) + int(pow((Y2 - Y1), 2)))
    B = (int(pow((X3 - X2), 2)) + int(pow((Y3 - Y2), 2)))
    C = (int(pow((X3 - X1), 2)) + int(pow((Y3 - Y1), 2)))
    if ((A > 0 and B > 0 and C > 0) and (
            A == (B + C) or B == (A + C) or C == (A + B))):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    X1 = 0
    X2 = 0
    X3 = 9
    Y1 = 2
    Y2 = 14
    Y3 = 2
    checkRightAngled(X1, Y1, X2, Y2, X3, Y3)
