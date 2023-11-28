def getResult(st):
    sum = 0
    length = len(st)
    for i in st:
        sum = sum + int(i)**length
    number = int(st)
    if (number == sum):
        return "true"
    else:
        return "false"


st = "153"
print(getResult(st))
