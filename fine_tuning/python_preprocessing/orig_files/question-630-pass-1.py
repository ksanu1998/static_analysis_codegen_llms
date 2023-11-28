import math


def uniqueCharacters(str):
    checker = 0
    for i in range(len(str)):
        bitAtIndex = ord(str[i]) - ord('a')
        if ((bitAtIndex) > 0):
            if ((checker & ((1 << bitAtIndex))) > 0):
                return False
            checker = checker | (1 << bitAtIndex)
    return True


if __name__ == '__main__':
    input = "geekforgeeks"
    if (uniqueCharacters(input)):
        print("The String " + input + " has all unique characters")
    else:
        print("The String " + input + " has duplicate characters")
