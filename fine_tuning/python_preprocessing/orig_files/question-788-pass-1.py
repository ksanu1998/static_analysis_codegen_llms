class newNode:
    def __init__(self, key):
        self .data = key
        self .left = None
        self .right = None


def updatetree(root):
    if (not root):
        return 0
    if (root .left is None and root .right is None):
        return root .data
    leftsum = updatetree(root .left)
    rightsum = updatetree(root .right)
    root .data += leftsum
    return root .data + rightsum


def inorder(node):
    if (node is None):
        return
    inorder(node .left)
    print(node .data, end=" ")
    inorder(node .right)


if __name__ == '__main__':
    root = newNode(1)
    root .left = newNode(2)
    root .right = newNode(3)
    root .left .left = newNode(4)
    root .left .right = newNode(5)
    root .right .right = newNode(6)
    updatetree(root)
    print("Inorder traversal of the modified tree is")
    inorder(root)
