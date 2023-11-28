def divisor(a):
    c = 0
    for (i = 1; i <= a / 2; i++)
        if (a % i == 0)
            c += 1
    if (c % 2 == 0)
        return 1
    else
        return 0


if __name__ == "__main__":
    n = 10
    print(divisor(n))
