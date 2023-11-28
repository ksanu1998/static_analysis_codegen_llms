def isVowel(ch):
    if ch in ['i', 'a', 'e', 'o', 'u']:
        return True
    else:
        return False


def isSatisfied(st, n):
    for i in range(1, n):
        if (isVowel(st[i]) == False and isVowel(st[i - 1]) == False):
            return False
    for i in range(1, n - 1):
        if (isVowel(st[i]) and isVowel(st[i - 1]) ==
                False and isVowel(st[i + 1]) == False):
            return False
    return True


st = "acaba"
n = len(st)
if (isSatisfied(st, n)):
    print("Yes")
else:
    print("No")
