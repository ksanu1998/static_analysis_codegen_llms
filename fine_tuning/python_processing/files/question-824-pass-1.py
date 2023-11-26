class Node:
    def __init__(self, data):self.data = data
        self.left = None
        self.right = None

def flip_binary_tree(root):
    if root is None:
        return None

    # Flip the left child
    root.left = flip_binary_tree(root.left)

    # Flip the right child
    root.right = flip_binary_tree(root.right)

    # Return the flipped root node
    return root

# Test the flip_binary_tree function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Original tree:")
print(root)

# Flip the binary tree
flip_binary_tree(root)

print("Flipped tree:")
print(root)
