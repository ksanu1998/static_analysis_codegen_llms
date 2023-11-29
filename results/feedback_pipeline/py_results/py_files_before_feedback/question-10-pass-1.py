def minSwaps(b):
    # Initialize variables
    rows, cols = len(b), len(b[0])
    swaps = 0

    # Loop through each row
    for i in range(rows):
        # Loop through each column
        for j in range(cols):
            # If the current cell is not equal to the previous cell
            if b[i][j]!= b[i][j-1]:
                # Swap the current cell with the previous cell
                b[i][j], b[i][j-1] = b[i][j-1], b[i][j]
                swaps += 1

    return swaps