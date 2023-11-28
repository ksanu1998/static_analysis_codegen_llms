def isVowel(ch):if ch in "aeiouAEIOU":
        return True
    else:
        return False

def hasMoreVowels(word):
    vowels = 0
    consonants = 0
    for ch in word:
        if isVowel(ch):
            vowels += 1
        else:
            consonants += 1
    return vowels >= consonants

def checkSubstrings(word):
    substrings = []
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            substrings.append(word[i:j])
    for substring in substrings:
        if not hasMoreVowels(substring):
            return False
    return True

def main():
    word = input("Enter a word: ")
    if checkSubstrings(word):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()[PYTHON]

# Check whether all the substrings have number of vowels atleast as that of consonants.
def isVowel(ch):
    if ch in "aeiouAEIOU":
        return True
    else:
        return False

def hasMoreVowels(word):
    vowels = 0
    consonants = 0
    for ch in word:
        if isVowel(ch):
            vowels += 1
        else:
            consonants += 1
    return vowels >= consonants

def checkSubstrings(word):
    substrings = []
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            substrings.append(
