def findNumberOfEvenCells(n, q, size):
    # Initialize a list to store the number of even cells in each row
    num_even_cells = [0] * n

    # Loop through each query
    for i in range(q):
        # Get the row and column indices of the current query
        row1, col1 = size[i][0] - 1, size[i][1] - 1
        row2, col2 = size[i][2] - 1, size[i][3] - 1

        # Increment the number of even cells in each row that has at least one even cell
        for r in range(row1, row2 + 1):
            if r % 2 == 0:
                num_even_cells[r] += 1

    # Return the number of even cells in each row
    return num_even_cells