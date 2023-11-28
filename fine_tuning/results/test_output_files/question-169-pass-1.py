def countSetBits(n):
    c = 0
    for i in range(1, n + 1):
        c += i & 1
    print(c)


if __name__ == "__main__":
    n = 5
    countSetBits(n)
