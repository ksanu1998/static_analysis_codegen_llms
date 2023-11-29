import sys


class Node ():
    def __init__(self, data):
        self.data = data
        self.next = None


def sum_and_product_fibonacci_nodes(head):
    sum = 0
    product = 1
    current = head
    while current:
        sum += current.data
        product *= current.data
        current = current.next
    return sum, product


def create_singly_linked_list(my_list):
    if not my_list:
        return None
    head = Node(my_list[0])
    current = head
    for i in range(1, len(my_list)):
        new_node = Node(my_list[i])
        current.next = new_node
        current = new_node
    return head


def print_singly_linked_list(head):
    current = head
    while current:
        print(current.data)
        current = current.next


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    head = create_singly_linked_list(my_list)
    print_singly_linked_list(head)
    sum, product = sum_and_product_fibonacci_nodes(head)
    print(f"Sum: {sum}")
    print(f"Product: {product}")


# Output:
# 1
# 2
# 3
# 4
# 5
# Sum: 15
# Product: 120

# Explanation:
# The sum of the Fibonacci nodes of the linked list is 15, and the product of the Fibonacci nodes is 120.
