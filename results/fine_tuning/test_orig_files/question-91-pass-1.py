def createSets(N):

def createSets(N):
    sets = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            if (i + j) % 2 == 0:
                sets.append([i, j])
                break
    return sets
