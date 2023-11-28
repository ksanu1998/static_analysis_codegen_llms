import sys


def getMinimizedSum(string, length):
    maxVal = -(sys .maxsize - 1)
    sum = 0
    occurrences = [0] * 26
    for i in range(length):
        occurrences[ord(string[i]) - ord('a')] += 1
        sum += ord(string[i])
    for i in range(26):
        count = occurrences[i] * (i + ord('a'))
        maxVal = max(maxVal, count)
    return (sum - maxVal)


if __name__ == "__main__":
    string = "geeksforgeeks"
    length = len(string)
    print(getMinimizedSum(string, length))
