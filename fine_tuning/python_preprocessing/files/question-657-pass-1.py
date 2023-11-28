dim = 3


class Node:
    def __init__(self, data):self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):[/INST]
        self.head = None
        self.tail = None

    def append(self, data):[/INST]
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def print_list(self):[/INST]
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


# Test the code
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Construct the doubly linked list from the 2D matrix
doubly_linked_list = DoublyLinkedList()
for row in matrix:
    for element in row:
        doubly_linked_list.append(element)

# Print the doubly linked list
doubly_linked_list.print_list()
