def isVowel(c):
    c = c .lower()
    if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
        return True
    return False


def swapRepeated(string):
    for i in range(len(string) - 1):
        if ((isVowel(string[i]) and isVowel(string[i + 1]))
                or (not (isVowel(string[i])) and not (isVowel(string[i + 1])))):
            (string[i], string[i + 1]) = (string[i + 1], string[i])
    string = "".join(string)
    return string


if __name__ == "__main__":
    string = "geeksforgeeks"
    print(swapRepeated(list(string)))
