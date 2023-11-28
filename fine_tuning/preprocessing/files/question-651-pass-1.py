NO_OF_CHARS = 256


def areAnagram(str1, str2):
    if len(str1)!= len(str2):
        return False
    else:
        count = [0] * NO_OF_CHARS
        for i in range(len(str1)):
            count[ord(str1[i])] += 1
            count[ord(str2[i])] -= 1
        for i in range(NO_OF_CHARS):
            if count[i]!= 0:
                return False
        return True
