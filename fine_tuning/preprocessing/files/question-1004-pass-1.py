def getMinSteps(K):
    steps = 0
    while K > 0:
        K >>= 1
        steps += 1
    return steps
