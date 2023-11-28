import math


def findLine(distance, degree):import math

def findLine(distance, degree):
    # Calculate the slope of the line
    slope = math.tan(math.radians(degree))

    # Calculate the y-intercept of the line
    y_intercept = distance / math.sqrt(1 + slope ** 2)

    # Calculate the equation of the line
    line_equation = f"y = {slope}x + {y_intercept}"

    return line_equation
