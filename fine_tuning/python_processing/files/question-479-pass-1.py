def isPossible(S, R, N):import math

def isPossible(S, R, N):
    # Calculate the diameter of the circle
    diameter = 2 * R
    # Calculate the length of each side of the square
    side_length = diameter / math.sqrt(2)
    # Calculate the number of rows and columns in the square
    rows = math.ceil(N / side_length)
    cols = math.ceil(N / side_length)
    # Initialize a array to store the points
    points = [[0 for _ in range(cols)] for _ in range(rows)]
    # Fill the array with the points
    for i in range(rows):
        for j in range(cols):
            points[i][j] = (i * side_length, j * side_length)
    # Check if any point is within the circle
    for i in range(rows):
        for j in range(cols):
            if math.sqrt((points[i][j][0] - S[0]) ** 2 + (points[i][j][1] - S[1]) ** 2) <= R:
                return True
    return False
