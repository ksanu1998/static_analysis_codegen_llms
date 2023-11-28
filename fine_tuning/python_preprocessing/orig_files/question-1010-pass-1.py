def printMaxAfterRemoval(s):
    flag = False
    n = len(s)
    for i in range(0, n):
        if s[i] == '0' and flag == False:
            flag = True
            continue
        else:
            print(s[i], end="")


if __name__ == "__main__":
    s = "1001"
    printMaxAfterRemoval(s)
