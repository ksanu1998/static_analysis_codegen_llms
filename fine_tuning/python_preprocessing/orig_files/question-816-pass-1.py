class Node:
    def __init__(self, key):
        self .data = key
        self .left = None
        self .right = None


def convert_expression(expression, i):
    if i >= len(expression):
        return None
    root = Node(expression[i])
    i += 1
    if (i < len(expression) and expression[i] == "?"):
        root .left = convert_expression(expression, i + 1)
    elif i < len(expression):
        root .right = convert_expression(expression, i + 1)
    return root


def print_tree(root):
    if not root:
        return
    print(root .data, end=' ')
    print_tree(root .left)
    print_tree(root .right)


if __name__ == "__main__":
    string_expression = "a?b?c:d:e"
    root_node = convert_expression(string_expression, 0)
    print_tree(root_node)
