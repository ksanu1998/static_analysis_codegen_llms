def ConstructList(Q):
    result = []
    for i in range(len(Q)):
        if Q[i] == 1:
            result.append(i)
        else:
            result.append(len(result) - i)
    return result
