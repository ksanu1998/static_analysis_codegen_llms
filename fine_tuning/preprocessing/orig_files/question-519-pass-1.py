def IsLexicographicallySmaller(A, B):
    if (A < B):
        return True
    temp = A
    temp = ''.join(sorted(temp))
    index = -1
    for i in range(len(A)):
        if (A[i] != temp[i]):
            index = i
            break
    if (index == -1):
        return False
    j = 0
    for i in range(len(A)):
        if (A[i] == temp[index]):
            j = i
    A = list(A)
    A[index], A[j] = A[j], A[index]
    A = ''.join(A)
    if (A < B):
        return True
    else:
        return False


A = "AGAIN"
B = "ACTION"
if (IsLexicographicallySmaller(A, B)):
    print("Yes")
else:
    print("No")
