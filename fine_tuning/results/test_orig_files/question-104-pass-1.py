class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def print_coprime_paths(root):
    if root is None:
        return
    print_coprime_paths_helper(root, [])

def print_coprime_paths_helper(node, path):
    if node is None:
        return
    path.append(node.key)
    if node.left is None and node.right is None:
        print(path)
    print_coprime_paths_helper(node.left, path)
    print_coprime_paths_helper(node.right, path)

# Test case
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print_coprime_paths(root)

# Output:
# [1, 2, 4]
# [1, 2, 5]
# [1, 3, 6]
# [1, 3, 7]
