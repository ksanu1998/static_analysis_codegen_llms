def getResult(n):
    if (n < 10):
        return 1
    for (i = 1; i <= 9; i++)
        if (n % i == 0):
            if (getResult(i) == 1):
                return 1
    return 0


if __name__ == "__main__":
    n = 1234
    if (getResult(n) == 1):
        print("Yes")
    else:
        print("No")
