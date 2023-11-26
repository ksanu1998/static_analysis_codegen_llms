def isVowel(x):
    return (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u')


def findMaxLen(s):
    maxLen = 0
    cur = 0
    if (isVowel(s[0])):
        maxLen = 1
    cur = maxLen
    for i in range(1, len(s)):
        if (isVowel(s[i])):
            if (s[i] != s[i - 1]):
                cur += 1
            else:
                cur = 1
        else:
            cur = 0
        maxLen = max(cur, maxLen)
    return maxLen


Str = "aeoibsddaeiouudb"
print(findMaxLen(Str))
