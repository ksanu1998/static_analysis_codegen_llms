class TreeNode:
    def __init__(self):
        self .parent = None
        self .children = []

    def addChild(self, node):
        self .children .append(node)

    def setParent(self, node):
        self .parent = node

    def getParent(self):
        return self .parent

    def computeScore(self):
        if (len(self .children) == 0):
            return 1
        res = 0
        for curr in self .children:
            res += curr .computeScore()
        if (self .parent is None):
            return res
        else:
            return 2 * res


def computeTree(s):
    current = TreeNode()
    root = current
    for i in range(len(s)):
        if (s[i] == '('):
            child = TreeNode()
            child .setParent(current)
            current .addChild(child)
            current = child
        else:
            current = current .getParent()
    return root


if __name__ == '__main__':
    s = "(()(()))"
    root = computeTree(s)
    print(root .computeScore())
