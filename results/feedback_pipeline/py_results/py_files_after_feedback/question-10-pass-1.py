def minSwaps(b):
    rows, cols = len(b), len(b[0])
    swaps = 0

    for i in range(rows):
        for j in range(cols):
            if b[i][j]!= b[i][j-1]:
                b[i][j], b[i][j-1] = b[i][j-1], b[i][j]
                swaps += 1

    return swaps
