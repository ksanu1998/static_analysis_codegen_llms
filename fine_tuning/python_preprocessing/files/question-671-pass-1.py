import math
import sys


def closest_angle(N, A):
    # Find the angle between the current vertex and the previous vertex
    angle = math.fabs(A - N)

    # If the angle is less than 180 degrees, return the current vertex
    if angle <= 180:
        return N

    # Otherwise, return the previous vertex
    return A
