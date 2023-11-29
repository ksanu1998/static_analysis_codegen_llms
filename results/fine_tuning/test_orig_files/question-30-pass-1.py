def solve(X, Y):

def solve(X, Y):
    steps = []
    while X!= Y:
        if X > Y:
            X -= Y
            steps.append("division by " + str(Y))
        else:
            Y -= X
            steps.append("multiplication by " + str(X))
    return steps
