def lcs(X, Y, m, n):
    # Create a 2D array to store the largest common subsequence
    lcs_matrix = [[0 for i in range(n+1)] for j in range(m+1)]

    # Fill in the first row and first column of the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
            else:
                lcs_matrix[i][j] = max(lcs_matrix[i-1][j], lcs_matrix[i][j-1])

    # Return the last value of the matrix
    return lcs_matrix[m][n]
