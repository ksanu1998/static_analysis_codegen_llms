def getResult(st):
    result = 0
    for i in range(len(st)):
        result += int(st[i]) ** len(st)
    return result
