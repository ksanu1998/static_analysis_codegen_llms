N = 3
M = 3


def check(a, b):
    # Initialize a flag to indicate whether the conversion is possible
    possible = True

    # Loop through each submatrix of size N x M
    for i in range(N - 1):
        for j in range(M - 1):
            # Get the current submatrix
            submatrix = a[i:i + 2, j:j + 2]

            # Check if the parity of the corner elements is the same in both submatrices
            if submatrix[0, 0] == submatrix[1, 1] and submatrix[0, 1] == submatrix[1, 0]:
                # If the parity is the same, continue to the next submatrix
                continue
            else:
                # If the parity is different, set the flag to False and break the loop
                possible = False
                break

    # Return the value of the flag
    return possible
