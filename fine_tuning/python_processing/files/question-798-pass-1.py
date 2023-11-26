class Stack:
    def __init__(self):self.items = []

    def is_empty(self):[/INST]
        return len(self.items) == 0

    def push(self, item):[/INST]
        self.items.append(item)

    def pop(self):[/INST]
        return self.items.pop()

    def peek(self):[/INST]
        return self.items[-1] if not self.is_empty() else None

    def size(self):[/INST]
        return len(self.items)

# Test the stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size()) # 3
print(stack.is_empty()) # False
print(stack.peek()) # 3
stack.pop()
print(stack.size()) # 2
print(stack.is_empty()) # False
print(stack.peek()) # 2
stack.pop()
print(stack.size()) # 1
print(stack.is_empty()) # False
print(stack.peek()) # 1
stack.pop()
print(stack.size()) # 0
print(stack.is_empty()) # True
print(stack.peek()) # None

# Delete middle element of a stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def delete_middle(self):
        if len(self.
