def largestCharacter(str):
    uppercase = [False] * 26
    lowercase = [False] * 26
    arr = list(str)
    for c in arr:
        if (c .islower()):
            lowercase[ord(c) - ord('a')] = True
        if (c .isupper()):
            uppercase[ord(c) - ord('A')] = True
    for i in range(25, -1, -1):
        if (uppercase[i] and lowercase[i]):
            return chr(i + ord('A')) + ""
    return "-1"


str = "admeDCAB"
print(largestCharacter(str))
