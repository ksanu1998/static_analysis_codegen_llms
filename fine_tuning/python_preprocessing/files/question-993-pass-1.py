class TreeNode:
    def __init__(self, val=0, left=None, right=None):self.val = val
        self.left = left
        self.right = right

def count_levels(root):
    if root is None:
        return 0
    queue = [root]
    level = 0
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return level

# Test case 1:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(count_levels(root)) # Output: 3

# Test case 2:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
print(count_levels(root)) # Output: 4

# Test case 3:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = Tree
