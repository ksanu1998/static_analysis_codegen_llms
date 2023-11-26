class newNode:
    def __init__(self, key):self.key = key
        self.left = None
        self.right = None

def convert_to_logical_and(root):
    if root is None:
        return None

    # Create a new node with the key of the current node
    new_node = newNode(root.key)

    # Recursively convert the left subtree
    new_node.left = convert_to_logical_and(root.left)

    # Recursively convert the right subtree
    new_node.right = convert_to_logical_and(root.right)

    return new_node

# Test the function
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)

print("Original tree:")
print(root)

new_root = convert_to_logical_and(root)

print("Logical AND tree:")
print(new_root)
