def solve(s, n):
    left = 0
    right = 0
    maxlength = 0
    for i in range(n):
        if (s[i] == '('):
            left += 1
        else:
            right += 1
        if (left == right):
            maxlength = max(maxlength, 2 * right)
        elif (right > left):
            left = right = 0
    left = right = 0
    for i in range(n - 1, -1, -1):
        if (s[i] == '('):
            left += 1
        else:
            right += 1
        if (left == right):
            maxlength = max(maxlength, 2 * left)
        elif (left > right):
            left = right = 0
    return maxlength


print(solve("((()()()()(((())", 16))
