from math import sqrt


def isPentadecagon(N):
    # A pentadecagonal number is a number that can be expressed as the sum of three squares
    # For example, 10 is a pentadecagonal number because it can be expressed as 3^2 + 2^2 + 1^2
    # The formula for a pentadecagonal number is N = (n^2 + n) / 2
    # Where n is the number of sides of a regular polygon with 2n-3 vertices
    # We can use this formula to check if N is a pentadecagonal number

    # First, we need to find the value of n
    # We can do this by taking the square root of 2N and rounding up to the nearest integer
    n = int(sqrt(2 * N) + 1)

    # Now we can calculate the number of sides of the regular polygon
    # Which is 2n-3
    num_sides = 2 * n - 3

    # Now we can calculate the perimeter of the regular polygon
    # Which is n times the length of the side
    perimeter = n * num_sides

    # Now we can calculate the area of the regular polygon
    # Which is (n^2 - 1) times the length of the side squared
    area = (n ** 2 - 1) * (num_sides ** 2)

    # Now we can check if N is a pentadecagonal number
    # By checking if the perimeter and area are equal
    if perimeter == N and area == N:
        return True
    else:
        return False
