import math


def checkcircle(r, R, r1, x1, y1):
    # Calculate the distance between the center of the inner circle and the point (x1, y1)
    d = math.sqrt((x1 - r1) ** 2 + (y1 - r1) ** 2)
    # If the distance is less than the radius of the inner circle, the point is inside the inner circle
    if d < r1:
        return True
    # Calculate the distance between the center of the outer circle and the point (x1, y1)
    d = math.sqrt((x1 - R) ** 2 + (y1 - R) ** 2)
    # If the distance is less than the radius of the outer circle, the point is inside the outer circle
    if d < R:
        return True
    # If the point is not inside either circle, return False
    return False
