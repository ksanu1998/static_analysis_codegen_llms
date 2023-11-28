def matchClosing(X, start, end, open, close):
    c = 1
    i = start + 1
    while (i <= end):
        if (X[i] == open):
            c += 1
        elif (X[i] == close):
            c -= 1
        if (c == 0):
            return i
        i += 1
    return i


def matchingOpening(X, start, end, open, close):
    c = -1
    i = end - 1
    while (i >= start):
        if (X[i] == open):
            c += 1
        elif (X[i] == close):
            c -= 1
        if (c == 0):
            return i
        i -= 1
    return -1


def isBalanced(X, n):
    for i in range(n):
        if (X[i] == '('):
            j = matchClosing(X, i, n - 1, '(', ')')
        elif (X[i] == '{'):
            j = matchClosing(X, i, n - 1, '{', '}')
        elif (X[i] == '['):
            j = matchClosing(X, i, n - 1, '[', ']')
        else:
            if (X[i] == ')'):
                j = matchingOpening(X, 0, i, '(', ')')
            elif (X[i] == '}'):
                j = matchingOpening(X, 0, i, '{', '}')
            elif (X[i] == ']'):
                j = matchingOpening(X, 0, i, '[', ']')
            if (j < 0 or j >= i):
                return False
            continue
        if (j >= n or j < 0):
            return False
        start = i
        end = j
        for k in range(start + 1, end):
            if (X[k] == '('):
                x = matchClosing(X, k, end, '(', ')')
                if (not (k < x and x < end)):
                    return False
            elif (X[k] == ')'):
                x = matchingOpening(X, start, k, '(', ')')
                if (not (start < x and x < k)):
                    return False
            if (X[k] == '{'):
                x = matchClosing(X, k, end, '{', '}')
                if (not (k < x and x < end)):
                    return False
            elif (X[k] == '}'):
                x = matchingOpening(X, start, k, '{', '}')
                if (not (start < x and x < k)):
                    return False
            if (X[k] == '['):
                x = matchClosing(X, k, end, '[', ']')
                if (not (k < x and x < end)):
                    return False
            elif (X[k] == ']'):
                x = matchingOpening(X, start, k, '[', ']')
                if (not (start < x and x < k)):
                    return False
    return True


if __name__ == "__main__":
    X = "[()]()"
    n = 6
    if (isBalanced(X, n)):
        print("Yes")
    else:
        print("No")
    Y = "[[()]])"
    n = 7
    if (isBalanced(Y, n)):
        print("Yes")
    else:
        print("No")
