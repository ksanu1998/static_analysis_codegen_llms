def hasEqualBlockFrequency(N):
    S = bin(N).replace("0b", "")
    p = set()
    c = 1
    for i in range(len(S) - 1):
        if (S[i] == S[i + 1]):
            c += 1
        else:
            p .add(c)
            c = 1
        p .add(c)
    if (len(p) == 1):
        print("Yes")
    else:
        print("No")


N = 5
hasEqualBlockFrequency(N)
