def isWordPresent(sentence, word):
    s = sentence .split(" ")
    for i in s:
        if (i == word):
            return True
    return False


s = "Geeks for Geeks"
word = "Geeks"
if (isWordPresent(s, word)):
    print("Yes")
else:
    print("No")
