MAX = 26


def canBeMadeEqual(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if (len1 == len2):
        freq = [0 for i in range(MAX)]
        for i in range(len1):
            freq[ord(str1[i]) - ord('a')] += 1
        for i in range(len2):
            if (freq[ord(str2[i]) - ord('a')] > 0):
                return True
    return False


str1 = "abc"
str2 = "defa"
if (canBeMadeEqual(str1, str2)):
    print("Yes")
else:
    print("No")
