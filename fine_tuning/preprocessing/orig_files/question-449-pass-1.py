def sum(n):
    return n * (n - 1) // 2


def BSpattern(N):
    Val = 0
    Pthree = 0,
    cnt = 0
    initial = -1
    s = "**"
    for i in range(N):
        cnt = 0
        if (i > 0):
            print(s, end="")
            s += "**"
        for j in range(i, N):
            if (i > 0):
                cnt += 1
            Val += 1
            print(Val, end="")
            print(0, end="")
        if (i == 0):
            Sumbeforelast = sum(Val) * 2
            Pthree = Val + Sumbeforelast + 1
            initial = Pthree
        initial = initial - cnt
        Pthree = initial
        for k in range(i, N):
            print(Pthree, end="")
            Pthree += 1
            if (k != N - 1):
                print(0, end="")
        print()


N = 5
BSpattern(N)
