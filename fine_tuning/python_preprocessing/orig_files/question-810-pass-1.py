def checkRedundancy(Str):
    st = []
    for ch in Str:
        if (ch == ')'):
            top = st[-1]
            st .pop()
            flag = True
            while (top != '('):
                if (top == '+' or top == '-' or top == '*' or top == '/'):
                    flag = False
                top = st[-1]
                st .pop()
            if (flag):
                return True
        else:
            st .append(ch)
    return False


def findRedundant(Str):
    ans = checkRedundancy(Str)
    if (ans):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    Str = "((a+b))"
    findRedundant(Str)
    Str = "(a+(b)/c)"
    findRedundant(Str)
    Str = "(a+b*(c-d))"
    findRedundant(Str)
