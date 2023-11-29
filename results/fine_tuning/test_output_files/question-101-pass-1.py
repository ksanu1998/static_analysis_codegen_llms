def movesRequired(a, b):
    a = a % b
    if (a == 0):
        print(0)
        exit(0)
    c = 0
    while (a > 0):
        c += 1
        a -= 1
    print(c)
