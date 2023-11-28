def isEven(arr, n, r):
    if (n == 1):
        if (arr[0] % r == 0):
            return 1
        else:
            return 0
    if (n == 2):
        if (arr[0] % r == 0 and arr[1] % r == 0):
            return 1
        else:
            return 0
    if (n == 3):
        if (arr[0] % r == 0 and arr[1] % r == 0 and arr[2] % r == 0):
            return 1
        else:
            return 0
    if (n == 4):
        if (arr[0] % r == 0 and arr[1] % r == 0 and arr[2] % r == 0 and arr[3] % r == 0):
            return 1
        else:
            return 0
    if (n == 5):
        if (arr[0] % r == 0 and arr[1] % r == 0 and arr[2] % r == 0 and arr[3] % r == 0 and arr[4] % r == 0):
            return 1
        else:
            return 0
    if (n == 6):
        if (arr[0] % r == 0 and arr[1] % r == 0 and arr[2] % r == 0 and arr[3] % r == 0 and arr[4] % r == 0 and arr[5] % r == 0):
            return 1
        else:
            return 0
    if (n == 7):
        if (arr[0] % r == 0 and arr[1] % r == 0 and arr[2] % r == 0 and arr[3] % r == 0 and
