import math
N = 100001
adj = [[]for i in range(N)]
a = [0 for i in range(N)]
ans = [0 for i in range(N)]


def hasOddNumberOfDivisors(n):
    count = 0
    while n > 0:
        count += 1
        n //= 2
    return count % 2 == 1