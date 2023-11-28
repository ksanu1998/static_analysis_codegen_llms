def minOperations(n, a, b, c):
    count = 0
    for i in range(n):
        if a[i]!= b[i]:
            count += 1
        if b[i]!= c[i]:
            count += 1
    return count
