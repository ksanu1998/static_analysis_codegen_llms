def preserveSpace(Str):
    n = len(Str)
    Str = list(Str)
    start = 0
    end = n - 1
    while (start < end):
        if (Str[start] == ' '):
            start += 1
            continue
        elif (Str[end] == ' '):
            end -= 1
            continue
        else:
            Str[start], Str[end] = (Str[end], Str[start])
            start += 1
            end -= 1
    print(''.join(Str))


Str = "internship at geeks for geeks"
preserveSpace(Str)
