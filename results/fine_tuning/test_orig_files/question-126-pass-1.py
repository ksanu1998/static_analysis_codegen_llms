def findNumberOfEvenCells(n, q, size):

def findNumberOfEvenCells(n, q, size):
    # Initialize a zero matrix of size n x n
    matrix = [[0] * n for _ in range(n)]

    # Perform Q queries
    for _ in range(q):
        # Get the coordinates of the cell to update
        x, y = map(int, input().split())

        # Update the cell at the coordinates
        matrix[x][y] += 1

    # Count the number of even cells
    count = 0
    for row in matrix:
        for cell in row:
            if cell % 2 == 0:
                count += 1

    return count
