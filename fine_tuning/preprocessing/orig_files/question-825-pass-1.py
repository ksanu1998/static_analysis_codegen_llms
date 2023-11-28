def pairWiseConsecutive(s):
    aux = []
    while (len(s) != 0):
        aux .append(s[-1])
        s .pop()
    result = True
    while (len(aux) > 1):
        x = aux[-1]
        aux .pop()
        y = aux[-1]
        aux .pop()
        if (abs(x - y) != 1):
            result = False
        s .append(x)
        s .append(y)
    if (len(aux) == 1):
        s .append(aux[-1])
    return result


if __name__ == '__main__':
    s = []
    s .append(4)
    s .append(5)
    s .append(-2)
    s .append(-3)
    s .append(11)
    s .append(10)
    s .append(5)
    s .append(6)
    s .append(20)
    if (pairWiseConsecutive(s)):
        print("Yes")
    else:
        print("No")
    print("Stack content (from top)", "after function call")
    while (len(s) != 0):
        print(s[-1], end=" ")
        s .pop()
