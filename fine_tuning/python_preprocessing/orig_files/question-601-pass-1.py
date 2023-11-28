def isVowel(ch):
    return (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u')


def isCons(ch):
    return (ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u')


def countSpecial(str):
    lent = len(str)
    if lent == 0:
    return 0
    co = []
    vo = []
    for i in range(0, lent + 1):
        co .append(0)
    for i in range(0, lent + 1):
        vo .append(0)
    if isCons(str[lent - 1]) == 1:
        co[lent - 1] = 1
    else:
        vo[lent - 1] = 1
    for i in range(lent - 2, -1, -1):
        if isCons(str[i]) == 1:
            co[i] = co[i + 1] + 1
            vo[i] = vo[i + 1]
        else:
            co[i] = co[i + 1]
            vo[i] = vo[i + 1] + 1
    ans = 0
    for i in range(lent):
        if isVowel(str[i]):
            ans = ans + co[i + 1]
        else:
            ans = ans + vo[i + 1]
    return ans


str = "adceba"
print(countSpecial(str))
