import math


def fitOrNotFit(R, r, x, y, rad):
    # Calculate the distance between the center of the circle and the point (x, y)
    d = math.sqrt((x - R) ** 2 + (y - R) ** 2)

    # Check if the distance is less than or equal to the radius of the smaller circle
    if d <= r:
        return True
    else:
        return False
