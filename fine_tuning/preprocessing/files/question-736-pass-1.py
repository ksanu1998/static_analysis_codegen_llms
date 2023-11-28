class Point:
    def __init__(self, x, y):self.x = x
        self.y = y

def is_square(p1, p2, p3, p4):
    # Check if the four points are collinear
    if not is_collinear(p1, p2, p3, p4):
        return False

    # Check if the four points are consecutive
    if not is_consecutive(p1, p2, p3, p4):
        return False

    # Check if the four points are in a rectangle
    if not is_rectangle(p1, p2, p3, p4):
        return False

    return True

def is_collinear(p1, p2, p3, p4):
    # Check if the four points are collinear
    if (p2.x - p1.x) * (p3.y - p1.y) == (p3.x - p1.x) * (p2.y - p1.y):
        return True
    else:
        return False

def is_consecutive(p1, p2, p3, p4):
    # Check if the four points are consecutive
    if (p2.x - p1.x) == (p3.x - p2.x) and (p2.y - p1.y) == (p3.y - p2.y):
        return True
    else:
        return False

def is_rectangle(p1, p2, p3, p4):
    # Check if the four points are in a rectangle
    if (p2.x - p1.x) == (p3.x - p2.x) and (p3.x - p4.x) == (p2.x - p3.x) and (p2.y - p1
