class node:
    def __init__(self):
        data = None
        next = None


def add(data):
    newnode = node()
    newnode .data = data
    newnode .next = None
    return newnode


def string_to_SLL(text, head):
    head = add(text[0])
    curr = head
    for i in range(len(text) - 1):
        curr .next = add(text[i + 1])
        curr = curr .next
    return head


def print_(head):
    curr = head
    while (curr is not None):
        print((curr .data), end=" - > ")
        curr = curr .next


text = "GEEKS"
head = None
head = string_to_SLL(text, head)
print_(head)
