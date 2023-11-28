def sortStack(input):
    stack = []
    while input:
        top = input.pop()
        while stack and stack[-1] < top:
            input.append(stack.pop())
        stack.append(top)
    return stack
