def center_octadecagon_num(n):
    if (n == 1):
        return 1
    a = 1
    b = 1
    c = 1
    sum = 0
    for i in range(2, n):
        a = a + 2
        b = b + 2
        c = c + 2
        sum = sum + a + b + c
    print(sum)


if __name__ == "__main__":
    center_octadecagon_num(10)
