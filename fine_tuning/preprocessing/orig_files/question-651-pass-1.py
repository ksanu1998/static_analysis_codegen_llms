NO_OF_CHARS = 256


def areAnagram(str1, str2):
    count = [0 for i in range(NO_OF_CHARS)]
    i = 0
    for i in range(len(str1)):
        count[ord(str1[i]) - ord('a')] += 1
        count[ord(str2[i]) - ord('a')] -= 1
    if (len(str1) != len(str2)):
        return False
    for i in range(NO_OF_CHARS):
        if (count[i] != 0):
            return False
    return True


str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
if (areAnagram(str1, str2)):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")
