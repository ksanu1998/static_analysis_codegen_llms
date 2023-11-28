def isTwoAlter(s):
    for i in range(len(s) - 2):
        if (s[i] != s[i + 2]):
            return False
    if (s[0] == s[1]):
        return False
    return True


if __name__ == "__main__":
    str = "ABAB"
    if (isTwoAlter(str)):
        print("Yes")
    else:
        print("No")
