class Node:
    def __init__(self, data):self.data = data
        self.left = None
        self.right = None

def get_max_xor_path(root):
    # Base case: If root is None, return 0
    if root is None:
        return 0

    # Get the maximum XOR path for the left and right subtrees
    left_max_xor = get_max_xor_path(root.left)
    right_max_xor = get_max_xor_path(root.right)

    # Calculate the maximum XOR path for the current node
    max_xor = max(left_max_xor, right_max_xor)
    max_xor = max(max_xor, root.data ^ left_max_xor)
    max_xor = max(max_xor, root.data ^ right_max_xor)

    return max_xor

# Test the get_max_xor_path function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(get_max_xor_path(root)) # Output: 7
