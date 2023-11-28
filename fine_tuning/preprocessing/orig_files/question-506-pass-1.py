def getTotCount(num):
    totCount = 1
    firstCount = 1
    temp = 1
    while (not (num & temp)):
        temp = temp << 1
        totCount += 1
    firstCount = totCount
    temp = num >> totCount
    while (temp):
        totCount += 1
        temp = temp >> 1
    return totCount, firstCount


def flipBitsFromRightMostSetBit(num):
    totbit, firstbit = getTotCount(num)
    num1 = num ^ ((1 << totbit) - 1)
    num1 = num1 ^ ((1 << firstbit) - 1)
    return num1


if __name__ == '__main__':
    n = 120
    print(flipBitsFromRightMostSetBit(n))
