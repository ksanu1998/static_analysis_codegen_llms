def isSumProperty(node):
    left_data = 0
    right_data = 0
    if (node is None or (node .left is None and node .right is None)):
        return 1
    else:
        if (node .left is not None):
            left_data = node .left .data
        if (node .right is not None):
            right_data = node .right .data
        if ((node .data == left_data + right_data)
                and isSumProperty(node .left) and isSumProperty(node .right)):
            return 1
        else:
            return 0


class newNode:
    def __init__(self, data):
        self .data = data
        self .left = None
        self .right = None


if __name__ == '__main__':
    root = newNode(10)
    root .left = newNode(8)
    root .right = newNode(2)
    root .left .left = newNode(3)
    root .left .right = newNode(5)
    root .right .right = newNode(2)
    if (isSumProperty(root)):
        print("The given tree satisfies the", "children sum property ")
    else:
        print("The given tree does not satisfy", "the children sum property ")
