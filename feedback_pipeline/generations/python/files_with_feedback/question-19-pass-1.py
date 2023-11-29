def findMode(a, n):
    maxCount = 0
    mode = None
    counts = {}
    for i in range(n):
        currentCount = counts.get(a[i], 0) + 1
        counts[a[i]] = currentCount
        if currentCount > maxCount:
            maxCount = currentCount
            mode = a[i]
    return mode
