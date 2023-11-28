class TreeNode:
    def __init__(self):self.value = value
        self.left = None
        self.right = None

def score_of_parentheses(s):
    # Create a tree from the input string
    root = TreeNode(None)
    current = root
    for char in s:
        if char == '(':
            current.left = TreeNode(None)
            current = current.left
        elif char == ')':
            current = current.parent
        else:
            current.value = char
    # Calculate the score of the tree
    return score_of_tree(root)

def score_of_tree(node):
    # Base case: Leaf node
    if node.left is None and node.right is None:
        return 1
    # Recursive case: Non-leaf node
    else:
        left_score = score_of_tree(node.left)
        right_score = score_of_tree(node.right)
        return 2 * left_score + right_score

# Test case 1:
s = "()"
print(score_of_parentheses(s)) # Should print 1

# Test case 2:
s = "((()))"
print(score_of_parentheses(s)) # Should print 3

# Test case 3:
s = "(()(()))"
print(score_of_parentheses(s)) # Should print 5

# Test case 4:
s = "((()(())))"
print(score_of_parentheses(s)) # Should print 7

# Test case 5:
s = "((((()))))"
print(score_of_parentheses(s)) # Should print 9

# Test case 6:
s = "((((()()()()()()()()()
