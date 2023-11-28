def isVowel(x):
    if (x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        return True
    return False


def FindSubstr1ing(str1):
    n = len(str1)
    for i in range(n):
        hash = dict()
        for j in range(i, n):
            if (isVowel(str1[j]) == False):
                break
            hash[str1[j]] = 1
            if (len(hash) == 5):
                print(str1[i:j + 1], end=" ")


str1 = "aeoibsddaeiouudb"
FindSubstr1ing(str1)
