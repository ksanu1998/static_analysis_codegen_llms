def pointsAreOnSameSideOfLine(a, b, c, x1, y1, x2, y2):
    return (sign(a, b, c) == sign(x1, y1, a, b) and sign(a, b, c) == sign(x2, y2, a, b))

def sign(a, b, c):
    return (a - c) * (b - c)
