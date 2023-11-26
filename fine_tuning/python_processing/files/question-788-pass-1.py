class newNode:
    def __init__(self, key):self.left = None
        self.right = None
        self.sum = 0
        self.key = key

def update_sum(root):
    if root is None:
        return
    root.sum = root.key
    if root.left is not None:
        root.sum += root.left.sum
    if root.right is not None:
        root.sum += root.right.sum
    update_sum(root.left)
    update_sum(root.right)

def get_sum(root):
    if root is None:
        return 0
    return root.sum

# Test case 1:
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
update_sum(root)
print(get_sum(root)) # Should print 28

# Test case 2:
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.left.left.left = newNode(8)
root.left.left.right = newNode(9)
update_sum(root)
print(get_sum(root)) # Should print 45

# Test case 3:
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
