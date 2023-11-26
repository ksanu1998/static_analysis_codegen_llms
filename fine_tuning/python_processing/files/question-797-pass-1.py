class newNode:
    def __init__(self, data):self.data = data
        self.left = None
        self.right = None

def mirrorTree(root):
    if root is None:
        return None

    # Create a new node with the same data as the root
    newRoot = newNode(root.data)

    # Recursively mirror the left subtree
    newRoot.left = mirrorTree(root.right)

    # Recursively mirror the right subtree
    newRoot.right = mirrorTree(root.left)

    return newRoot

# Driver code
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)

# Mirror the tree
mirroredTree = mirrorTree(root)

# Print the mirrored tree
printMirroredTree(mirroredTree)

# Print the original tree
printOriginalTree(root)

# Function to print the mirrored tree
def printMirroredTree(root):
    if root is None:
        return
    print(root.data)
    printMirroredTree(root.left)
    printMirroredTree(root.right)

# Function to print the original tree
def printOriginalTree(root):
    if root is None:
        return
    print(root.data)
    printOriginalTree(root.left)
    printOriginalTree(root.right)
