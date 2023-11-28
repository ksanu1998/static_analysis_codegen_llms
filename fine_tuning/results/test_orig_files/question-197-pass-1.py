def printBalancedExpression(a, b, c, d):

def printBalancedExpression(a, b, c, d):
    expression = ""
    if a > 0:
        expression += "(" * a
    if b > 0:
        expression += ")" * b
    if c > 0:
        expression += "[" * c
    if d > 0:
        expression += "]" * d
    return expression
