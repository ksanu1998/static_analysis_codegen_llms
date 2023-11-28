class newNode:
    def __init__(self, data):self.data = data
        self.left = None
        self.right = None

def mirrorTree(root):
    if root is None:
        return None
    else:
        temp = root.left
        root.left = root.right
        root.right = temp
        mirrorTree(root.left)
        mirrorTree(root.right)
    return root

# Test the mirrorTree function
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)

print("Original Tree:")
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)
print(root.right.left.data)
print(root.right.right.data)

mirrorTree(root)

print("\nMirror Tree:")
print(root.data)
print(root.left.data)
print(root.right.data)
print(root.left.left.data)
print(root.left.right.data)
print(root.right.left.data)
print(root.right.right.data)
