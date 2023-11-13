import sys


class Node ():
    def __init__(self, data):self.data = data
        self.next = None


def sum_fibonacci_nodes(head):
    if head is None:
        return 0
    elif head.next is None:
        return head.data
    else:
        sum = head.data + sum_fibonacci_nodes(head.next)
        head.next = Node(sum)
        return sum


def product_fibonacci_nodes(head):
    if head is None:
        return 1
    elif head.next is None:
        return head.data
    else:
        product = head.data * product_fibonacci_nodes(head.next)
        head.next = Node(product)
        return product


def main():
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(8)

    print("Sum of Fibonacci nodes:", sum_fibonacci_nodes(head))
    print("Product of Fibonacci nodes:", product_fibonacci_nodes(head))


if __name__ == "__main__":
    main()