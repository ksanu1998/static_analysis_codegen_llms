import math as mt


def checkSub(sub, s):
    if (sub == 0):
        print(s)
        return
    if (sub < 0):
        return
    for i in range(1, 10):
        if (sub >= i):
            checkSub(sub - i, s + str(i))


if __name__ == "__main__":
    checkSub(mt.floor(8 / 2), "")
