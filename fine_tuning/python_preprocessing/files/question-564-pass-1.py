def printString(Str1, n):
    if n == 1:
        return Str1
    else:
        for i in range(n-1):
            if Str1[i] > Str1[i+1]:
                Str1[i], Str1[i+1] = Str1[i+1], Str1[i]
        return printString(Str1, n-1)
