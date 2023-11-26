ALPHABET_SIZE = 26


class trieNode:
    def __init__(self):
        self .t = [None for i in range(ALPHABET_SIZE)]
        self .isEnd = 0


def getNode():
    temp = trieNode()
    return temp


def insert(root, key):
    trail = None
    trail = root
    for i in range(len(key)):
        if (trail .t[ord(key[i]) - ord('a')] is None):
            temp = None
            temp = getNode()
            trail .t[ord(key[i]) - ord('a')] = temp
        trail = trail .t[ord(key[i]) - ord('a')]
    (trail .isEnd) += 1


def search_mod(root, word):
    trail = root
    for i in range(len(word)):
        if (trail .t[ord(word[i]) - ord('a')] is None):
            return False
        trail = trail .t[ord(word[i]) - ord('a')]
    if ((trail .isEnd) > 0 and trail is not None):
        (trail .isEnd) -= 1
        return True
    else:
        return False


def checkPossibility(sentence, m, root):
    flag = 1
    for i in range(m):
        if (search_mod(root, sentence[i]) == False):
            print('NO', end='')
            return
    print('YES')


def insertToTrie(dictionary, n, root):
    for i in range(n):
        insert(root, dictionary[i])


if __name__ == '__main__':
    root = getNode()
    dictionary = [
        "find",
        "a",
        "geeks",
        "all",
        "for",
        "on",
        "geeks",
        "answers",
        "inter"]
    N = len(dictionary)
    insertToTrie(dictionary, N, root)
    sentence = ["find", "all", "answers", "on", "geeks", "for", "geeks"]
    M = len(sentence)
    checkPossibility(sentence, M, root)
