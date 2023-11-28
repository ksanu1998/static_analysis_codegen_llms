def block(x):
    v = []
    print("Blocks for %d : " % x, end="")
    while (x > 0):
        v .append(int(x % 2))
        x = int(x / 2)
    for i in range(0, len(v)):
        if (v[i] == 1):
            print(i, end="")
            if (i != len(v) - 1):
                print(", ", end="")
    print("")


block(71307)
block(1213)
block(29)
block(100)
