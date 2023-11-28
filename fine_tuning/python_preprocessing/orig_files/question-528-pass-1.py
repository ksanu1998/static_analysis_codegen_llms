def isWordPresent(sentence, word):
    word = word .upper()
    sentence = sentence .upper()
    s = sentence .split()
    for temp in s:
        if (temp == word):
            return True
    return False


if __name__ == "__main__":
    s = "Geeks for Geeks"
    word = "geeks"
    if (isWordPresent(s, word)):
        print("Yes")
    else:
        print("No")
