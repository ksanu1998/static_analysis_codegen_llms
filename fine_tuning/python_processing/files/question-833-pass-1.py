def isSumProperty(node):class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_sum_property(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return node.value == 0
    if node.left is not None and node.right is not None:
        return node.value == node.left.value + node.right.value
    return False
