def isSubSeqDivisible(st):
    for i in range(len(st)-7):
        if sum(int(x) for x in st[i:i+8]) % 8 == 0:
            return True
    return False
