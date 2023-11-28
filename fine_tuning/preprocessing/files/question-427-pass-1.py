def KnapSack(val, wt, n, W):
    # Create a 2D table to store the results of subproblems
    table = [[0 for _ in range(W+1)] for _ in range(n+1)]

    # Fill the table
    for i in range(1, n+1):
        for j in range(1, W+1):
            # If the current item is not included
            table[i][j] = table[i-1][j]
            # If the current item is included
            if wt[i-1] <= j:
                table[i][j] = max(table[i-1][j-wt[i-1]] + val[i-1], table[i][j])

    # Return the maximum value in the last row
    return table[-1][-1]
