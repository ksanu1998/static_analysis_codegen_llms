import numpy as np


def maxLengthSquare(row, column, arr, k):
    sum = np .zeros((row + 1, column + 1))
    cur_max = 1
    max = 0
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            sum[i][j] = sum[i - 1][j] + sum[i][j - 1] + \
                arr[i - 1][j - 1] - sum[i - 1][j - 1]
            if (i >= cur_max and j >= cur_max and sum[i][j] - sum[i - cur_max]
                [j] - sum[i][j - cur_max] + sum[i - cur_max][j - cur_max] <= k):
                max = cur_max
                cur_max += 1
    return max


if __name__ == "__main__":
    row = 4
    column = 4
    matrix = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    k = 6
    ans = maxLengthSquare(row, column, matrix, k)
    print(ans)
