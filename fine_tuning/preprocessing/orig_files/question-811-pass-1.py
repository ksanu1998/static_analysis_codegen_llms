MAX_CHAR = 26


def adjSign(s, i):
    if (i == 0):
        return True
    if (s[i - 1] == '-'):
        return False
    return True


def eval(s, v, add):
    stk = []
    stk .append(True)
    i = 0
    while (i < len(s)):
        if (s[i] == '+' or s[i] == '-'):
        i += 1
        continue
        if (s[i] == '('):
        if (adjSign(s, i)):
            stk .append(stk[-1])
        else:
            stk .append(not stk[-1])
        elif (s[i] == ')'):
        stk .pop()
        else:
        if (stk[-1]):
            v[ord(s[i]) - ord('a')] += (1 if add else -
                                        1)if adjSign(s, i)else (-1 if add else 1)
        else:
            v[ord(s[i]) - ord('a')] += (-1 if add else 1)if adjSign(s,
                                                                    i)else (1 if add else -1)
        i += 1


def areSame(expr1, expr2):
    v = [0 for i in range(MAX_CHAR)]
    eval(expr1, v, True)
    eval(expr2, v, False)
    for i in range(MAX_CHAR):
        if (v[i] != 0):
        return False
    return True


if __name__ == '__main__':
    expr1 = "-(a+b+c)"
    expr2 = "-a-b-c"
    if (areSame(expr1, expr2)):
        print("Yes")
    else:
        print("No")
