class node:
    def __init__(self):self.data = None
        self.next = None

def string_to_linked_list(input_string):
    # Create a sentinel node
    head = node()
    current = head

    # Iterate through the input string and create a new node for each character
    for char in input_string:
        new_node = node()
        new_node.data = char
        current.next = new_node
        current = new_node

    # Return the head node of the linked list
    return head.next

# Test the function
input_string = "hello"
linked_list = string_to_linked_list(input_string)
print(linked_list.data) # Should print 'h'
print(linked_list.next.data) # Should print 'e'
print(linked_list.next.next.data) # Should print 'l'
print(linked_list.next.next.next.data) # Should print 'l'
print(linked_list.next.next.next.next.data) # Should print 'o'
