from collections import deque


def get_index(s, i):
    stack = deque()
    for j, char in enumerate(s):
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return j
            stack.pop()
    return -1
