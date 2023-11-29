def Icosagonal_num(n):
    if (n == 1):
        return 1
    i = 1
    sum = 0
    while (i <= n):
        sum = sum + i
        i = i + 1
    return sum


if __name__ == "__main__":
    n = 5
    print(Icosagonal_num(n))
