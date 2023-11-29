def center_heptagonal_num(n):
    if (n == 1):
        return 1
    a = 1
    for i in range(2, n + 1):
        a = (a * 7) + 1
    print(a)


if __name__ == "__main__":
    center_heptagonal_num(10)
