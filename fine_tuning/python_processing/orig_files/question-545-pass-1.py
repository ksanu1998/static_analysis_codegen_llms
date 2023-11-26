def balancedBrackets(Str):
    dep = 0
    minDep = 0
    for i in Str:
        if (i == '('):
            dep += 1
        else:
            dep -= 1
        if (minDep > dep):
            minDep = dep
    if (minDep < 0):
        for i in range(abs(minDep)):
            Str = '(' + Str
    dep = 0
    for i in Str:
        if (i == '('):
            dep += 1
        else:
            dep -= 1
    if (dep != 0):
        for i in range(dep):
            Str = Str + ')'
    return Str


Str = ")))()"
print(balancedBrackets(Str))
