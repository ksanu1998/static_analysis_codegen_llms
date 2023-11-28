def printLargest(seq, N):
    largest = 0
    for i in range(N):
        if seq[i] > largest:
            largest = seq[i]
    return largest
