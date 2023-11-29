def findMin(arr, n):
    if (n == 1):
        return (arr[0]);
    if (n == 2):
        return (min(arr[0], arr[1]));
    if (n == 3):
        return (min(min(arr[0], arr[1]), arr[2]));
    if (n == 4):
        return (min(min(arr[0], arr[1]), min(arr[2], arr[3])));
    if (n == 5):
        return (min(min(arr[0], arr[1]), min(arr[2], arr[3]), arr[4]));
    if (n == 6):
        return (min(min(arr[0], arr[1]), min(arr[2], arr[3]),
                    min(arr[4], arr[5])));
    if (n == 7):
        return (min(min(arr[0], arr[1]), min(arr[2], arr[3]),
                    min(arr[4], arr[5]), arr[6]));
    if (n == 8):
        return (min(min(arr[0], arr[1]), min(arr[2], arr[3]),
                    min(arr[4], arr[5]), min(arr[6], arr[7])));
    if (n == 9):
        return (min(min(arr[0], arr[1]), min(arr[2], arr[3]),
                    min(arr[4], arr[5]), min(arr[6], arr[7]), arr[8]));
    if (n == 10):
        return (min(min(arr[0], arr[1]), min(arr[2], arr[3]),
                    min(arr[4], arr[5]), min
