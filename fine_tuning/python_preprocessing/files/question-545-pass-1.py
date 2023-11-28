def balancedBrackets(Str):
    stack = []
    for char in Str:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0
