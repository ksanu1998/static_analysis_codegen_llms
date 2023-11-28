def checkOrtho(x1, y1, x2, y2, x3, y3, x4, y4):
    return (x1-x3) * (y2-y4) == (x2-x4) * (y1-y3)
