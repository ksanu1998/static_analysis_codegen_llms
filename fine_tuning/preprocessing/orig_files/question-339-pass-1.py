C = 5
R = 3
INT_MAX = 10000000
table = [[0 for i in range(C)]for j in range(R)]
visited = [[0 for i in range(C)]for j in range(R)]


def min(p, q, r, s):
    if (p < q):
        temp1 = p
    else:
        temp1 = q
    if (r < s):
        temp2 = r
    else:
        temp2 = s
    if (temp1 < temp2):
        return temp1
    return temp2


def Distance(arr, i, j):
    if (i >= R or j >= C or i < 0 or j < 0):
        return INT_MAX
    elif (arr[i][j] == 0):
        table[i][j] = INT_MAX
        return INT_MAX
    elif (arr[i][j] == 2):
        table[i][j] = 0
        return 0
    elif (visited[i][j]):
        return INT_MAX
    else:
        visited[i][j] = 1
        temp1 = Distance(arr, i + 1, j)
        temp2 = Distance(arr, i - 1, j)
        temp3 = Distance(arr, i, j + 1)
        temp4 = Distance(arr, i, j - 1)
        min_value = 1 + min(temp1, temp2, temp3, temp4)
        if table[i][j] > 0 and table[i][j] < INT_MAX:
            if min_value < table[i][j]:
                table[i][j] = min_value
        else:
            table[i][j] = min_value
        visited[i][j] = 0
    return table[i][j]


def minTime(arr):
    max = 0
    for i in range(R):
        for j in range(C):
            if (arr[i][j] == 1):
                Distance(arr, i, j)
    for i in range(R):
        for j in range(C):
            if (arr[i][j] == 1 and table[i][j] > max):
                max = table[i][j]
    if (max < INT_MAX):
        return max
    return -1


if __name__ == '__main__':
    arr = [[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
    print(minTime(arr))
