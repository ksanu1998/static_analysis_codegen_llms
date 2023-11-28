def printBalancedExpression(a, b, c, d):
    if (a == 0 and b == 0):
        print("No balanced expression")
        return
    if (a == 0):
        print("(" + c + " + " + d + ")")
        return
    if (b == 0):
        print("(" + c + " - " + d + ")")
        return
    printBalancedExpression(a - 1, b, c, d)
    printBalancedExpression(a, b - 1, c, d)


a = 2
b = 2
c = "1"
d = "2"
printBalancedExpression(a, b, c, d)
