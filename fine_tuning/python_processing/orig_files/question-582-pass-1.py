def areVowelsInOrder(s):
    n = len(s)
    c = chr(64)
    for i in range(0, n):
        if (s[i] == 'a' or s[i] == 'e' or s[i] ==
                'i' or s[i] == 'o' or s[i] == 'u'):
            if s[i] < c:
                return False
            else:
                c = s[i]
    return True


if __name__ == "__main__":
    s = "aabbbddeecc"
    if areVowelsInOrder(s):
        print("Yes")
    else:
        print("No")
