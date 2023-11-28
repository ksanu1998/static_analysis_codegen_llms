def isReducible(Str):
    N = len(Str)
    s = []
    for i in range(N):
    if (Str[i] == '1'):
        s .append(Str[i])
    elif (len(s) > 0):
        del s[len(s) - 1]
    else:
        return False
    if (len(s) == 0):
    return True
    else:
    return False


Str = "11011000"
if (isReducible(Str)):
    print("Yes")
else:
    print("No")
