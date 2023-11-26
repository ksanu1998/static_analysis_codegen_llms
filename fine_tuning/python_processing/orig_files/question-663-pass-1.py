import math
result = []


def solveBoard(board, row, rowmask, ldmask, rdmask):
    n = len(board)
    all_rows_filled = (1 << n) - 1
    if (rowmask == all_rows_filled):
        v = []
        for i in board:
            for j in range(len(i)):
                if i[j] == 'Q':
                    v .append(j + 1)
        result .append(v)
    safe = all_rows_filled & (~(rowmask ldmask rdmask))
    while (safe > 0):
        p = safe & (-safe)
        col = (int)(math .log(p) / math .log(2))
        board[row][col] = 'Q'
        solveBoard(board, row + 1, rowmask | p, (ldmask p) << 1, (rdmask p) >> 1)
        safe = safe & (safe - 1)

    board[row][col] = ' '


def printBoard(board):
    for row in board:
        print("|" + "|".join(row) + " ")


def main():
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row .append(' ')
        board .append(row)
    rowmask = 0
    ldmask = 0
    rdmask = 0
    row = 0
    result .clear()
    solveBoard(board, row, rowmask, ldmask, rdmask)
    result .sort()
    print(result)


if __name__ == "__main__":
    main()
