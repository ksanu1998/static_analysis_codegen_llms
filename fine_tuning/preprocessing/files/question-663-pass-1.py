import math
result = []


def solveBoard(board, row, rowmask, ldmask, rdmask):# Base case: if the board is completely filled, return the board
    if row == 8:
        result.append(board)
        return

    # Recursive case: try all possible values for the current row
    for i in range(1, 10):
        # Check if the current value is valid
        if (rowmask & (1 << i)) or (ldmask & (1 << i)) or (rdmask & (1 << i)):
            continue

        # Make the current move
        board[row] = i

        # Update the masks for the next row
        rowmask |= (1 << i)
        ldmask |= ((1 << i) << (row - i + 1))
        rdmask |= ((1 << i) >> (row - i + 1))

        # Recursively solve the next row
        solveBoard(board, row + 1, rowmask, ldmask, rdmask)

        # Undo the current move
        board[row] = 0
        rowmask &= ~(1 << i)
        ldmask &= ~((1 << i) << (row - i + 1))
        rdmask &= ~((1 << i) >> (row - i + 1))
[PYTHON]
# Driver code
board = [0] * 9
solveBoard(board, 0, 0, 0, 0)
print(result)
