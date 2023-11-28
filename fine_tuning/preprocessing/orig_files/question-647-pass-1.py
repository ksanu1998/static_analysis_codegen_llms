def isPalin(str, st, end):
    while (st < end):
        if (str[st] != str[end]):
            return False
        st += 1
        end - -1
    return True


def findMinInsert(str, n):
    for i in range(n - 1, -1, -1):
        if (isPalin(str, 0, i)):
            return (n - i - 1)


Input = "JAVA"
print(findMinInsert(Input, len(Input)))
