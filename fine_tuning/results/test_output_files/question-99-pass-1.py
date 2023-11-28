def findAns(a, b, n):
    c = 0
    for i in range(0, n + 1):
        if (i % 2 == 0):
            c += (a * (i / 2) + b) / 2
        else:
            c += (a * (i / 2) + b) / 2
    c = (c + 0.5)
    print(int(c))


if __name__ == "__main__":
    a = 2
    b = 3
    n = 4
    findAns(a, b, n)
