def reverse(s):
    stc = []
    temp = ""
    for i in range(len(s)):
        if s[i] == ' ':
        stc .append(temp)
        temp = ""
        else:
        temp = temp + s[i]
    stc .append(temp)
    while len(stc) != 0:
        temp = stc[len(stc) - 1]
        print(temp, end=" ")
        stc .pop()
    print()


s = "I Love To Code"
reverse(s)
