def printBalancedExpression(a, b, c, d):
    expression = ""
    if a == "(" and b == ")":
        expression = "()"
    elif a == "{" and b == "}":
        expression = "{}".format(c, d)
    elif a == "[" and b == "]":
        expression = "[]"
    return expression