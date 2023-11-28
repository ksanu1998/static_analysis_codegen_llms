def findDuplicateparenthesis(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return True
            stack.pop()
    return bool(stack)
