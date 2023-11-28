class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def printCoprime(root):
    if (root == None):
        return
    printCoprime(root.left)
    printCoprime(root.right)
    if (root.left == None and root.right == None):
        print(root.data, end=" ")


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    printCoprime(root)
