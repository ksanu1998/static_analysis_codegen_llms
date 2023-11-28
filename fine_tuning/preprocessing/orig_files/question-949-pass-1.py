def makeOdd(n):
    if (n % 2 != 0):
        return 1
    resul = 1
    while (n % 2 == 0):
        n = n / 2
        resul = resul * 2
    return resul


n = 36
print(makeOdd(n))
