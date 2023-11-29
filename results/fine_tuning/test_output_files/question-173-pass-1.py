def findNumber(n):
    if (n == 1):
        print(1)
        return
    findNumber(n - 1)
    print(n)


if __name__ == "__main__":
    n = 3
    findNumber(n)
