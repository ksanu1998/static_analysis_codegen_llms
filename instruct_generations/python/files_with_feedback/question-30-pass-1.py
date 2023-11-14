def solve(X, Y):
    steps = []
    while X!= Y:
        if X > Y:
            X -= Y
            steps.append('divide')
        else:
            Y -= X
            steps.append('multiply')
    return steps
