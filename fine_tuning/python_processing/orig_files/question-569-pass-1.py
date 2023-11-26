def constructBinString(a, b, x):
    d = x // 2
    if x % 2 == 0 and x // 2 != a:
        d -= 1
        print("0", end="")
        a -= 1
    for i in range(d):
        print("10", end="")
    a = a - d
    b = b - d
    for i in range(b):
        print("1", end="")
    for i in range(a):
        print("0", end="")


if __name__ == "__main__":
    a, b, x = 4, 3, 2
    constructBinString(a, b, x)
