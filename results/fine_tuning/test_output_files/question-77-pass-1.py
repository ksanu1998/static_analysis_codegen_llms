def Centered_Pentagonal_num(n):
    i = 1
    sum = 0
    while (i <= n):
        sum = sum + (((3 * i - 1) * (3 * i - 1)) / 2)
        i = i + 1
    print(sum)


if __name__ == "__main__":
    Centered_Pentagonal_num(10)
