def findAns(a, b, n):
    count = 0
    for i in range(n+1):
        if a*i + b == 0:
            count += 1
    return count