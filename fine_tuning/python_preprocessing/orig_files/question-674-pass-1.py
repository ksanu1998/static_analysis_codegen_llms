def centralPoints(arr, N):
    count = 0
    for i in range(N):
        c1 = 0
        c2 = 0
        c3 = 0
        c4 = 0
        x = arr[i][0]
        y = arr[i][1]
        for j in range(N):
            if (arr[j][0] > x and arr[j][1] == y):
                c1 = 1
            if (arr[j][1] > y and arr[j][0] == x):
                c2 = 1
            if (arr[j][0] < x and arr[j][1] == y):
                c3 = 1
            if (arr[j][1] < y and arr[j][0] == x):
                c4 = 1
        if (c1 + c2 + c3 + c4 == 4):
            count += 1
    return count


if __name__ == '__main__':
    arr = [[1, 0], [2, 0], [1, 1], [1, -1]]
    N = len(arr)
    print(centralPoints(arr, N))
