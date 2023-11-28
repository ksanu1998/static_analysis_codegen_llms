def printString(Str1, n):
    ones = 0
    for i in range(n):
        if (Str1[i] == '1'):
            ones += 1
    used = False
    for i in range(n):
        if (Str1[i] == '2' and used == False):
            used = 1
            for j in range(ones):
                print("1", end="")
        if (Str1[i] != '1'):
            print(Str1[i], end="")
    if (used == False):
        for j in range(ones):
            print("1", end="")


Str1 = "100210"
n = len(Str1)
printString(Str1, n)
