def checkprefix(A, B):
    s1 = str(A)
    s2 = str(B)
    n1 = len(s1)
    n2 = len(s2)
    if n1 < n2:
        return False
    for i in range(0, n2):
        if s1[i] != s2[i]:
            return False
    return True


if __name__ == '__main__':
    A = 12345
    B = 12
    result = checkprefix(A, B)
    if result:
        print("Yes")
    else:
        print("No")
