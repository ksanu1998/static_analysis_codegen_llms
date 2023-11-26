ALPHABET_SIZE = 26


class trieNode:
    def __init__(self):self.children = [None] * ALPHABET_SIZE
        self.is_word = False


class Trie:
    def __init__(self):[/INST]
        self.root = trieNode()

    def insert(self, word):[/INST]
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = trieNode()
            curr = curr.children[index]
        curr.is_word = True


def canForm(words, dictionary):[/INST]
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    for word in words:
        if not trie.search(word):
            return False
    return True


def main():[/INST]
    dictionary = ["apple", "banana", "cat", "dog"]
    words = ["apple", "banana", "dog"]
    print(canForm(words, dictionary))


if __name__ == "__main__":
    main()
