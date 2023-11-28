def findDivisors(n):

def findDivisors(n):
    count = 0
    for i in range(1, n + 1):
        if i % n == 0:
            count += 1
    return count
