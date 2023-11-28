def pointsAreOnSameSideOfLine(a, b, c, x1, y1, x2, y2):
    fx1 = a * x1 + b * y1 - c
    fx2 = a * x2 + b * y2 - c
    if ((fx1 * fx2) > 0):
        return True
    return False


a, b, c = 1, 1, 1
x1, y1 = 1, 1
x2, y2 = 2, 1
if (pointsAreOnSameSideOfLine(a, b, c, x1, y1, x2, y2)):
    print("Yes")
else:
    print("No")
