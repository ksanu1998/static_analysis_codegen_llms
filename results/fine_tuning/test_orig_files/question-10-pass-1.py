def minSwaps(b):

def minSwaps(b):
    # Initialize the number of swaps to 0
    swaps = 0

    # Loop through the rows of the binary matrix
    for i in range(len(b)):
        # Loop through the columns of the binary matrix
        for j in range(len(b[0])):
            # If the current element is 0, continue to the next element
            if b[i][j] == 0:
                continue

            # If the current element is not 0, check if the element in the same row and column is also not 0
            if b[i][j] == b[i][j-1] and b[i][j] == b[i-1][j]:
                # If the element in the same row and column is also not 0, swap the elements
                b[i][j], b[i][j-1], b[i-1][j] = b[i][j-1], b[i][j], b[i-1][j]
                swaps += 1

    # Return the number of swaps
    return swaps
