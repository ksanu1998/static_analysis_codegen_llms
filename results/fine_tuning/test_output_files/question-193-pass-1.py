def CntDivbyX(arr, n, x):
    cnt = 0
    for i in range(n):
        if (arr[i] % x == 0):
            cnt += 1
    return cnt


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    n = len(arr)
    x = 3
    print(CntDivbyX(arr, n, x))
