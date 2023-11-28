def isPalindrome(Str):
    Len = len(Str)
    for i in range(Len):
        if (Str[i] != Str[Len - i - 1]):
            return False
    return True


def isCompressablePalindrome(Str):
    Len = len(Str)
    compressed = ""
    compressed += Str[0]
    for i in range(1, Len):
        if (Str[i] != Str[i - 1]):
            compressed += Str[i]
    return isPalindrome(compressed)


if __name__ == '__main__':
    Str = "abbcbbbaaa"
    if (isCompressablePalindrome(Str)):
        print("Yes")
    else:
        print("No")
