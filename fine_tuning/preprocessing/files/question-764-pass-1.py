def removeEveryKth(l, k):
    for i in range(0, len(l), k):
        l.pop(i)
    return l
