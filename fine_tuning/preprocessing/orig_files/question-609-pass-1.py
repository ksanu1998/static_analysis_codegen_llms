def isVowel(c):
    return (c == 'A' or c == 'E' or c == 'I' or c == 'O' or c ==
            'U' or c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u')


def pigLatin(s):
    length = len(s)
    index = -1
    for i in range(length):
        if (isVowel(s[i])):
            index = i
            break
    if (index == -1):
        return "-1"
    return s[index:] + s[0:index] + "ay"


str = pigLatin("graphic")
if (str == "-1"):
    print("No vowels found. Pig Latin not possible")
else:
    print(str)
