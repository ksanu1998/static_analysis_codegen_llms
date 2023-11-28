import numpy as np


def maxLengthSquare(row, column, arr, k):
    # Initialize the maximum length of the square submatrix
    # as 0
    max_length = 0

    # Loop through each row of the matrix
    for i in range(row):
        # Loop through each column of the matrix
        for j in range(column):
            # Initialize the sum of the elements of the square submatrix
            # as 0
            sum = 0

            # Loop through each element of the square submatrix
            for r in range(i, i + max_length + 1):
                for c in range(j, j + max_length + 1):
                    # Check if the element is out of bounds
                    if r >= row or c >= column:
                        break

                    # Add the element to the sum
                    sum += arr[r][c]

                    # Check if the sum is greater than or equal to k
                    if sum >= k:
                        # Update the maximum length of the square submatrix
                        max_length = max(max_length, r - i + 1)

    # Return the maximum length of the square submatrix
    return max_length
