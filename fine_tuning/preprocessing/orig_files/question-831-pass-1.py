from collections import deque


class Node:
    def __init__(self, key):
        self .data = key
        self .left = None
        self .right = None


def flipBinaryTree(root):
    curr = root
    next = None
    temp = None
    prev = None
    while (curr):
        next = curr .left
        curr .left = temp
        temp = curr .right
        curr .right = prev
        prev = curr
        curr = next
    return prev


def printLevelOrder(root):
    if (root is None):
        return
    q = deque()
    q .append(root)
    while (1):
        nodeCount = len(q)
        if (nodeCount == 0):
            break
        while (nodeCount > 0):
            node = q .popleft()
            print(node .data, end=" ")
            if (node .left is not None):
                q .append(node .left)
            if (node .right is not None):
                q .append(node .right)
            nodeCount -= 1
        print()


if __name__ == '__main__':
    root = Node(1)
    root .left = Node(2)
    root .right = Node(3)
    root .right .left = Node(4)
    root .right .right = Node(5)
    print("Level order traversal of given tree")
    printLevelOrder(root)
    root = flipBinaryTree(root)
    print("Levelordertraversaloftheflipped" "tree")
    printLevelOrder(root)
