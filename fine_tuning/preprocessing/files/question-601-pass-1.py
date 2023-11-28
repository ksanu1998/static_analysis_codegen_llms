def isVowel(ch):return ch in "aeiouAEIOU"

def isConsonant(ch):[/INST]
    return ch not in "aeiouAEIOU"

def isVowelEnding(word):[/INST]
    if len(word) == 0:
        return False
    if isVowel(word[-1]):
        return True
    return isVowelEnding(word[:-1])

def isConsonantEnding(word):[/INST]
    if len(word) == 0:
        return False
    if isConsonant(word[-1]):
        return True
    return isConsonantEnding(word[:-1])

def findSubstrings(word):[/INST]
    substrings = []
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            substring = word[i:j]
            if isVowelEnding(substring) and isConsonantEnding(substring):
                substrings.append(substring)
    return substrings

def main():[/INST]
    word = input("Enter a word: ")
    substrings = findSubstrings(word)
    print("Substrings starting with vowel and ending with consonant:", substrings)

if __name__ == "__main__":
    main()
