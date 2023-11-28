def check_isogram(string):
    length = len(string)
    mapHash = [0] * 26
    for i in range(length):
        mapHash[ord(string[i]) - ord('a')] += 1
        if (mapHash[ord(string[i]) - ord('a')] > 1):
            return False
    return True


if __name__ == "__main__":
    string = "geeks"
    string2 = "computer"
    if (check_isogram(string)):
        print("True")
    else:
        print("False")
    if (check_isogram(string2)):
        print("True")
    else:
        print("False")
