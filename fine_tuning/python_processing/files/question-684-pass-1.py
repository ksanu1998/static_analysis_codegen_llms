def checkRightAngled(X1, Y1, X2, Y2, X3, Y3):
    if X1 * (Y2 - Y3) + X2 * (Y3 - Y1) + X3 * (Y1 - Y2) == 0:
        return True
    else:
        return False
