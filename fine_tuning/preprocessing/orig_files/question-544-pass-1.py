def IsRedundantBraces(A):
    a, b = 0, 0
    for i in range(len(A)):
        if (A[i] == '(' and A[i + 2] == ')'):
            return True
        if (A[i] == '*' or A[i] == '+' or A[i] == '-' or A[i] == '/'):
            a += 1
        if (A[i] == '('):
            b += 1
    if (b > a):
        return True
    return False


if __name__ == '__main__':
    A = "(((a+b) + c) + d)"
    if (IsRedundantBraces(A)):
        print("YES")
    else:
        print("NO")
