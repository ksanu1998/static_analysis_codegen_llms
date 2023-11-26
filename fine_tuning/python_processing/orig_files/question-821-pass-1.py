class newNode:
    def __init__(self, data):
        self .data = data
        self .left = self .right = None


def printAncestors(root, key):
    if (root is None):
        return
    st = []
    while (1):
        while (root and root .data != key):
            st .append(root)
            root = root .left
        if (root and root .data == key):
            break
        if (st[-1].right is None):
            root = st[-1]
            st .pop()
            while (len(st) != 0 and st[-1].right == root):
                root = st[-1]
                st .pop()
        root = None if len(st) == 0 else st[-1].right
    while (len(st) != 0):
        print(st[-1].data, end=" ")
        st .pop()


if __name__ == '__main__':
    root = newNode(1)
    root .left = newNode(2)
    root .right = newNode(7)
    root .left .left = newNode(3)
    root .left .right = newNode(5)
    root .right .left = newNode(8)
    root .right .right = newNode(9)
    root .left .left .left = newNode(4)
    root .left .right .right = newNode(6)
    root .right .right .left = newNode(10)
    key = 6
    printAncestors(root, key)
