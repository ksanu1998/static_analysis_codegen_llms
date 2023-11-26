def checkIfStartsWithVowels(string):
    if (not (string[0] == 'A' or string[0] == 'a' or string[0] == 'E' or string[0] == 'e' or string[0] ==
             'I' or string[0] == 'i' or string[0] == 'O' or string[0] == 'o' or string[0] == 'U' or string[0] == 'u')):
        return 1
    else:
        return 0


def check(string):
    if (checkIfStartsWithVowels(string)):
        print("Not Accepted")
    else:
        print("Accepted")


if __name__ == "__main__":
    string = "animal"
    check(string)
    string = "zebra"
    check(string)
