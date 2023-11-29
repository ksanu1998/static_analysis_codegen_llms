MAX = 100000
graph = [[]for i in range(MAX + 1)]
Prime = [True for i in range(MAX + 1)]
height = [0 for i in range(MAX + 1)]


def SieveOfEratosthenes():
    for i in range(2, MAX + 1):
        if (Prime[i] == True):
            for j in range(i * i, MAX + 1, i):
                Prime[j] = False


def findHeight(root, i):
    if (root == None):
        return 0
    if (height[i]!= 0):
        return height[i]
    height[i] = 1 + findHeight(root->left, 2 * i + 1)
    height[i] = max(height[i], 1 + findHeight(root->right, 2 * i + 2))
    return height[i]


def printNodes(root, i, h):
    if (root == None):
        return
    if (i == 0):
        print(root->data, end=" ")
    if (i < h):
        printNodes(root->left, 2 * i + 1, h)
    if (i > h):
        printNodes(root->right, 2 * i + 2, h)


def printPrimeHeightNodes(root):
    SieveOfEratosthenes()
    for i in range(1, MAX + 1):
        if (Prime[i] == True):
            findHeight(root, i)
    printNodes(root, 0, 1)


if __name__ == "__main__":
    root = newNode(1)
    root->left = newNode(2)
    root->right = newNode(3)
