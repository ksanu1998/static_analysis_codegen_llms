class newNode:
    def __init__(self, data):
        self .data = data
        self .left = None
        self .right = None


def mirror(root):
    if (root is None):
        return
    q = []
    q .append(root)
    while (len(q)):
        curr = q[0]
        q .pop(0)
        curr .left, curr .right = curr .right, curr .left
        if (curr .left):
            q .append(curr .left)
        if (curr .right):
            q .append(curr .right)


def inOrder(node):
    if (node is None):
        return
    inOrder(node .left)
    print(node .data, end=" ")
    inOrder(node .right)


root = newNode(1)
root .left = newNode(2)
root .right = newNode(3)
root .left .left = newNode(4)
root .left .right = newNode(5)
print("Inorder traversal of the constructed tree is")
inOrder(root)
mirror(root)
print("Inordertraversalofthemirrortreeis")
inOrder(root)
