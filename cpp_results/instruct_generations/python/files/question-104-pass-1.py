class Node:
    def __init__(self, key):self.key = key
        self.left = None
        self.right = None

def print_coprime_paths(root):
    if root is None:
        return []
    result = []
    print_coprime_paths_helper(root, result, [])
    return result

def print_coprime_paths_helper(node, result, path):
    if node is None:
        return
    path.append(node.key)
    if node.left is None and node.right is None:
        result.append(path[:])
    print_coprime_paths_helper(node.left, result, path)
    print_coprime_paths_helper(node.right, result, path)
    path.pop()

# Test case 1:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(print_coprime_paths(root))
# Output: [[1, 2, 4], [1, 2, 5], [1, 3, 6], [1, 3, 7]]

# Test case 2:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)