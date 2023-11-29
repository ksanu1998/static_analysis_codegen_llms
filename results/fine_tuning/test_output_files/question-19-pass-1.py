def findMode(a, n):
    if (n == 1):
        print("No mode")
        return
    maxCount = 1
    mode = a[0]
    for i in range(1, n):
        if (a[i] == mode):
            maxCount += 1
        else:
            if (maxCount < 2):
                mode = a[i]
                maxCount = 1
            else:
                maxCount = 1
    if (maxCount < 2):
        print("No mode")
    else:
        print(mode)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5,
