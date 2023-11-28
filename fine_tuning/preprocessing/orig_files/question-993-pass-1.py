class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self .val = val
        self .left = left
        self .right = right


def uniqueLevels(root):
    uniqueLevels = 0
    que = [root]
    while len(que):
        length = len(que)
        prefix_XOR = 0
        prefix_OR = 0
        flag = True
        while length:
            temp = que .pop(0)
            prefix_OR |= temp .val
            prefix_XOR ^= temp .val
            if prefix_XOR != prefix_OR:
                flag = False
            if temp .left:
                que .append(temp .left)
            if temp .right:
                que .append(temp .right)
            length -= 1
        if flag:
            uniqueLevels += 1
    print(uniqueLevels)


if __name__ == '__main__':
    root = TreeNode(5)
    root .left = TreeNode(6)
    root .right = TreeNode(9)
    root .left .left = TreeNode(1)
    root .left .right = TreeNode(4)
    root .right .right = TreeNode(7)
    uniqueLevels(root)
