class Point:
    def __init__(self, x, y):
        self .x = x
        self .y = y


def distSq(p, q):
    return (p .x - q .x) * (p .x - q .x) + (p .y - q .y) * (p .y - q .y)


def isSquare(p1, p2, p3, p4):
    if d2 == 0 or d3 == 0 or d4 == 0:
        return False
    if d2 == d3 and 2 * d2 == d4 and 2 * distSq(p2, p4) == distSq(p2, p3):
        return True
    if d3 == d4 and 2 * d3 == d2 and 2 * distSq(p3, p2) == distSq(p3, p4):
        return True
    if d2 == d4 and 2 * d2 == d3 and 2 * distSq(p2, p3) == distSq(p2, p4):
        return True
    return False


if __name__ == "__main__":
    p1 = Point(20, 10)
    p2 = Point(10, 20)
    p3 = Point(20, 20)
    p4 = Point(10, 10)
    if isSquare(p1, p2, p3, p4):
        print('Yes')
    else:
        print('No')
