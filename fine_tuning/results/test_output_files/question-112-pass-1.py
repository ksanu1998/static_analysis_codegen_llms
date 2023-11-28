import sys


class Node ():
    def __init__(self, data):
        self.data = data
        self.next = None


def sumAndProduct(head):
    if (head is None):
        return
    sum = 0
    product = 1
    while (head is not None):
        sum = sum + head.data
        product = product * head.data
        head = head.next
    print(sum, product)


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    sumAndProduct(head)
