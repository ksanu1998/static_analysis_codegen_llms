def printHyphen(string):
    lis = list(string .split(" "))
    string = '-'.join(lis)
    return string


string = "Text contains malayalam and level words"
print(printHyphen(string))
