row = 5
col = 5


def isPath(arr):
    arr[0][0] = 1
    for i in range(1, row):
        if (arr[i][0] != -1):
            arr[i][0] = arr[i - 1][0]
    for j in range(1, col):
        if (arr[0][j] != -1):
            arr[0][j] = arr[0][j - 1]
    for i in range(1, row):
        for j in range(1, col):
            if (arr[i][j] != -1):
                arr[i][j] = max(arr[i][j - 1], arr[i - 1][j])
    return (arr[row - 1][col - 1] == 1)


arr = [[0, 0, 0, -1, 0], [-1, 0, 0, -1, -1],
       [0, 0, 0, -1, 0], [-1, 0, -1, 0, -1], [0, 0, -1, 0, 0]]
if (isPath(arr)):
    print("Yes")
else:
    print("No")
