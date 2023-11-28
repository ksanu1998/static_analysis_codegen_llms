class newNode:
    def __init__(self, data):
        self .data = data
        self .left = None
        self .right = None


def push(head_ref, node):
    node .right = (head_ref)
    node .left = None
    if ((head_ref) is not None):
        (head_ref).left = node
    (head_ref) = node


def printList(node):
    i = 0
    while (i < len(node)):
        print(node[i].data, end=" ")
        i += 1


def spiralLevelOrder(root):
    if (root is None):
        return
    q = []
    q .append(root)
    stk = []
    level = 0
    while (len(q)):
        nodeCount = len(q)
        if (level & 1):
            while (nodeCount > 0):
                node = q[0]
                q .pop(0)
                stk .append(node)
                if (node .left is not None):
                    q .append(node .left)
                if (node .right is not None):
                    q .append(node .right)
                nodeCount -= 1
        else:
            while (nodeCount > 0):
                node = q[-1]
                q .pop(-1)
                stk .append(node)
                if (node .right is not None):
                    q .insert(0, node .right)
                if (node .left is not None):
                    q .insert(0, node .left)
                nodeCount -= 1
        level += 1
    head = []
    while (len(stk)):
        head .append(stk[0])
        stk .pop(0)
    print("Created DLL is:")
    printList(head)


if __name__ == '__main__':
    root = newNode(1)
    root .left = newNode(2)
    root .right = newNode(3)
    root .left .left = newNode(4)
    root .left .right = newNode(5)
    root .right .left = newNode(6)
    root .right .right = newNode(7)
    root .left .left .left = newNode(8)
    root .left .left .right = newNode(9)
    root .left .right .left = newNode(10)
    root .left .right .right = newNode(11)
    root .right .left .right = newNode(13)
    root .right .right .left = newNode(14)
    spiralLevelOrder(root)
