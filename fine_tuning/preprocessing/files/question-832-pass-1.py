class newNode:
    def __init__(self, data):self.data = data
        self.left = None
        self.right = None

# Function to check if a binary tree is foldable or not
def isFoldable(root):
    # Check if the tree is empty
    if root is None:
        return False

    # Check if the tree has only one node
    if root.left is None and root.right is None:
        return False

    # Check if the tree has two children
    if root.left is None or root.right is None:
        return False

    # Check if the tree is foldable by comparing the height of the left and right subtrees
    if height(root.left) == height(root.right):
        return True
    else:
        return False

# Function to find the height of a binary tree
def height(root):
    if root is None:
        return 0
    else:
        return max(height(root.left), height(root.right)) + 1

# Test the function
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)

print(isFoldable(root)) # Should print True

root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)

print(isFoldable(root)) # Should print False

root.left.left = None
root.left.right = None
root.right.left = None
root.right.right = None

print(isFoldable(root)) # Should print True

root.left = None
root.right = None

print(isFoldable(root)) # Should print False
