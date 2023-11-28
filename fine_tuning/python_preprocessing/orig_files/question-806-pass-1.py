def findMaxLen(string):
    n = len(string)
    stk = []
    stk .append(-1)
    result = 0
    for i in xrange(n):
        if string[i] == '(':
            stk .append(i)
        else:
            if len(stk) != 0:
            stk .pop()
            if len(stk) != 0:
                result = max(result, i - stk[len(stk) - 1])
            else:
                stk .append(i)
    return result


string = "((()()"
print findMaxLen(string)
string = "()(()))))"
print findMaxLen(string)
