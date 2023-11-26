vowels = ['a', 'e', 'i', 'o', 'u']
mapping = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}


def isValidSequence(subList):
    for vowel in vowels:
        if vowel not in subList:
            return False
    return True


def longestSubsequence(string, subList, index):
    if index == len(string):
        if isValidSequence(subList):
            return subList
        else:
            return []
    else:
        if len(subList) == 0:
            if string[index] != 'a':
                return longestSubsequence(string, subList, index + 1)
            else:
                return longestSubsequence(string, subList +\[string[index]], index + 1)
        elif mapping[subList[-1]] == mapping[string[index]]:
            return longestSubsequence(string, subList +\[string[index]], index + 1)
        elif (mapping[subList[-1]] + 1) == mapping[string[index]]:
            sub1 = longestSubsequence(string, subList +\[string[index]], index + 1)
            sub2 = longestSubsequence(string, subList, index + 1)
            if len(sub1) > len(sub2):
                return sub1
            else:
                return sub2
        else:
            return longestSubsequence(string, subList, index + 1)


if __name__ == "__main__":
    string = "aeiaaioooauuaeiou"
    subsequence = longestSubsequence(string, [], 0)
    if len(subsequence) == 0:
        print("No subsequence possible")
    else:
        print(subsequence)
