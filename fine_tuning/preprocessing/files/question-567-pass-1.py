vowels = ['a', 'e', 'i', 'o', 'u']
mapping = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}


def isValidSequence(subList):
    if len(subList) == 0:
        return False
    for i in range(len(subList) - 1):
        if mapping[subList[i]] >= mapping[subList[i + 1]]:
            return False
    return True
