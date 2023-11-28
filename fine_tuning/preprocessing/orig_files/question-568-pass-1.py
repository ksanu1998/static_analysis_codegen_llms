def printExpansion(str):
    for i in range(len(str) - 1, -1, -1):
        for j in range(i, len(str)):
            print(str[j], end="")


str = "geeks"
printExpansion(str)
