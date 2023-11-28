def Squares(n, m, a):
    return (((m + a - 1) // a) * ((n + a - 1) // a))


if __name__ == "__main__":
    n = 6
    m = 6
    a = 4
    print(Squares(n, m, a))
