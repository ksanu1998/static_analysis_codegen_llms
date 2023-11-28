def printNGE(arr):
    n = len(arr)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    while stack:
        result[stack.pop()] = -1
    return result
