def reverse(s):
    # Create a empty stack
    stack = []
    # Iterate through the string
    for char in s:
        # If the character is a space, push the stack
        if char == " ":
            stack.append(char)
        # If the character is not a space, pop the stack
        else:
            stack.pop()
    # Return the reversed string
    return "".join(stack)
