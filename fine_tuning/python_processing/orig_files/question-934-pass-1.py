import math


def multiple(a, b, x):
    if (b < 0):
        if (a == 1 and x == 1):
            print("1")
        else:
            print("0")
    mul = int(pow(a, b))
    ans = int(mul / x)
    ans1 = x * ans
    ans2 = x * (ans + 1)
    if ((mul - ans1) <= (ans2 - mul)):
        print(ans1)
    else:
        print(ans2)


a = 349
b = 1
x = 4
multiple(a, b, x)
