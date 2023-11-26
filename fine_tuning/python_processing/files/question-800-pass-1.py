class newNode:
    def __init__(self, data):self.data = data
        self.left = None
        self.right = None

def convertToDoublyLinkedList(root):
    # Base case
    if root is None:
        return None

    # Create a doubly linked list
    head = None
    tail = None

    # Initialize current node as root
    current = root

    # Initialize previous and next nodes as null
    prev = None
    next = None

    # Loop until we reach the end of the tree
    while current is not None:
        # Check if we have a left child
        if current.left is not None:
            # If we have a left child, set the previous node
            # to the current node and the current node to the left child
            prev = current
            current = current.left
        # Check if we have a right child
        elif current.right is not None:
            # If we have a right child, set the next node
            # to the current node and the current node to the right child
            next = current
            current = current.right
        # If we don't have a left or right child, we are at a leaf node
        else:
            # If we are at a leaf node, we need to connect the previous node
            # to the current node and the current node to the next node
            if prev is not None:
                prev.right = current
            if next is not None:
                current.left = prev

            # If we are at the head of the list, set the head to the current node
            if head is None:
                head = current
            # If we are at the tail of the list, set the tail to the current node
            if tail is None:
                tail = current

            # Break out of the loop
            break

    # Return the head of the doubly
