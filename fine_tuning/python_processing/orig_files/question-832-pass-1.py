class newNode:
    def __init__(self, data):
        self .data = data
        self .left = self .right = None


def IsFoldable(root):
    if (root is None):
        return True
    return IsFoldableUtil(root .left, root .right)


def IsFoldableUtil(n1, n2):
    if n1 is None and n2 is None:
        return True
    if n1 is None or n2 is None:
        return False
    d1 = IsFoldableUtil(n1 .left, n2 .right)
    d2 = IsFoldableUtil(n1 .right, n2 .left)
    return d1 and d2


if __name__ == "__main__":
    root = newNode(1)
    root .left = newNode(2)
    root .right = newNode(3)
    root .left .right = newNode(4)
    root .right .left = newNode(5)
    if IsFoldable(root):
        print("Tree is foldable")
    else:
        print("Tree is not foldable")
