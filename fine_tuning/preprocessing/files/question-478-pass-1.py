def countStringPairs(a, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i][0]!= a[j][0] and a[i]!= a[j]:
                count += 1
    return count
