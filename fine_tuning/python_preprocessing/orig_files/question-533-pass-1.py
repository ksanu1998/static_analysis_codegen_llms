def addZeros(strr, n):
    for i in range(n):
        strr = "0" + strr
    return strr


def getXOR(a, b):
    aLen = len(a)
    bLen = len(b)
    if (aLen > bLen):
        b = addZeros(b, aLen - bLen)
    elif (bLen > aLen):
        a = addZeros(a, bLen - aLen)
    lenn = max(aLen, bLen)
    res = ""
    for i in range(lenn):
        if (a[i] == b[i]):
            res += "0"
        else:
            res += "1"
    return res


a = "11001"
b = "111111"
print(getXOR(a, b))
