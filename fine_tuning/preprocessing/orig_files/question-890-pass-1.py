import math
pwr = [0] * 10


def isMunchhausen(n):
    sm = 0
    temp = n
    while (temp):
        sm = sm + pwr[(temp % 10)]
        temp = temp // 10
    return (sm == n)


def printMunchhausenNumbers(n):
    for i in range(0, 10):
        pwr[i] = math .pow((float)(i), (float)(i))
    for i in range(1, n + 1):
        if (isMunchhausen(i)):
            print(i)


n = 10000
printMunchhausenNumbers(n)
