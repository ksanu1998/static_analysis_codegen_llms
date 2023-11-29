def isTriPerfect(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0:
            sum += i
    return sum + n == 2 * n
