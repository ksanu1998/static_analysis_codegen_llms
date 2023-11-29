def createSets(N):
    sets = []
    for i in range(1, N+1):
        sets.append(i)
    for i in range(1, N+1):
        if len(sets) == 2:
            break
        for j in range(i+1, N+1):
            if (i*j) % N == 0:
                sets.append(i*j)
                if len(sets) == 2:
                    break
    return sets
