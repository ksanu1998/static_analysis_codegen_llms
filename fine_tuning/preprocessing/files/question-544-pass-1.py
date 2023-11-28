def is_redundant_braces(expression):
    # Check if the expression is a string
    if not isinstance(expression, str):
        return False

    # Remove any whitespace from the expression
    expression = expression.replace(" ", "")

    # Check if the expression is a valid Python expression
    try:
        ast.parse(expression, mode="eval")
    except SyntaxError:
        return False

    # Check if the expression contains redundant braces
    if expression.count("{") > expression.count("}"):
        return True
    else:
        return False
