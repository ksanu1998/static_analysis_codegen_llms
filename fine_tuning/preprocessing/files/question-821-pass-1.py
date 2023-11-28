class newNode:
    def __init__(self, data):self.data = data
        self.left = None
        self.right = None

def ancestors(root, n):
    # Base case: If root is None, return an empty list
    if root is None:
        return []

    # Initialize an empty list to store the ancestors
    ancestors_list = []

    # Loop through the nodes in the tree
    while root is not None:
        # If the current node is the node we are looking for, add its parent to the list of ancestors
        if root.data == n:
            ancestors_list.append(root.data)
            root = root.parent
        # If the current node is not the node we are looking for, check its left and right subtrees
        else:
            if root.left is not None and root.left.data == n:
                ancestors_list.append(root.data)
                root = root.left
            elif root.right is not None and root.right.data == n:
                ancestors_list.append(root.data)
                root = root.right
            else:
                root = None

    # Return the list of ancestors
    return ancestors_list

# Test the function with a sample binary tree and node
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)

print(ancestors(root, 4)) # Output: [1, 2]
print(ancestors(root, 7)) # Output: [1, 3, 7]
print(ancestors(root, 1)) # Output
