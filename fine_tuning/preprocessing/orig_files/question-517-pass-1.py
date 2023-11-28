def finalString(st):
    x, y = 0, 0
    n = len(st)
    for i in range(n):
        if (st[i] == '1'):
            x += 1
        else:
            y += 1
    if (x > y):
        left = 1
    else:
        left = 0
    length = n - 2 * min(x, y)
    for i in range(length):
        print(left, end="")


if __name__ == "__main__":
    st = "010110100100000"
    finalString(st)
