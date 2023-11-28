def simplify(Str):
    Len = len(Str)
    res = [None] * Len
    index = 0
    i = 0
    s = []
    s .append(0)
    while (i < Len):
        if (Str[i] == '+'):
            if (s[-1] == 1):
                res[index] = '-'
                index += 1
            if (s[-1] == 0):
                res[index] = '+'
                index += 1
        elif (Str[i] == '-'):
            if (s[-1] == 1):
                res[index] = '+'
                index += 1
            elif (s[-1] == 0):
                res[index] = '-'
                index += 1
        elif (Str[i] == '(' and i > 0):
            if (Str[i - 1] == '-'):
                x = 0 if (s[-1] == 1)else 1
                s .append(x)
            elif (Str[i - 1] == '+'):
                s .append(s[-1])
        elif (Str[i] == ')'):
            s .pop()
        else:
            res[index] = Str[i]
            index += 1
        i += 1
    return res


if __name__ == '__main__':
    s1 = "a-(b+c)"
    s2 = "a-(b-c-(d+e))-f"
    r1 = simplify(s1)
    for i in r1:
        if i is not None:
            print(i, end=" ")
        else:
            break
    print()
    r2 = simplify(s2)
    for i in r2:
        if i is not None:
            print(i, end=" ")
        else:
            break
