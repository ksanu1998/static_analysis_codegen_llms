def areVowelsInOrder(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(vowels) - 1):
        if s.count(vowels[i]) > s.count(vowels[i + 1]):
            return False
    return True
