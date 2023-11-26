class newNode:
    def __init__(self, key):
        self .data = key
        self .left = None
        self .right = None


def convertTree(root):
    if (root is None):
        return
    convertTree(root .left)
    convertTree(root .right)
    if (root .left is not None and root .right is not None):
        root .data = ((root .left .data) & (root .right .data))


def printInorder(root):
    if (root is None):
        return
    printInorder(root .left)
    print(root .data, end=" ")
    printInorder(root .right)


if __name__ == '__main__':
    root = newNode(0)
    root .left = newNode(1)
    root .right = newNode(0)
    root .left .left = newNode(0)
    root .left .right = newNode(1)
    root .right .left = newNode(1)
    root .right .right = newNode(1)
    print("Inorder traversal before conversion", end=" ")
    printInorder(root)
    convertTree(root)
    print("Inordertraversalafterconversion",  end  = "")
    printInorder(root)
