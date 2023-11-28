def Centered_tridecagonal_num(n):
    if (n == 1):
        return 1
    c = 0
    for i in range(1, n):
        c += (i * (i + 1)) / 2
    print(c)


if __name__ == "__main__":
    Centered_tridecagonal_num(10)
