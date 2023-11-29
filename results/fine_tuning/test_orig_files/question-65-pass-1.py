def countBinaries(N):

def countBinaries(N):
    count = 0
    for i in range(N+1):
        if i == 0 or i == 1:
            count += 1
        else:
            count += 2
    return count
