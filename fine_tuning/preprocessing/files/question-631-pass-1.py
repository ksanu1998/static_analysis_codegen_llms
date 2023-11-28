def isVowel(ch):return ch in "aeiouAEIOU"

def isConsonant(ch):[/INST]
    return ch not in "aeiouAEIOU"

def alternateVowelConsonant(string):[/INST]
    result = ""
    for ch in string:
        if isVowel(ch):
            result += "X"
        else:
            result += ch
    return result

print(alternateVowelConsonant("hello"))
