def countSquares(row, column):
    if (row == 0 and column == 0):
        return 1
    if (row < 0 or column < 0):
        return 0
    if (row == 0):
        return column
    if (column == 0):
        return row
    return (countSquares(row - 1, column - 1) +
            countSquares(row - 1, column) +
            countSquares(row, column - 1) +
            countSquares(row, column))


if __name__ == "__main__":
    row = 3
    column = 3
    print(countSquares(row, column))
