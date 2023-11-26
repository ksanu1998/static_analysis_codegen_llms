MAX_CHAR = 26


def checkCorrectOrNot(s):
    global MAX_CHAR
    count = [0] * MAX_CHAR
    n = len(s)
    if n == 1:
        return true
    i = 0
    j = n - 1
    while i < j:
        count[ord(s[i]) - ord('a')] += 1
        count[ord(s[j]) - ord('a')] -= 1
        i += 1
        j -= 1
    for i in range(MAX_CHAR):
        if count[i] != 0:
            return False
    return True


s = "abab"
print("Yes"if checkCorrectOrNot(s)else "No")
