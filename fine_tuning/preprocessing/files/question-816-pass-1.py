class Node:
    def __init__(self, key):self.key = key
        self.left = None
        self.right = None

def convert_ternary_to_binary(ternary_expression):
    # Convert the ternary expression to a binary tree
    root = Node(ternary_expression[0])
    stack = [root]
    for i in range(1, len(ternary_expression)):
        node = Node(ternary_expression[i])
        if ternary_expression[i - 1] == "?":
            stack[-1].left = node
        else:
            stack[-1].right = node
        stack.append(node)
    return root

ternary_expression = ["A", "?", "B", ":", "C", "?", "D", ":", "E"]
root = convert_ternary_to_binary(ternary_expression)
print(root.key) # A
print(root.left.key) # B
print(root.right.key) # C
print(root.left.left.key) # D
print(root.left.right.key) # E
