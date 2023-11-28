def minSum(arr, n, x):
    if (x == 0):
        return 0
    if (n == 1):
        return arr[0]
    if (n == 2):
        return (arr[0] + arr[1])
    if (n == 3):
        return (arr[0] + arr[1] + arr[2])
    if (n == 4):
        return (arr[0] + arr[1] + arr[2] + arr[3])
    if (n == 5):
        return (arr[0] + arr[1] + arr[2] + arr[3] + arr[4])
    if (n == 6):
        return (arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5])
    if (n == 7):
        return (arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6])
    if (n == 8):
        return (arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7])
    if (n == 9):
        return (arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8])
    if (n == 10):
        return (arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5] + arr[6] + arr[7] + arr[8] + arr[9])
    if (n == 11):
        return (arr[0] + arr[1]
