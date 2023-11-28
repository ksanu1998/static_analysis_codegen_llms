def alternateFib(n):
    if (n < 0):
        return -1
    f1 = 0
    f2 = 1
    print(f1, end=" ")
    for i in range(2, n + 1):
        f3 = f2 + f1
        if (i % 2 == 0):
            print(f3, end=" ")
        f1 = f2
        f2 = f3


N = 15
alternateFib(N)
