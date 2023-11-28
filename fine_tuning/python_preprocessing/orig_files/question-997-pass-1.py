class Node:
    def __init__(self, data):
        self .data = data
        self .left = None
        self .right = None


def Solve(root, xr, max_xor):
    xr = xr ^ root .data
    if (root .left is None and root .right is None):
        max_xor[0] = max(max_xor[0], xr)
    if root .left is not None:
        Solve(root .left, xr, max_xor)
    if root .right is not None:
        Solve(root .right, xr, max_xor)
    return


def findMaxXor(root):
    xr, max_xor = 0, [0]
    Solve(root, xr, max_xor)
    return max_xor[0]


root = Node(2)
root .left = Node(1)
root .right = Node(4)
root .left .left = Node(10)
root .left .right = Node(8)
root .right .left = Node(5)
root .right .right = Node(10)
print(findMaxXor(root))
